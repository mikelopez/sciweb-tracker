from base import *

TEST_SITE = 'test.com'

class TrackVisitTypes(TrackerBase):

    def test_track_visit_types(self):
        """
        Keeps track of an entrance, pageview and unique visitors
        """
        #self.reset_track()
        track = self.track
        track['action'] = 'view'
        c1 = '10.10.10.1'
        c2 = '10.10.10.2'


        visits = [
        	# new unique visit / entrance
        	{'sid': '123', 'ipaddress': c1, 'domain': 'test1.com',
             'path': 'page1', 'action': 'pageview'},

            # same session / ip = +1 pageview
            {'sid': '123', 'ipaddress': c1, 'domain': 'test1.com',
             'path': 'page4', 'action': 'pageview'},

            # new entrance to site with same IP / new sesson / entrance +1
            {'sid': 'XXX', 'ipaddress': c1, 'domain': 'test1.com',
             'path': 'page1', 'action': 'pageview'},

            # new session and ip / unique +1 / entrance +1
        	{'sid': '999', 'ipaddress': c2, 'domain': 'test2.com',
             'path': 'page2', 'action': 'pageview'},

            # same session / ip. pageview +1 / entrance +1
        	{'sid': '999', 'ipaddress': c2, 'domain': 'test2.com',
             'path': 'index', 'action': 'pageview'},   	

        ]


        # track the visits
        for v in visits:
        	self.dovisit(data=v)
        	
        self.assertEquals(Tracking.objects.get_uniques(), 2)
        self.assertEquals(Tracking.objects.get_uniques(domain='test1.com'), 1)
        self.assertEquals(Tracking.objects.get_uniques(domain='test2.com'), 1)

        self.assertEquals(Tracking.objects.get_entrances(), 3)
        self.assertEquals(Tracking.objects.get_entrances(domain='test1.com'), 2)
        self.assertEquals(Tracking.objects.get_entrances(domain='test2.com'), 1)

        self.assertEquals(Tracking.objects.get_pageviews(), 5)
        self.assertEquals(Tracking.objects.get_pageviews(domain='test1.com'), 3)
        self.assertEquals(Tracking.objects.get_pageviews(domain='test2.com'), 2)


