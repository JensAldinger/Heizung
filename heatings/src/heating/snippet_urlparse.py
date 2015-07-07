import urlparse
url = 'http://foo.appspot.com/abc?def=ghi'
parsed = urlparse.urlparse(url)
print urlparse.parse_qs(parsed.query)['def']
	

import urlparse
url = 'http://example.com/?q=abc&p=123'
par = urlparse.parse_qs(urlparse.urlparse(url).query)

print par['q'], par['p']

