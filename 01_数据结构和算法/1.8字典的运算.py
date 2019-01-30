prices = {'ACME': 45.23,
          'AAPL': 612.78, 
          'IBM': 205.55, 
          'HPQ': 37.20, 
          'FB': 10.75
          }


# 利用zip，会先比较值，再比较键
min_price = min(zip(prices.values(), prices.keys()))
print(min_price)
max_price = max(zip(prices.values(), prices.keys()))
print(max_price)

# 利用sorted进行排序
sorted_prices = sorted(zip(prices.values(), prices.keys()))
print(sorted_prices)

# 你可以在 min() 和 max() 函数中提供 key 函数参数来获取最小值或最大值对应的 键的信息
# 这里会发现不管传进去的是prices 还是 prices.keys() 最后结果都是一样的，这是因为实际上字典比较的就是key的值
print(min(prices.keys(), key=lambda k: prices[k]))
print(min(prices, key=lambda k: prices[k]))
print(max(prices, key=lambda k: prices[k]))






