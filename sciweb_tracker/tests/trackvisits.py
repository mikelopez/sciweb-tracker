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

        # new unique visit / entrance
        t = Tracking.objects.trackit(**track)
        track['sid'] = 'session456'
        track['ipaddress'] = '10.10.10.2'
        t2 = Tracking.objects.trackit(**track)
        # same ip = +1 pageviews
        track['pageid'] = 444
        track['path'] = 'index'
        t3 = Tracking.objects.trackit(**track)
        # same session / ip = +1 pageview
        track['sid'] = 'session123'
        track['ipaddress'] = '10.10.10.1'
        track['path'] = 'landing-page4'
        track['pageid'] = 543
        t4 = Tracking.objects.trackit(**track)
        # new entrance to site with same IP / new session
        track['sid'] = 'session999'
        track['ipaddress'] = '10.10.10.1'
        t5 = Tracking.objects.trackit(**track)

        self.assertEquals(Tracking.objects.count_uniques(), 2)
        self.assertEquals(Tracking.objects.count_entrances(), 3)
        self.assertEquals(Tracking.objects.count_pageviews(), 4)


