import uuid
from django.db import models

# Create your models here.
class Consumer(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=20)
    description = models.TextField(max_length=200, blank=True, null=True)

    def getUUID(self):
        uuid = "%s" % self.id
        return uuid

    def __str__(self):
        return self.name

class Router(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200, unique=True)
    ip = models.CharField(max_length=200)
    consumer = models.ForeignKey(Consumer, on_delete=models.CASCADE)

    def getUUID(self):
        uuid = "%s" % self.id
        return uuid

    def __str__(self):
        return self.name
