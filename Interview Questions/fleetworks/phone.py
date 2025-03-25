def LRUCache(strArr):

  # set up list
  # append each element
  # when appending, check prev
  # if prev found, pop that elem, and append again
  # if element is more than 5, then pop first one
  # after done, join with -

  arr = []
  for c in strArr:
    # check prev
    for i, elem in enumerate(arr):
      if elem == c:
        # pop it
        arr.pop(i)
        break
    arr.append(c)
    if len(arr) > 5:
      arr.pop(0)
  return '-'.join(arr)

# keep this function call here 
print('Sample test passing: ' + str(LRUCache(["A", "B", "C", "D", "A", "E", "D", "Z"]) == 'C-A-E-D-Z'))
print('Sample test passing: ' + str(LRUCache(["A", "B", "A", "C", "A", "B"]) == 'C-A-B'))

# do not remove this line: __internalTestCases__
