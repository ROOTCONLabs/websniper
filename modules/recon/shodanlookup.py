# shodanlookup.py
# description: looks up the host using Shodan's API
# author: @shipcod3

import shodan, time, sys

class shodanlookup:

    def __init__(self, core):
        pass

    def run(self):
    #api config here: account.shodan.io
        SHODAN_API_KEY = "uAs67OallytytIdagyHKO1nAWxYetniW"

        try:
            api = shodan.Shodan(SHODAN_API_KEY)
            host = api.host(raw_input("Set RHOST IP: "))
            print ''
            print "[*] Starting Shodan IP search......"
            print ''
            time.sleep (3)
            print "[+] ISP: {}".format(host.get('isp', 'n/a'))
            print "[+] Country: {}".format(host.get('country_name', 'n/a'))
            print "[+] Longitude: {}".format(host.get('longitude', 'n/a'))
            print "[+] Longitude: {}".format(host.get('latitude', 'n/a'))
            print "[+] Organization: {}".format(host.get('org', 'n/a'))
            print "[+] Operating System: {}".format(host.get('os', 'n/a'))
            print "[+] Timestamp: {}".format(host.get('timestamp', 'n/a'))
            print ''
            print "[***] Printing available port(s)"
            print ''
            time.sleep(1)
            for item in host['data']:
                print "[!] Port: {}".format(item['port'])
                print "{}".format(item['data'])
            print'[####] Done!!!'
            print ''
        except Exception, e:
            print '[!!!!] Error: %s' % e
            sys.exit(1)
