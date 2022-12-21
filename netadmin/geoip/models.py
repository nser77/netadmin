import uuid
from django.db import models

# Create your models here.
from items.models import Router

class Location(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    geoname_id = models.CharField(max_length=200, null=False)
    locale_code = models.CharField(max_length=200, null=False)
    continent_code = models.CharField(max_length=200, null=False)
    continent_name = models.CharField(max_length=200, null=False)
    country_iso_code = models.CharField(max_length=200, null=False)
    country_name = models.CharField(max_length=200, null=False)
    is_in_european_union = models.BooleanField(null=False)

    def continentNameUpper(self):
        return self.continent_name.upper()

    def continentNameLower(self):
        return self.continent_name.lower()

    def countryNameUpper(self):
        return self.country_name.upper()

    def countryNameLower(self):
        return self.country_name.lower()

    def humanName(self):
        hn="{} ({})".format(self.country_name, self.continent_code)
        return hn

    def getUUID(self):
        uuid = "%s" % self.id
        return uuid

    def __str__(self):
        return self.humanName()

class Ipv4Database(models.Model):
    id = id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    path = models.CharField(max_length=200, unique=True, null=False)
    root = models.CharField(max_length=200, null=False)
    db = models.CharField(max_length=200, null=False)
    date =  models.DateTimeField(auto_now_add=True, null=False)

    def __str__(self):
        return self.path

class Combo(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    router = models.ForeignKey(Router, on_delete=models.CASCADE, null=False)
    timeout = models.CharField(max_length=200, default="7d", null=False)
    address_list_prefix = models.CharField(max_length=33, default="geoip", null=False)
    location = models.ManyToManyField(Location)
    description =  models.TextField(max_length=200, blank=True, null=True)

    def getUUID(self):
        uuid = "%s" % self.id
        return uuid

    def __str__(self):
        return self.getUUID()
