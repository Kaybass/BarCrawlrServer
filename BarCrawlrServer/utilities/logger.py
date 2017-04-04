class Logger:

    def __init__(self,filename):
        
        self.filename = filename

    def log(self, event):
        with open(self.filename,'a') as file:
            file.write(event.toString())

        return

    def getLog(self):
        log = None

        with open(self.filename,'r') as file:
            log = file.read()

        return log