"""
怎样从一个集合中获得最大或者最小的 N 个元素列表?
"""

import heapq

# 基本用法
# 如果你想在一个集合中查找最小或最大的 N 个元素，并且 N 小于集合元素数量， 那么这些函数提供了很好的性能。因为在底层实现里面，首先会先将集合数据进行堆排 序后放入一个列表中
nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

# 复杂数据结构中
portfolio = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35},
    {'name': 'ACME', 'shares': 75, 'price': 115.65}
]

print(heapq.nlargest(3, portfolio, key=lambda a_dic: a_dic["name"]))
print(heapq.nsmallest(3, portfolio, key=lambda a_dic: a_dic["name"]))

# 查找唯一的最大或者最小

heap = list(nums)
heapq.heapify(heap)
print(heap)













