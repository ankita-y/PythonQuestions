# Given an array of integers , Find the maximum product obtained from multiplying 2 adjacent numbers in the array.
# Notes
#     Array/list size is at least 2.
#     Array/list numbers could be a mixture of positives, negatives also zeroes .

def adjacentElementsProduct(arr):
  #method 1
  l = []
  for i in range(len(arr)-1):
    l.append(arr[i]*arr[i+1])
  return max(l)
  # method 2
  return max(i*j for i,j in zip(arr,arr[1:])
             
print(adjacentElementsProduct([-1, 2, 8,3,0,4,5]))
