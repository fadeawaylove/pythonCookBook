"""
Python 的星号表达式可以用来解决这个问题。比如，你在学习一门课程，在学期 末的时候，你想统计下家庭作业的平均成绩，但是排除掉第一个和最后一个分数。如果 只有四个分数，你可能就直接去简单的手动赋值，但如果有 24 个呢?这时候星号表达 式就派上用场了:
"""

def avg(alist):
    return sum(alist)/len(alist)

def drop_first_last(grades):
    """去掉第一个和最后一个分数"""
    first, *middle, last = grades
    print(middle, type(middle))
    # 此时middle是列表类型
    return avg(middle)


if __name__ == "__main__":
    grades = (1, 2, 3, 4, 5, 6, 7, 1231, 8, 99, 0, 0, 333)
    print(drop_first_last(grades))



