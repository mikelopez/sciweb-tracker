import sys
from sciweb_tracker.models import *
from django.test import TestCase
TEST_SITE = 'domain.com'

class TrackerBase(TestCase):
    """Base tracker class with data """
    track = {
  		'sid': '',
  		'action': '',
  		'domain': '',
  		'path': '',
  		'pageid': '',
  		'item_type': '',
  		'item_id': '',
  		'item_ctype': '',
  		'counter': '',
  		'ipaddress': '',
  		'admin': '',
  		'ua': '',
  		'created': '',
  		'redirect_to': ''
    }
    session = ''

    def trackset(self, k, v):
    	"""Quick setter"""
     	self.track[k] = v

    def dovisit(self, data=None):
        """Perform simulated visit."""
        if not data:
      		data = self.track
        self.trackset('action', 'view')
        return Tracking.objects.trackit(**data)

    def reset_track(self):
        """A user goes to test.com/page2."""
        self.track = {}
