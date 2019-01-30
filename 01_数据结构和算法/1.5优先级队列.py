import heapq

class PriorityQueue(object):
    def __init__(self):
        self._queue = []
        self._index = 0
    
    def push(self, item, priority):
        # 把priority放在元组的第一位 heappop的时候就是按这个的大小比较了
        # 引入index组成三元元组 可以使得优先级相同的元素 同样可以进行比较
        heapq.heappush(self._queue, (-priority, self._index, item))
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]

class Item(object):
    def __init__(self, name):
        self.name = name
    def __repr__(self):
        return 'Item({!r})'.format(self.name)

if __name__ == "__main__":
    q = PriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)

    print(q.pop())
    print(q.pop())
    print(q.pop())
    print(q.pop())
