from collections import defaultdict
"""
你可以很方便的使用 collections 模块中的 defaultdict 来构造这样的字典。 defaultdict 的一个特征是它会自动初始化每个 key 刚开始对应的值，所以你只需要 关注添加元素操作了。
"""

d = defaultdict(list)
d['a'].append(1) 
d['a'].append(2) 
d['b'].append(4)
print(d)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['b'].add(4)
print(e)

d = {} # A regular dictionary 
d.setdefault('a', []).append(1) 
d.setdefault('a', []).append(2) 
d.setdefault('b', []).append(4)
print(d)
