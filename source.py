'''import time
from threading import Thread



def sleeper(i):
   print("thread %d sleeps for %d second" %(i,i))
   time.sleep(i+1)
   print("woke up %d" %i)


for i in range(3):
   t=Thread(target=sleeper,args=(i,))
   print("executed successfully")
   t.start()


'''

import threading
import time

exitFlag=0

class myThread(threading.Thread):
    """docstring threadId,threadName,counter .
    """
    def __init__(self, threadId,threadName,counter):
        threading.Thread.__init__(self)
        self.threadId=threadId
        self.threadName=threadName
        self.counter=counter
    def run(self):
        print("starting" + self.threadName)
        #threadLock.acquire()

        print_time(self.threadName,self.counter,5)
        print("exiting" + self.threadName)
        #threadLock.release()

def print_time(threadName,delay,counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print("%s : %s" %(threadName,time.ctime(time.time())))
        counter = counter-1

#threadLock=threading.Lock()
#threads=[]

thread1 = myThread(1,"thread1",1)
thread2 = myThread(2,"thread2",2)

thread1.start()
thread2.start()
thread1.join()
thread2.join()
#threads.append(thread1)
#threads.append(thread2)

or t in threads:
    t.join()

#print("exiting main thread")

