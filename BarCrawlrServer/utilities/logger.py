class Logger:
    
    log = None

    def log(self,string):
        
        self.log += string

    def getLog(self):

        return self.log
