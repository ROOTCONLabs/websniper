# core.py
# description: WebSniper Framework core file
# author: @semprix

import os, sys, time

#common functions
class funcs:
    #initialize
    def __init__(self):
        print "WebSniper Initializing..."
        time.sleep(2)
        self.module_types = ['recon', 'discovery', 'exploits']
        self.modules_list = {}

	def list_modules(self):
        	for m_type in self.module_types:
         	 self.modules_list[m_type] = []
          	 dirs = os.listdir("modules/"+m_type)
          	for x in dirs:
                 if x[-3:] == ".py" and x[0:2] != "__":
                    self.modules_list[m_type].append(x[0:len(x)-3])
                    return self.modules_list

    #run module needs dict ex: {'type': 'recon', 'name': 'httpanalyzer'}
    def run_module(self, data):        
        module_type = data["type"]
        sys.path.append(r'modules/'+module_type)
        module_name = data["name"]
        module_class = data["name"]
        module = __import__(module_name)
        my_class = getattr(module, module_class)
        instance = my_class(self)
        instance.run()

    #return all the module types
    def modules_types(self):
        return self.module_types

    def loopz(self):
        mgr = output_mgr.console_print()
        print dir(mgr)
        mgr.out("WebSniper")