# 2. Dictionary – Word Count

x = "hello world hello".split()
y = {}

for i in x:
    if i in y:
        y[i] += 1
    else:
        y[i] = 1

print(y)