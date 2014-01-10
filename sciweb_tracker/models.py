from django.db import models

"""
Track and keep logs of what people do
"""

class TrackingManager(models.Manager):
    @classmethod
    def trackit(self, *args, **kwargs):
        """Log the tracking object."""
        t = Tracking(**kwargs)
        t.save()

    @classmethod 
    def get_uniques(self, **kwargs):
        """Get the unique visits by distinct ip address."""
        kwargs['action'] = 'view'
        return Tracking.objects.filter(**kwargs)\
                .values_list('ipaddress', flat=True).distinct().count()
        
        
    @classmethod 
    def get_entrances(self, **kwargs):
        """Figure out the entrances."""
        kwargs['action'] = 'view'
        return Tracking.objects.filter(**kwargs).distinct('sid').count()

    @classmethod
    def get_pageviews(self, **kwargs):
        """Figure out the page views."""
        kwargs['action'] = 'view'
        return Tracking.objects.filter(**kwargs).count()

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

