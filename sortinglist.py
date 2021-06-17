import time
def sort_(arr):
    t1 = time.time()
    
    for i in range(len(arr)):
        for j in range(i,len(arr)-1):
            if arr[i] > arr[j+1]:
                arr[i],arr[j+1] = arr[j+1],arr[i]
    t2 = time.time() - t1
    print(arr)
    print(t2)


def sort(a):
    n = 0
    t1 = time.time()
    while n <= len(a):
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i],a[i+1] = a[i+1],a[i]
        n += 1
    t2 = time.time() - t1         
    print(a)
    print(t2)

sort_([5,6,1,2,9,4])
time.sleep(1)
print("*"*20)
sort([5,6,1,2,9,4])  
