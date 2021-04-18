# Write a program to find fibonacci series

n = int(input("Enter: "))
f1 = 0
f2 = 1
next = 0
if n <= 0:
    print(f1)
else:
    print("Fibonacci series: ", f1, f2, end=" ")
    for i in range(2, n):
        next = f1 + f2
        # if next >= n:
        #     break
        print(next, end=" ")
        f1, f2 = f2,next

