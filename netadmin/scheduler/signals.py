import json, csv
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from .models import Setup

@receiver(pre_save, sender=Setup)
def serializeCombo(sender, instance, **kwargs):
    address_list = []

    for location in instance.combo.location.all():
        address_list_name='{}-{}'.format(instance.combo.address_list_prefix.lower(), location.country_iso_code.lower())
        obj = {
            "address_list_name": address_list_name,
            "address_list_id": location.geoname_id
        }
        address_list.append(obj)

    payload=[{
        "router": instance.combo.router.ip,
        "timeout": instance.combo.timeout,
        "address_list": address_list
    }]

    instance.args=json.dumps(payload)
    instance.queue=instance.combo.router.consumer.name.lower()
    instance.task="worker.tasks.broad_message"
