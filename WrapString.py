# You are given a string S and width W.
# Your task is to wrap the string into a paragraph of width .
# Input Format
# The first line contains a string, S.
# The second line contains the width W .

# s = "ABCDEFGHIJKLIMNOQRSTUVWXYZ"
userstr = input()
w = int(input())
y = w
j = 0
for i in range(len(userstr)):
    print(userstr[j:y])
    j += w
    y += w
