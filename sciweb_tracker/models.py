from django.db import models

"""
Track and keep logs of what people do
"""

class TrackingManager(models.Manager):
    pass


class Tracking(models.Model):
    """
    Track some stuff.
    """
    sid = models.CharField(max_length=100, default='direct')
    action = models.CharField(max_length=10)
    domain = models.CharField(max_length=100)
    path = models.CharField(max_length=50, blank=True, null=True)
    pageid = models.IntegerField(blank=True, null=True)
    item_type = models.CharField(max_length=20, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    item_ctype = models.CharField(max_length=30, blank=True, null=True)
    counter = models.IntegerField(default=0, blank=True, null=True)
    ipaddress = models.CharField(max_length=20, blank=True, null=True)
    admin = models.NullBooleanField(default=False)
    ua = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    redirect_to = models.TextField(blank=True, null=True)
    objects = TrackingManager()

