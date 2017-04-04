class Logger:

    def __init__(self,filename):
        
        self.filename = filename

    def log(self, event):
        with open(self.filename,'a') as file:
            file.write(event.toString() + '\n')

        return

    def getLog(self):
        log = []

        with open(self.filename,'r') as file:
            for line in file:
                log.append(line)

        return log