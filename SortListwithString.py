name_arr = ["Vidya", "Deepika","Monika","Sachin"]
order_arr = ["M","V","D","S"]
sortarr = []
for i in range(len(name_arr)):
    for j in range(len(name_arr)):
      
        if name_arr[j][0] == order_arr[i]:
            sortarr.append(name_arr[j])
            
print(sortarr)
