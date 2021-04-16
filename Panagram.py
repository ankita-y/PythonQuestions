str = "The quick brown fox jumps over the lazy dog"
# to remove the space from the string and convert it into lower case
str ="".join([c for c in str if c != " "]).lower()
index = 0

for i in range(len(str)):
    if 'a' <= str[i] <= 'z':
        index += 1

if index >= 26:
    print("The String is a Pangram String.")
else:
    print("The String is not a Pangram String.")