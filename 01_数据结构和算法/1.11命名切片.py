items = [0, 1, 2, 3, 4, 5, 6]

a = slice(2,4)

print(items[a])

s = 'HelloWorld'
print(a.indices(len(s)))

for i in range(*a.indices(len(s))):
    print(s[i])

