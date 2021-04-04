import os
from time import sleep
from random import randrange
import multiprocessing as mp
from multiprocessing import Pool

# from multiprocessing import Process, freeze_support
import time
# freeze_support()

totaltargets = 2
totalacc = 5

totaltargets += 1
def dataoff():
    os.system('adb shell sh /storage/EA5D-2D07/dataoff.sh')
    sleep(10)

def dataon():
    os.system('adb shell sh /storage/EA5D-2D07/dataon.sh')
    sleep(20)
    os.system('adb shell ip -4 addr show rmnet0')

def runp(arg):
    print(arg)                                                    
    os.system(arg)  

if __name__ ==  '__main__':
    while 1:
        plus = randrange(0, 4)
        print("the launcher plus is", plus)
        dmin = 5
        dmax = 30
        slp = randrange(90, 110)
        total = 37
        i = 1
        tar = 1
        while i < totalacc:
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print(current_time)

            delay = randrange(dmin, dmax)
            print("delay is ", delay)
            p = Pool(2)
            one = i%totalacc
            two = (i+1)%totalacc
            t1 = tar%(totaltargets)
            t2 = (tar+1)%(totaltargets)
            p.map(runp, [str("python3 run.py 8 12 ../acc/acc"+str(one)+".txt "+str(0)+" ../targets/target"+str(t1)+".txt"), str("python3 run.py 8 12 ../acc/acc"+str(two)+".txt "+str(0)+" ../targets/target"+str(t2)+".txt")])
            # p1 = mp(runp(a[i]))
            # p2 = mp(runp[a[i+1]])
            # p1.start()
            # p2.start()
            # p1.join()
            # p2.join()
            print("Waiting time im seconds : ",slp)
            t = time.localtime()
            current_time = time.strftime("%H:%M:%S", t)
            print(current_time)
            sleep(slp)
            dataoff()
            sleep(30)
            dataon()
            sleep(30)
            i+=2
            tar+=2
            # if i == (total - 1):
            #     i = 0
            #     sleep(delay)
            # else:
            #     i+=4
