from base import *


TEST_SITE = 'domain.com'

class TestTrackClicks(TrackerBase):
    """
    Test the scenario of tracking an item 
    Item types examples can be:
     - link
     - banner
     - gallery/album

    Also tests for multiple clicks within same session / timedelta.
    """
    def __simulate_sample_visit(self, **kwargs):
        """simlates a sample visit so we can get a session."""
        self.trackset('action', 'view')
        self.trackset('path', 'index')
        self.trackset('ipaddress', '10.10.10.1')
        self.trackset('sid', 'SESSION123')
        # set any overrides
        if kwargs:
            for k, v in kwargs.items():
                self.trackset(k, v)
        return Tracking.objects.trackit(**self.track)


    def __do_click_link(self, **kwargs):
        """Perform the click on a link simulation by setting data."""
        # override from the data that simulate method did
        self.trackset('action', 'click')
        # keep the same page
        self.trackset('item_type', 'link')
        self.trackset('item_id', 123)
        self.trackset('item_ctype', 'productlink')
        self.trackset('redirect_to', 'http://linkthatwasclicked.com')
        # set any overrides
        if kwargs:
            for k, v in kwargs.items():
                self.trackset(k, v)
        return Tracking.objects.trackit(**self.track)


    def test_track_a_link_click(self):
        """Test tracking the click of a link on a particular page."""
        self.reset_track()
        # run a simulated request
        self.__simulate_sample_visit(domain="test1.com")
        self.__do_click_link()

        # should have 1 unique, 1 entrance, 1 pageview, and 1 click on our link
        self.assertEquals(Tracking.objects.get_uniques(domain="test1.com"), int(1))
        self.assertEquals(Tracking.objects.get_entrances(domain="test1.com"), int(1))
        self.assertEquals(Tracking.objects.get_pageviews(domain="test1.com"), int(1))

        itype, iid = self.track.get('item_type'), self.track.get('item_id')
        self.assertEquals(len(Tracking.objects.get_by_item(itype, iid)), int(1))
        self.assertEquals(Tracking.objects.get_by_item(itype, iid).count(), int(1))

        self.__simulate_sample_visit(ipaddress='10.10.10.2', 
                                     sid='SESSION999',
                                     path='page123')
        self.trackset('ipaddress', '10.10.10.2')
        self.__do_click_link()
        
        # another user hits page1, then back to index, then clicks the link
        # should have 3 pageviews, 2 uniques, 2 entrances
        # should have 1 item tracks with counter 2 
        self.assertEquals(Tracking.objects.get_uniques(), int(2))
        self.assertEquals(Tracking.objects.get_entrances(), int(2))
        self.assertEquals(Tracking.objects.get_pageviews(), int(2))
        itype, iid = self.track.get('item_type'), self.track.get('item_id')
        self.assertEquals(len(Tracking.objects.get_by_item(itype, iid)), int(2))        
        self.assertEquals(Tracking.objects.get_by_item(itype, iid).count(), int(2))



