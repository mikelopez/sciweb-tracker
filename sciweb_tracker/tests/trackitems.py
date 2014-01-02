TEST_SITE = 'domain.com'

class TrackItems(TrackerBase):
    def test_track_items(self):
        self.reset_track()
        track = self.track
        track['action'] = 
