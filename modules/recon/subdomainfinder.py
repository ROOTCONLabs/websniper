# subdomainlookup.py
# description: uses google to search for subdomains
# forker: @shipcod3
#
# copyright (c)2009:  Sertan Kolat - sertan@olympos.org
# cookie support and additional patches: Bedirhan Urgun

import re, sys, urllib, urllib2, cookielib, time, os

def Uniq(u):
	un=[]
	[un.append(i) for i in u if not un.count(i)]
	return un

class Webdog:
	def	__init__(self):
		self.usestart = False
		self.start = 0
		self.useragent = 'Mozilla/5.0 ' \
			+ '(Windows; U; Windows NT 5.1; en-US; rv:1.9.1.3) ' \
			+ 'Gecko/20090824 Firefox/3.5.3'
		# added cookie jar and opener member initialization
		self.cj = cookielib.CookieJar()
		self.opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(self.cj))
		
	def get(self, url):
		try:
			request = urllib2.Request(url)
			request.add_header('User-agent', self.useragent)

			# Optionally use Accept-Language header
			#request.add_header('Accept-Language', 'en-us,en,tr;q=0.5')

			result = self.opener.open(request)
			content = result.read()
		
		except KeyboardInterrupt:
			globals()['results'].sort()
			print ('[!] %s subdomains found for %s\n' % (len(results), w.domainname), GREEN)
			for r in globals()['results']:
				print r
			print '\n- Error: canceled by user'
		
		except urllib2.HTTPError, e:
			print e

		except: raise RuntimeError('Error: unable to open url')
		
		return content
	
	def search(self, keyw):
		url = 'http://www.google.com/m/search?q=%s' % urllib.quote(keyw)
		if self.usestart:
			if self.start == 0:
			 print '[!] Found more than 20 subdomains, This may take a long time depending on target.'
			self.start = self.start + 10
			url = url + '&start=%s' % self.start
			sys.stdout.write('.')
		content = self.get(url)
		results = re.findall(
				'<cite>\s?([-\w.]*?\.%s).*?</cite>' % self.domainname, content)
		results = Uniq(results)
		
		return results
	
def subdomainfinder():
	print 'Set RHOST (use TLD):',
	rhost = raw_input()
	print ""
	print "[*] Starting subdomain finder..."
	print ""
	results = []
	w = Webdog()
	w.domainname = rhost
	results = w.search('site:' + w.domainname)
	if len(results) < 1:
		print ('  >> No result found for %s' % w.domainname)
	else:
		others = results
		while len(others) > 0:
			if len(results) > 20:
				w.usestart = True
				lookup = 'site:' + w.domainname + ' -site:' + ' -site:'.join(results)
			else:
				lookup = ' -site:' + ' -site:'.join(results) + ' site:' + w.domainname
			others = w.search(lookup)
			if len(others) > 0:
				results = list(set(results) | set(others))
	
	results.sort()
	print '[!] %s subdomains found for %s\n' % (len(results), w.domainname)
	for r in results:
		print "[+]"+r
		time.sleep(2)
		print ""
        print "[#] Done!!!"	
        print ""
        time.sleep(3)
     
