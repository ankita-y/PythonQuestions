def calc(Npow):
    temp = Npow
    sum = 0

    while temp > 0:
        rem = temp % 10
        sum += rem
        temp = temp // 10

    if sum > 9:
        return calc(sum)
    else:
        return sum

N = int(input("Enter Number: "))
M = pow(2, N)
result = calc(M)
print(result)