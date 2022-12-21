# NETADMIN

NETADMIN is an admin tool written in Python/Django that allow the administrator to centralize GeoIP address list and distribute it through a Producer/Consumer architecture.

Both Producer and Consumer uses a MaxMind free account to download and store the address list.
On Producer side, please set your MaxMind download key into: ```netadmin/netadmin/geoip/maxmind/conf.json```

Each Consumer must download and store the IPs of each address list and update them through cron.


When you save a Setup into the NETADMIN application, you practically create a Celery-Beat PeriodicTask and save it on the Celery-Beat Backend; then when the task time arrives, the NETADMIN application submits the task via Celery-Beat (netadmin-beat.service must be running on the same machine) and the consumers must get and craft the message (with netadmin-worker.service).


A really useful example would be with MIKROTIK and its APIs.

## Requirements
Before installation, make sure that your system has the following packages installed:

```
root@ubuntu:/opt# apt-get update
root@ubuntu:/opt# apt-get install python3-venv
```

## Installation
Download and install NETADMIN with ```git``` and ```venv```.
```
root@ubuntu:/opt# cd /opt
root@ubuntu:/opt# git clone git@github.com:nser77/netadmin.git
root@ubuntu:/opt/netadmin# cd netadmin/
root@ubuntu:/opt/netadmin# python3 -m venv ./venv
root@ubuntu:/opt/netadmin# source ./venv/bin/activate
(venv) root@ubuntu:/opt/netadmin# pip install -r requirements.txt
(venv) root@ubuntu:/opt/netadmin# deactivate
```

Create NETADMIN user and assign the ownerships:
```
root@ubuntu:/opt/netadmin# adduser --system --group --home /opt/netadmin/netadmin --no-create-home netadmin
root@ubuntu:/opt/netadmin# chown -R netadmin: /opt/netadmin
```

Create system's unit links:
```
root@ubuntu:/opt/netadmin# ln -s /opt/netadmin/etc/systemd/system/* /etc/systemd/system/
root@ubuntu:/opt/netadmin# ln -s /opt/netadmin/etc/default/* /etc/default/
root@ubuntu:/opt/netadmin# ln -s /opt/netadmin/etc/tmpfiles.d/* /etc/tmpfiles.d/
root@ubuntu:/opt/netadmin# systemctl enable netadmin
root@ubuntu:/opt/netadmin# systemctl enable netadmin-beat
```

## Update MaxMind address list
After the installation, you may want to run your first MaxMind Update on the Producer side:
```
root@ubuntu:/opt/netadmin# cd /opt/netadmin/netadmin
root@ubuntu:/opt/netadmin/netadmin# ../venv/bin/python manage.py updateMaxMind
```
