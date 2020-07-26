# grabheader.py
# description: HTTP Header Analyzer forked by httphacker
# author: @semprix

import sys, urllib2, time

class httpheaderanalyzer:
	
	def __init__(self, core):
		pass

	def run(self):
		print 'Set RHOST (use http(s)//domain.tld format):',
		rhost = raw_input()
		print ""
		print "[*] Starting header analysis..."
		print ""
		
		try:
		 response = urllib2.urlopen(rhost)
		 grabserver = response.info().getheader('server')
		 print "[+] Grabbing web server version"
		 time.sleep(2)
		 if grabserver is None:
		  print '>> Failed to get header value *not vulnerable*'
		 else:
		  print '>> ' + grabserver
		 grabplatform = response.info().getheader('x-powered-by')
		 print "[+] Grabbing platform "
		 time.sleep(2)
		 if grabplatform is None:
			print '>> No response from server'
		 else:
			print '>> ' + grabplatform
		 grabcontent = response.info().getheader('content-type')
		 print "[+] Grabbing content type "
		 time.sleep(2)
		 if grabcontent is None:
			print '>> Failed to get header value *not vulnerable*'
		 else:
			print '>> ' + grabcontent
		 grabframeopt = response.info().getheader('x-frame-options')
		 print "[+] Grabbing x-frame-options "
		 time.sleep(2)
	
		 if grabframeopt is None:
			print '>>  No x-frame-options *vulnerable to click-jacking possible*'
		 else:
			print'>> ' + grabframeopt + ' *flag found (not vulnerable)*'
		
		 grabxssprotect = response.info().getheader('x-xss-protection')
		 print "[+] Grabbing x-xss-protection "
		 time.sleep(2)
		 if grabframeopt is None:
			print '>> No XSS protection *vulnerable to XSS possible*'
		 else:
			print '>> ' + grabframeopt + ' *flag found (not vulnerable)*'
		
		 grabxcontent = response.info().getheader('x-content-type-options')
		 print "[+] Grabbing x-content-type-options"
		 time.sleep(2)
		 
		 if grabxcontent is None:
			print '>> No x-content-type-options *vulnerable to MIME sniffing possible*'
		 else:
			print '>> ' + grabxcontent + ' *flag found (not vulnerable)*'
		 print ""
		 print "[+] Checking for SSL settings"
		 print ""
		 time.sleep(2)
		 grabhsts = response.info().getheader('Strict-Transport-Security')
	
		 if grabhsts is None:
			print '>>  No HSTS Policy *vulnerable*'
		 else:
			print '>> ' + grabhsts + ' *flag found (not vulnerable)*'
		
		except Exception:
			pass
			print "[!] Host not reachable"
	
		print ""
		print'[#] Done!!!'
		print ""
		time.sleep(3)


