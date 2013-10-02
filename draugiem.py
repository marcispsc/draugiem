import requests
import simplejson as json
from hashlib import md5
from urllib import urlencode

class Draugiem:
	URL_AUTH = 'http://api.draugiem.lv/authorize/'
	URL_API_GET = 'http://api.draugiem.lv/json/'
	URL_API_POST = 'https://api.draugiem.lv/v5/'

	_id = 0
	_key = None
	_apikey = None

	def __init__(self, id, key, apikey=None):
		self._id = id
		self._key = key
		self._apikey = apikey

	def get_apikey(self):
		return self._apikey

	def set_apikey(self, apikey):
		self._apikey = apikey

	def get_login_url(self, callback):
		return '%s?%s' % (self.URL_AUTH, urlencode({
			'app': self._id,
			'hash': md5('%s%s' % (self._key, callback)).hexdigest(),
			'redirect': callback,
		}))

	def authorize(self, code):
		return self.api('authorize', code=code)

	def api(self, action, method='GET', **kwargs):
		if method == 'POST':
			post = {
				'auth': {
					'app': self._key,
				},
				'method': {
					action: kwargs,
				}
			}
			if self._apikey:
				post['auth']['apikey'] = self._apikey
			return requests.post(self.URL_API_POST, data=json.dumps(post)).json()
		else:
			kwargs['app'] = self._key
			kwargs['action'] = action
			if self._apikey:
				kwargs['apikey'] = self._apikey
			return requests.get(self.URL_API_GET, params=kwargs).json()