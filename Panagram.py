# str = "The quick brown fox jumps over the lazy dog"
string = input()
# to remove the space from the string and convert it into lower case
string ="".join([c for c in string if c != " "]).lower()
index = 0

for i in range(len(str)):
    if 'a' <= string[i] <= 'z':
        index += 1

if index >= 26:
    print("The String is a Pangram String.")
else:
    print("The String is not a Pangram String.")
# Method 2
string = string.replace(' ','').lower()
newstr = set()
for i in range(len(string)): newstr.add(string[i])

if len(newstr) == 26:
    print("The string is panagram string")
else:
    print("The string is not panagram string")
