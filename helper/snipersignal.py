class signalhandler:
    def __init__(self):
        pass

	def sigint_handler(signum, frame):
    		print '>> Use Quit to shutdown cleanly'
 
		signal.signal(signal.SIGINT, sigint_handler)