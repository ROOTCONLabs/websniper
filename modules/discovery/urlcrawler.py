# urlcrawler.py
# description: crawls the URL
# author: @shipcod3

import sys, requests, time, os

from bs4 import BeautifulSoup 

class urlcrawler:
  
  def __init__(self, core):
    pass

  def run(self):
    print 'Set RHOST:',
    rhost = raw_input()
    print 'Set RPORT:',
    rport = raw_input()
    print ""
    print "[*] Starting URL crawler..."
    time.sleep(3)
    if rport == '80':
        print ('[+] Crawling unauthenticated HTTP')
        req  = requests.get("http://" + rhost)
        data = req.text
        soup = BeautifulSoup(data)
        for link in soup.find_all('a'):
            print >> f, (link.get('href'))
        f.close()

    elif rport == '443':
        print ('[+] Crawling unauthenticated HTTPS')
        req  = requests.get("https://" + rhost)
        data = req.text
        soup = BeautifulSoup(data)
        for link in soup.find_all('a'):
            print >> f,(link.get('href'))
        f.close()

    else:
        print '[!] Error performing url crawl'

    print'[#] Done...'
time.sleep(3)