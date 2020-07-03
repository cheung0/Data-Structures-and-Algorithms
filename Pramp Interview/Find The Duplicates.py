# case 1: M ≈ N
# time: O(N + M)      
# space: O(N + M)     
def find_duplicates(arr1, arr2):
  res = []
  
  i = 0
  j = 0
  while i < len(arr1) and j < len(arr2):
    if arr1[i] == arr2[j]:
      res.append(arr1[i])
      i += 1
      j += 1
    elif arr1[i] < arr2[j]:
      i += 1
    else:
      j += 1
  
  return res
