# Python Program to Check Perfect Number
num = int(input())
div_sum = 0
for i in range(1,num):
    if num%i == 0:
        div_sum += i

if div_sum == num:
    print("Number is perfect number")
else:
    print("Number is not perfect number")
