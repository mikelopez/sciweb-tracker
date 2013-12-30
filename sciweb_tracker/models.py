from django.db import models

"""
Visit track is just tracking a page visit.
Object track is tracking a particular object or link that was clicked.
"""
TRACK_TYPES = ['visit', 'object']

class LinkTracking(models.Model):
    """Track a particular link and redirect (optional)"""
    name = models.CharField(max_length=30)
    item_type = models.CharField(max_length=20, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    item_ctype = models.CharField(max_length=30, blank=True, null=True)
    counter = models.IntegerField(default=0, blank=True, null=True)
    admin = models.NullBooleanField(default=False)


