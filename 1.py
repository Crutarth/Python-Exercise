# 1. List – Filtering Even Numbers

list1 = [1,2,3,4,5,6]
list2 = []

for i in list1:
    if i%2 == 0:
        list2.append(i)

print(list2)


# -------------------------------------------------- 

x = [i for i in list1 if i%2 == 0]; print(x)