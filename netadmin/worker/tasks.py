from celery import shared_task

@shared_task(name="worker.tasks.broad_message")
def broad_message(message, *args, **kwargs):
    return True
