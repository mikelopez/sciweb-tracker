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
        self.track = {
        	'sid': 'session123',
            'domain': TEST_SITE,
            'path': 'page2',
            'pageid': 567,
            'action': '',
            'ipaddress': '10.10.10.1'
        }
