def findlocalmaxima(n, arr):
  maxima = [] 
  # Check the first element
  if arr[0] > arr[1]: 
    maxima.append(0) 
  # Check the elements in the middle
  for i in range(1, n-1):
    if arr[i-1] < arr[i] and arr[i] > arr[i+1]:
      maxima.append(i) 
  # Check the last element
  if arr[-1] > arr[-2]:
    maxima.append(n-1) 
  # Print the results
  if len(maxima) > 0:
    print("Points of local maxima are: ", end="")
    print(*maxima) 
  else: 
    print("There are no points of local maxima")

# Main function
if __name__ =="__main__": 
  n = 9
  arr=[10,10,15,14,13,25,5,4,3] 
  findlocalmaxima(n,arr)
