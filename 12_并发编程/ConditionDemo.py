import threading
import time
class PeriodicTimer:
    def __init__(self, interval):
        self._interval = interval  # 时间间隔
        self._flag = 0  # 触发器标志
        self._cv = threading.Condition()  # condition

    def start(self):
        t = threading.Thread(target=self.run) 
        t.daemon = True
        t.start()

    def run(self): 
        '''
        Run the timer and notify waiting threads after each interval 
        '''
        while True:
            time.sleep(self._interval) 
            with self._cv:
                self._flag ^= 1
                self._cv.notify_all()

    def wait_for_tick(self): 
        '''
        Wait for the next tick of the timer 
        '''
        with self._cv:
            last_flag = self._flag
            print("last_flag:{} self._flag:{}".format(last_flag, self._flag))
            while last_flag == self._flag:
                # 触发器标志没有改变的时候，就会卡在这里等一个notify_all来解锁等待这个Condition的线程
                self._cv.wait()

# Example use of the timer
ptimer = PeriodicTimer(5)
ptimer.start()

# Two threads that synchronize on the timer
def countdown(nticks):
    while nticks > 0:
        ptimer.wait_for_tick()  # 会阻塞在这里，等待这个condition解锁后，继续下一步
        print('T-minus', nticks) 
        nticks -= 1

def countup(last): 
    n=0
    while n < last: 
        ptimer.wait_for_tick() 
        print('Counting', n) 
        n += 1

threading.Thread(target=countdown, args=(10,)).start()
# threading.Thread(target=countup, args=(5,)).start()