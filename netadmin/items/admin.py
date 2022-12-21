from django.contrib import admin

# Register your models here.
from .models import Consumer, Router
from netadmin.admin import MyModelAdmin

class ConsumerAdmin(MyModelAdmin):
    #search_fields = ["name"]
    list_filter = ("location", )
    ordering = ["name"]
    list_display = ("name", "location", "description")

class RouterAdmin(MyModelAdmin):
    search_fields = ["name", "ip"]
    list_filter = ("consumer",)
    ordering = ["ip", "consumer"]
    list_display = ("name", "ip", "consumer",)

admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(Router, RouterAdmin)
