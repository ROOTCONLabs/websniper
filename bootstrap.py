# bootstrap.py
# description: Dependency checker, bootstrapping WebSniper.
# author: @semprix

import sys, os, time, ConfigParser, platform

wsniperlibs =['socket','bs4','requests','termcolor','ping',
			 'ConfigParser', 'tld', 'shodan', 'lxml', 'signal',
			 'xmlrpclib']

print "[**] BootStrapping WebSniper. Please wait....."
time.sleep (3)
print "[+] Getting OS version"
print "[+] Checking dependency"
websniper = platform.platform()
print  ">> " +websniper
print "[+] Checking for required python modules"
for module_name in wsniperlibs:
  try:
    __import__(module_name)
    print ">> Module %s found." %(module_name)
    time.sleep(1)
  except ImportError:
    print "\033[91m -- Please install dependency ==>> (%s). \033[0m" %(module_name)
print ""
print "[--]BootStrap finishing"
time.sleep(3)
