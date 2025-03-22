# Замикання - життєвий приклад
from datetime import datetime
from typing import Callable

def init_log(filename:str,reset:bool=True):
    
    def read_log():
        with open(filename,'r')as f:
            return f.readlines()

    def write_log(message:str):
        with open(filename,'a')as f:
            f.write(f"{datetime.now()} : {message}\n")

    if reset:
        f=open(filename,'w')
        f.close()

    return read_log, write_log

if __name__=='__main__':
    read,write=init_log('log.txt')
    write('some action')
    write('another action')
    write('one more action')
    read2,write2=init_log('log2.txt',reset=False)
    write2('some action')
    write2('another action')
    write2('one more action')
    print('from log.txt:')
    for line in read():
        print(line.rstrip())
    print()
    print('from log2.txt:')
    for line in read2():
        print(line.rstrip())

