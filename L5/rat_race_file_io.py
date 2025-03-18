import threading
from time import sleep

def f1():
    with open('text.txt','x+') as f1:
        sleep(5) # симуляція тяжкої роботи
        f1.write('f1')
        print('f1 Done')

def f2():
    with open('text.txt','x+') as f2:
        f2.write('f2f2f2')
        print('f2 Done')

if __name__=="__main__":
    task1=threading.Thread(target=f1, group=None)
    task2=threading.Thread(target=f2, group=None)
    task1.start()
    task2.start()
    task1.join()
    task2.join()