from plugins.plugin import Plugin
'''
#Uncomment to use
class Test(Plugin):
    name = "Test"
    optname = "test"
    has_opts = True
    implements = ["handleResponse"]
    def add_options(self,options):
        options.add_argument("--testy",action="store_true",
                help="This is a test option")
    def initialize(self,options):
        self.worked = options.test
        if self.worked:
            print "Hurrah!"
        else:
            print "Fail."
    def handleResponse(self,request,data):
        print "Response received..."
'''
