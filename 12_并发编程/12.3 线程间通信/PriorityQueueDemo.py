import heapq
import threading
import time

class PriorityQueue:
    """一个优先级队列"""
    def __init__(self):
        self._queue = []
        self._count = 0
        self._cv = threading.Condition()
    def put(self, item, priority):
        with self._cv:
            heapq.heappush(self._queue, (priority, self._count, item))
            self._count += 1
            self._cv.notify()
    def get(self):
        with self._cv:
            while len(self._queue) == 0:
                self._cv.wait()
            return heapq.heappop(self._queue)[-1]

def producer(pq):
    for i in range(10):
        time.sleep(0.5)
        pq.put(int(time.time()), i)
        
def comsumer(pq):
    while True:
        print(pq.get())


if __name__ == "__main__":
    pq = PriorityQueue()
    # p.put("我是你爸爸",1)
    # p.put("我是你妈妈",3)
    # p.put("我是你爷爷",-10)

    # print(p.get())
    t1 = threading.Thread(target=producer, args=(pq,))
    t2 = threading.Thread(target=comsumer, args=(pq,))

    t2.start()
    print("等待2秒钟!")
    time.sleep(2)
    t1.start()





