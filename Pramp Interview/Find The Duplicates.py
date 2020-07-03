# case 1: M ≈ N
# time: O(N + M)      
# space: O(N + M)     
def find_duplicates1(arr1, arr2):
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


# case 2: M >> N
# time: O(N log M)      
# space: O(N)     
def find_duplicates2(arr1, arr2):
  duplicates = []
  
  for num in arr1:
    if binary_search(arr2, num) != -1:
      duplicates.append(num)
      
  return duplicates

def binary_search(arr, num):
  left = 0
  right = len(arr) - 1
  
  while left <= right:
    mid = left + ((right - left) // 2)
    if arr[mid] == num:
      return mid
    elif arr[mid] < num:
      left = mid + 1
    else:
      right = mid - 1
      
  return -1
