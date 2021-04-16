str = {"apple","sample","hello","subject"}
print(type(str))
new_str = set()

for i in str:
    if i[0].lower() == 's':
        new_str.add(i)

print(new_str)