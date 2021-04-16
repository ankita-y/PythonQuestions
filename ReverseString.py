# To reverse the string
s = input()
# print(s[::-1])
str = ''
count = 0
for i in s:
    str = i + str
    count += 1

print(str)
print(count)
