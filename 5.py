# 5. Logical – Find the Largest of Three Numbers

a = int(input("Enter Number : "))
b = int(input("Enter Number : "))
c = int(input("Enter Number : "))

if a>b and a>c:
    print(f'{a} is Max.')
elif b>c and b>a:
    print(f'{b} is Max.')
else:
    print(f'{c} is Max')

