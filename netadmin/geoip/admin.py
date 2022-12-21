from django.contrib import admin

# Register your models here.
from netadmin.admin import MyModelAdmin
from .models import Location,Ipv4Database,Combo

class LocationAdmin(MyModelAdmin):
    search_fields = ["country_name"]
    list_filter = ("is_in_european_union", "continent_name",)
    ordering = ["country_name"]
    list_display = ("country_name", "country_iso_code", "geoname_id", "continent_code", "continent_name",)

class Ipv4DatabaseAdmin(MyModelAdmin):
    ordering = ["-date"]
    list_display = ("id", "root", "db", "date",)

class ComboAdmin(MyModelAdmin):
    filter_horizontal = ("location",)
    list_filter = ("router", )
    ordering = ["router"]
    list_display =("id", "router", "address_list_prefix", "timeout", "description")

admin.site.register(Location, LocationAdmin)
admin.site.register(Ipv4Database, Ipv4DatabaseAdmin)
admin.site.register(Combo, ComboAdmin)
