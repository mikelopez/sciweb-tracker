from datetime import datetime, timedelta
import pytz
from django.db import models

"""
Track and keep logs of what people do
"""

class TrackingManager(models.Manager):
    @classmethod
    def trackit(self, *args, **kwargs):
        """Log the tracking object."""

        t = Tracking.objects.filter(**kwargs)
        # update existing...refresher..
        if len(t) > 0:
            t = t[0]
            if (datetime.now() - t.created).seconds <= 300:
                setattr(t, 'counter', (getattr(t, 'counter', 0) + 1))
                t.save()
            else:
                # or add new record
                kwargs['created'] = datetime.now()
                t = Tracking(**kwargs)
                t.save()
        else:
            # or add new record
            kwargs['created'] = datetime.now()
            t = Tracking(**kwargs)
            t.save()  



    @classmethod
    def getdistinct(self, distinct_field, **kwargs):
        """mysql no likey distinct-on because fuck you. """
        q = []
        dups = []
        for i in Tracking.objects.filter(**kwargs):
            if not getattr(i, distinct_field) in dups:
                dups.append(getattr(i, distinct_field))
                q.append(i)
        return q



    @classmethod 
    def get_uniques(self, **kwargs):
        """Get the unique visits by distinct ip address."""
        kwargs['action'] = 'view'
        return len(self.getdistinct('ipaddress', **kwargs))

        
    @classmethod 
    def get_entrances(self, **kwargs):
        """Figure out the entrances."""
        kwargs['action'] = 'view'
        return len(self.getdistinct('sid', **kwargs))
        
    @classmethod
    def get_pageviews(self, **kwargs):
        """Figure out the page views."""
        kwargs['action'] = 'view'
        return len(Tracking.objects.filter(**kwargs))

    @classmethod 
    def get_by_item(self, itype, iid, **kwargs):
        """Get a track by item id and type"""
        return Tracking.objects.filter(action='click', item_type=itype, 
                                       item_id=iid, **kwargs)



class Tracking(models.Model):
    """
    Track some stuff.
    """
    sid = models.CharField(max_length=100, default='direct')
    action = models.CharField(max_length=10)
    domain = models.CharField(max_length=100)
    name = models.CharField(max_length=30, blank=True, null=True)
    path = models.CharField(max_length=50, blank=True, null=True)
    pageid = models.IntegerField(blank=True, null=True)
    referer = models.CharField(max_length=100, blank=True, null=True, default='direct')
    item_type = models.CharField(max_length=20, blank=True, null=True)
    item_id = models.IntegerField(blank=True, null=True)
    item_ctype = models.CharField(max_length=30, blank=True, null=True)
    counter = models.IntegerField(default=0, blank=True, null=True)
    ipaddress = models.CharField(max_length=20, blank=True, null=True)
    admin = models.NullBooleanField(default=False)
    ua = models.TextField(blank=True, null=True)
    created = models.DateTimeField(blank=True, null=True)
    redirect_to = models.TextField(blank=True, null=True)
    objects = TrackingManager()

