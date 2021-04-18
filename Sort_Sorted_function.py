# Difference between sort and sorted function
l1 = [10,20,5,3,1,8,89,45,25]
l2 = [10,20,5,3,1,8,89,45,25]
t1 = (10,20,5,3,1,8,89,45,25)
s1 = {10,20,5,3,1,8,89,45,25}
l1.sort()
# Sort works with list only and modifies original list. Return None
print(l1.sort())
print(l1)
# Sorted works with any iterable and return new modified list
print(sorted(l2))
print(l2)
print(sorted(t1))
print(sorted(s1))

print("===========================")
# Sorting using Bubble Sort
for i in range(len(l2)):
    for j in range(len(l2)-1):
        if l2[j] > l2[j+1]:
            l2[j],l2[j+1] = l2[j+1], l2[j]

print(l2)