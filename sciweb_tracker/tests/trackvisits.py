from django.test import TestCase

TEST_SITE = 'test.com'

class TrackVisitsTypes(TrackerBase):

    def test_track_visit_types(self):
        """
        Keeps track of an entrance, pageview and unique visitors
        """
        self.reset_track()
        track = self.track
        track['action'] = 'view'
        c1 = '10.10.10.1'
        c2 = '10.10.10.2'
        visits = [
        	# new unique visit / entrance
        	{'sid': '123', 'ipaddress': c1, 'path': 'page1'},
        	{'sid': '999', 'ipaddress': c2, 'path': 'page2'},
        	{'sid': '999', 'ipaddress': c2, 'path': 'index'},
        	# same session / ip = +1 pageview
        	{'sid': '123', 'ipaddress': c1, 'path': 'page4'},
        	# new entrance to site with same IP / new session
        	{'sid': 'XXX', 'ipaddress': c1, 'path': 'page1'}
        ]
        # track the visits
        for v in visits:
        	self.dovisit(data=v)
        	
        self.assertEquals(Tracking.objects.count_uniques(), 2)
        self.assertEquals(Tracking.objects.count_entrances(), 3)
        self.assertEquals(Tracking.objects.count_pageviews(), 4)


