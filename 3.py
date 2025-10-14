# 3. String – Palindrome Check 

x = 'madam'
n = len(x)
left = 0
right = n-1
flag = 0

while left<right:
    if x[left] != x[right]:
        print("Not Palindrom")
        flag += 1
        break
    left += 1
    right -= 1
if flag == 0:
    print("Palindrom")


# --------------------------------------------------

f'Palindrom' if x == x[::-1] else f'Not Palindrom'