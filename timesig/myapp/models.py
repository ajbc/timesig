from django.db import models

class Doc(models.Model):
    title = models.CharField(max_length=80)
    author = models.CharField(max_length=80)
    filename = models.CharField(max_length=80)

class UserDoc(models.Model):
    doc = models.IntegerField()
    user = models.IntegerField()
    lastModified = models.DateTimeField()
    lastLocation = models.IntegerField()
    active = models.BooleanField()