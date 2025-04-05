class logger:
    def __init__(self, filename):
        self.filename = filename
        
    def __call__(self, *args, **kwargs):
        with open(self.filename, 'a') as f:
            print(*args, file=f, **kwargs)

    def getLogs(self):
        with open(self.filename, 'r') as f:
            return f.readlines()
    
    def reset(self):
        with open(self.filename, 'w') as f:
            pass

if __name__ == '__main__':
    log = logger('log.txt')
    log('Hello, World!')
    log('Another Log Line')
    for line in log.getLogs():
        print(line, end='')
    log.reset()