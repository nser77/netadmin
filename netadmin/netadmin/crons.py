import csv
from pathlib import Path
from datetime import date, time, datetime, timedelta
from geoip.models import Ipv4Database
from scheduler.models import Task
from worker.tasks import broad_message

def onceTask(date_now, start_date):
    if start_date == date_now:
        return True

    return False

def dailyTask(start_date, date_now, freq_interval):
    return False

def weeklyTask(date_now, freq_interval):
    if date_now.weekday() == freq_interval:
        return True

    return False

def montlyTask(date_now, freq_interval):
    if date_now.day == freq_interval:
        return True

    return False

def runnable(start_date, freq_type, freq_interval, time_of_day):
    run=False
    date_now=date(datetime.today().year, datetime.today().month, datetime.today().day)
    time_now=time(datetime.today().hour, datetime.today().minute, datetime.today().second)

    if time_of_day <= time_now:
        if freq_type == 'O':
            run = onceTask(date_now, start_date)
        if freq_type == 'D':
            run = dailyTask(start_date, date_now, freq_interval)
        if freq_type == 'W':
           run = weeklyTask(date_now, freq_interval)
        if freq_type == 'M':
           run = montlyTask(date_now, freq_interval)

    return run

def exec():
    from .celery import app as celery_app

    __all__ = ('celery_app',)

    import os
    from celery import Celery

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'netadmin.settings')

    app = Celery('netadmin')
    app.config_from_object('django.conf:settings', namespace='CELERY')
    app.autodiscover_tasks()

    tasks=Task.objects.filter(
        start_date__lte=date(datetime.today().year, datetime.today().month, datetime.today().day),
        #time_of_day=time(datetime.today().hour, datetime.today().minute, datetime.today().second),
    )

    ip_db=Ipv4Database.objects.filter(
        db="GeoLite2-Country-Blocks-IPv4.csv",
    ).order_by("-date")[:1]

    geoip_ip_db=Path(
        ip_db[0].path,
    )

    if not geoip_ip_db.exists():
        print("Database './{}' does not exist".format(geoip_ip_db))
        exit(0)

    for task in tasks:
        if runnable(task.start_date, task.freq_type, task.freq_interval, task.time_of_day):
            print("Running task: {}".format(task.id))

            for location in task.combo.location.all():
                address_list='{}-{}'.format(task.combo.address_list_prefix.lower(), location.country_iso_code.lower())
                ips = []
                with geoip_ip_db.open() as f:
                    ip_db=csv.reader(f)
                    for r in ip_db:
                        if location.geoname_id in r[1]:
                            ips.append(r[0])
                    f.close()

                payload={"router": task.combo.router.ip, "address_list": address_list, "timeout": task.combo.timeout, "addresses": ips }

                broad_message.apply_async((payload,), queue=task.combo.router.consumer.name.lower())
