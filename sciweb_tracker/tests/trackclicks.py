TEST_SITE = 'domain.com'

class TrackItems(TrackerBase):
	"""
	Test the scenario of tracking an item 
	Item types examples can be:
	 - link
	 - banner
	 - gallery/album

	Also tests for multiple clicks within same session / timedelta.
	"""

    def test_track_a_link_click(self):
    	"""Test tracking the click of a link on a particular page."""
        self.reset_track()
        _session = self.track.get('sid')
        self.trackset

        track['action'] = 'click'
        track['']
        