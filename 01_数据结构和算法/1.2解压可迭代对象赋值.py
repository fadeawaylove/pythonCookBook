"""
实现递归算法
"""

def summ(items):
    head, *tails = items
    return head + sum(tails)


if __name__ == "__main__":
    items = [1,2,3,4,5]
    print(summ(items))