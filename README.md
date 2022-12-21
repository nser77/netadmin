# NETADMIN

NETADMIN is an admin tool written in Python/Django that allow the administrator to centralize GeoIP address list and distribute it through a Producer/Consumer architecture.

Both Producer and Consumer uses a MaxMind free account to download and store the address list.

On Producer side, please set your MaxMind download key into: ```netadmin/netadmin/geoip/maxmind/conf.json```

Each Consumer must download and store the IPs of each address list and update them through cron.


When you save a Combo into the NETADMIN application, you practically create a Celery-Beat PeriodicTask and save it on the Celery-Beat Backend; then when the task time arrives, the NETADMIN application submits the task via Celery-Beat (netadmin-beat.service must be running on the same machine) and the consumers must get and craft the message (with netadmin-worker.service).


A really useful example would be with MIKROTIK and its APIs.
