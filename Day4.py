n = int(input("Enter a positive integer: "))


print("Even number: ",end='')
for num in range(0,n + 1):
    if num % 2 == 0:
        print(num , end=',')

