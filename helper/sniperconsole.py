class consoleprint:
    def __init__(self):
        pass

    def out(self, output=""):
        print output
        return

    def prompt(self):
        return "websniper>"

    def banner(self):
        print ""
        print "\033[94m__        __   _    ____        _                  \033[0m"
        print "\033[94m\ \      / /__| |__/ ___| _ __ (_)_ __   ___ _ __  \033[0m"
        print "\033[94m \ \ /\ / / _ \ '_ \___ \| '_ \| | '_ \ / _ \ '__| \033[0m"
        print "\033[94m  \ V  V /  __/ |_) |__) | | | | | |_) |  __/ |    \033[0m"
        print "\033[94m   \_/\_/ \___|_.__/____/|_| |_|_| .__/ \___|_|    \033[0m"
        print "\033[94m                                 |_|               \033[0m"
        print""
        print('\033[94m****************************************** \033[0m')
        print('\033[94mDevs: @semprix, @shipcod3, @godflux   \033[0m')
        print('\033[94mVersion: v1.0\033[0m')
        print('\033[94m****************************************** \033[0m')
        print ""

    def help(self):
        print ''
        print('******************************************')
        print "Available commands:"
        print "help, show, back, credits, quit\n"
        print "To run specific module or exploit do: websniper>modules <enter> recon <enter> run httpheaderanalyzer"
        print ""
        return

    def credits(self):
        print "Credits to ROOTCON Labs"
