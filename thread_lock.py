import threading
from time import sleep


def before(lock):
    global x
    x = 0
    print x
    #print dir(lock)
    lock.acquire()
    
    #print x
    try:
        while x<350:
            x+=1
        sleep(0.001)
        print x
    finally:
        pass
        lock.release()
    
def after(lock):
    global x
    x = 450
    print x
    lock.acquire()
    
    #print x
    try:
        while x<600:
            sleep(0.001)
            x+=1
        print x
    finally:
        lock.release()
    

def main():
    global x
    x = 0
    lock = threading.Lock()
    t1 = threading.Thread(target=before, args=(lock,))
    t2 = threading.Thread(target=after, args=(lock,))
    t1.start()
    t2.start()
main()
    
