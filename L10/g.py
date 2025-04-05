class LoggerContextManagerExample:
    def __init__(self, logfile):
        self.logfile = logfile
        self.log = None
        self.opened = False
    
    def __enter__(self):
        print('Entering the context')
        self.log = open(self.logfile, 'a')
        self.opened = True
        return self.log
    
    def __exit__(self, exc_type, exc_value, traceback):
        if self.opened:
            self.log.close()
            self.opened = False
            print ('Exiting the context')
        return True # Не преривати основну програму у випадку помилки

if __name__ == '__main__':
    with LoggerContextManagerExample('logfile.txt') as log:
        log.write('Hello, World!\n')
        log.write('Another Log Line\n')

    print()