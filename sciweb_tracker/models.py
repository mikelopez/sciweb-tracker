from django.db import models

"""
Track and keep logs of what people do
"""

TRACK_TYPES = ['visit', 'object']

class Tracking(models.Model):
    """Track a particular link and redirect (optional)"""
    name = models.CharField(max_length=30)
    item_type = models.CharField(max_length=20, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    item_ctype = models.CharField(max_length=30, blank=True, null=True)
    counter = models.IntegerField(default=0, blank=True, null=True)
    ipaddress = models.CharField(max_length=20, blank=True, null=True)
    admin = models.NullBooleanField(default=False)
    date_tracked = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    redirect_to = models.TextField(blank=True, null=True)


