import threading

def worker(n, sema):
    sema.acquire()
    print("Working", n)

# 这里传的0表示release最少调用的次数，默认是1，传n，就会默认release n次
sema = threading.Semaphore(0)
nworkers = 10
for n in range(nworkers):
    t = threading.Thread(target = worker, args=(n, sema))
    t.start()


