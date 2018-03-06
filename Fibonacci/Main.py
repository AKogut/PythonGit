num = int(input("Enter number of fibonacci: "))

def recur_fibonacci(n):
    if n <= 1:
        return n
    else:
        return(recur_fibonacci(n-1) + recur_fibonacci(n-2))

if num <= 0:
    print("Plese enter a positive integer")
else:
    print("Fibonacci sequence:")
    for i in range(num):
        print(recur_fibonacci(i))
