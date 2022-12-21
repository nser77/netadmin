from django.contrib import admin

# Register your models here.
from .models import Setup
from netadmin.admin import MyModelAdmin
from django_celery_beat.models import PeriodicTask

class SetupAdmin(MyModelAdmin):
    exclude = ("args", "kwargs", "exchange","routing_key","headers", "queue", "task", "priority", "expire_seconds")
    list_display = ("setup","combo")

admin.site.unregister(PeriodicTask)
admin.site.register(Setup, SetupAdmin)
