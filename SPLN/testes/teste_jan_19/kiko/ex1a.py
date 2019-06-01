

array = [1,1,3,5,2]

def max_diff(array):
  if len(array)<2:
    return None
  if (array[0]>array[1]):
    min=array[1]
    max=array[0]
  else:
    min=array[0]
    max=array[1]

  for n in array:
    if n<min:
      min=n
    if n>max:
      max=n
  return max-min

# print(max_diff(array))
max_diff(array)