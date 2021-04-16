alpha = input().lower()
alpha_str = {}
c = 97
for i in range(1,27):
    alpha_str[chr(c)] = i
    c += 1

wt = 0
str1 = [c for c in alpha]

for i in str1:
    wt += alpha_str[i]

print("Weight of {0} is {1}".format(alpha,wt))