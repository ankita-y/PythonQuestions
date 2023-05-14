#FibonacciSeries
# input: 10
# output: 0 1 1 2 3 5 8 13
n = int(input("Enter n: "))
f1 = 0
f2 = 1
if n <=0:
    print("Fibonacco series: ",f1)
else:
    print("Fibonacco series: ", f1,f2,end=" ")
    for i in range(2,n):
        next = f1+f2
        print(next,end=" ")
        f1=f2
        f2=next
