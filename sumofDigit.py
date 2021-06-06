# Python Program to Find Sum of Digit
num = int(input())
sum = 0
while num:
    sum += num%10
    num //= 10
print("Sum:", sum)
