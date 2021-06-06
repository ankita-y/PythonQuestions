# Python Example : Reverse List Elements
l = [12,8,7,54,36,45] 
# Method 1
print(l[::-1])
# Method 2
lenl=len(l)-1
for i in range(lenl,-1,-1):
    print(l[i])
