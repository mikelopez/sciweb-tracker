class TrackerBase(TrackerBase):
	"""Base tracker class with data """
    self.track = {
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

    def reset_track(self):
    	"""A user goes to test.com/page2."""
        self.track = {
        	'sid': 'session123',
            'domain': TEST_SITE,
            'path': 'page2',
            'pageid': 567,
            'action': '',
            'ipaddress': '10.10.10.1',
