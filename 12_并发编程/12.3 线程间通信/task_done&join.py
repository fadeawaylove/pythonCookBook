
from queue import Queue 
from threading import Thread
# A thread that produces data
def producer(out_q):
    for i in range(10):
        # Produce some data ... 
        out_q.put(i)

# A thread that consumes data
def consumer(in_q): 
    while True:
        # Get some data
        data = in_q.get()
        print(data)
        # Process the data
        # Indicate completion
        in_q.task_done()

# Create the shared queue and launch both threads
q = Queue()
t1 = Thread(target=consumer, args=(q,))
t2 = Thread(target=producer, args=(q,))
t1.start()
t2.start()
# Wait for all produced items to be consumed
q.join()