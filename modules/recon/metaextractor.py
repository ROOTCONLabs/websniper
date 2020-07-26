# metaextractor.py
# description: extracts metadata from target website
# author: @semprix

import ping, time, sys, urllib2, subprocess, socket, ConfigParser, string
from urllib import urlopen
from lxml import etree

class metaextractor:
  
  def __init__(self, core):
    pass

  def run(self):
    print 'Set RHOST:',
    rhost = raw_input()
    print 'Set RPORT:',
    rport = raw_input()
    print ""
    print "[*] Starting meta extractor..."
    print ""
    time.sleep(3)
    
    if rport == '80':
     try:
       f = urlopen ("http://" + rhost).read()
       tree = etree.HTML( f )
       extractor = tree.xpath( "//meta" )
       print "[+] Extracting meta on " + rhost
       print "[+] Using port " + rport
       print ""
       for i in extractor:
	print etree.tostring( i )
     except Exception:
       pass
       print "[!] Host not reachable"
       print ""
    
    elif rport == '443':
     try:
       f = urlopen ("https://" + rhost).read()
       tree = etree.HTML( f )
       extractor = tree.xpath( "//meta" )
       print "[+] Extracting meta on " + rhost
       print "[+] Using port " + rport
       time.sleep(3)
       for i in extractor:
	print etree.tostring( i )	
     except Exception:
	pass
	print "[!] Host not reachable"
	print ""
    
    else:
	   print "[!] Error extracting meta"
    
    print'[#] Done!!!'
    print ""
    time.sleep(3)

