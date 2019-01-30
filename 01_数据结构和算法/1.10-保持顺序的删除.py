

def dedupe(items):
    """这个方法仅仅在序列中元素为 hashable 的时候才管用"""
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)



alist = [1,1,1,2,2,2,3,3,3]

for a in dedupe(alist):
    print(a)


"""
如果你想消除元素不可哈 希 (比如 dict 类型) 的序列中重复元素的话，你需要将上述代码稍微改变一下，就像 这样:
"""

def dedupe(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)


alist = [{'x': 1, 'y': 2}, {'x': 1, 'y': 3},
         {'x': 1, 'y': 2}, {'x': 2, 'y': 4}]
        
# for a in dedupe(alist, key=lambda d: (d["x"], d["y"])):
for a in dedupe(alist, key=lambda d: d["x"]):
    print(a)



