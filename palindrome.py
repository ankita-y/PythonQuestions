# To check whether number is palindrome or not
def check_palindrome(x):
    rn = 0
    while x != 0:
        t = x%10
        rn = (rn * 10) + t
        x = x//10

    return rn

n = int(input())
rn = check_palindrome(n)
if n == rn:
    print("No. is palindrome")
else:
    print("No. is not palindrome")
