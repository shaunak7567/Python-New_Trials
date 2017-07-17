import thread
import time
def print_time(threadName,Delay):
    count=0
    while count<5:
        time.sleep(5)
        count+=1
        print ("%s: %s" %(threadName,time.ctime(time.time())))
        
        
try:
    thread.start_new_thread(print_time, ("Thread-1",1))
    

except:
    print("Unable to start thread thread for some reason ")
    
while 1:
    pass