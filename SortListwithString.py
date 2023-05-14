# Sort the string according to order_arr

name_arr = ["Vidya", "Deepika","Monika","Sachin"]
order_arr = ["M","V","D","S"]
sortarr = []
for i in range(len(name_arr)):
    for j in range(len(name_arr)):
      
        if name_arr[j][0] == order_arr[i]:
            sortarr.append(name_arr[j])
# for arr1 in order_arr:
#     for arr2 in name_arr:
#         if arr1 == arr2[0]:
#             sortarr.append(arr2)            
print(sortarr)
