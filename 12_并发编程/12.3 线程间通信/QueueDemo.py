import time

from queue import Queue 
from threading import Thread


_sentinel = object()
# A thread that produces data
def producer(out_q): 
    i = 0
    while True:
        # Produce some data
        data = time.time()
        out_q.put(int(data))
        i += 1
        time.sleep(1)
        if i > 9:
            break
    out_q.put(_sentinel)


# A thread that consumes data
def consumer(in_q): 
    while True:
        # Get some data
        data = in_q.get()
        # Process the data ...
        if data is _sentinel:
            in_q.put(data)
            break
        print("current_time:{}".format(data))
        
# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()