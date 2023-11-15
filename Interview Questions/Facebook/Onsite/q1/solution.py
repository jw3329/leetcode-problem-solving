# // Given a string representing an arithmetic expression with only addition and multiplication operators, return the result of the calculation. For example, for "2*3+4", return 10
# Find the kth largest value in an array: Given an integer array and an integer number k. Return the k-th largest element in the array

# (n - k)th smallest
# quickselect for (n-k)

# arr
# partition of array -> pivot index
# if k is less than pivot index -> left side search
# if k is equal to pivot, then we found -> return
# if k is larger than pivot -> right side search

def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, left, right):
    pivot = arr[right]
    i = left
    for j in range(left, right):
        if arr[j] < pivot:
            # swap with i with left
            swap(arr, i, j)
            i += 1
    # swap i with right
    swap(arr, i, right)
    return i


def find_kth_smallest(arr, k):
    left = 0
    right = len(arr) - 1
    while left <= right:
        # find pivot
        index = partition(arr, left, right)
        if k == index + left: return arr[index]
        if k < index + left: 
            right = index - 1
        else:
            left = index + 1
    return -1


def find_kth_largest(arr, k):
    return find_kth_smallest(arr, len(arr) - k)


# average -> o(n)
# worst case -> o(n^2)


# arr = [1,5,3,4,2] pivot -> 2
#.         i.    right
# arr = [1,5,3,4,2] swap 5,2 to make bottom arr

# arr = [1,2,3,4,5] -> index = 1
#.         1.  3

# left -> 2
# right -> 4

# [3, 4, 5]

# [3, 4]

# left, right

# 2

# k is 3

# pivot is 2

# left is 2

# left + pivot > k

# k = 2 -> 4


#  0 1 2 3
# [1,2,3,4,5]
# left -> 0
# right -> 4



find_kth_largest(arr, k)



# iterate string
# if number is found, then check with current so far number, 10x with so far number + current number
# if it's multiple, then try to find new number, for same process, then multiple, put into stack

# try to make multiplification operation, then put into stack, then add all stack to number

# 2*3+4 sofar -> 0
# [2] stack pop -> 2 * 3 -> 6 then put into stack [6, 4] -> 10

# 2 + 3 + 4 -> 9

# 2 + 3 * 4


def operate_stack_insert(stack, sofar, multi):
    if multi:
        if not stack: raise Exception('stack is empty')
        popped = stack.pop()
        # so far multiple
        stack.append(popped * sofar)
    else:
        stack.append(sofar)

def solve(string):
    sofar = 0
    multi = False
    for c in string:
        if '0' <= c <= '9':
            # update so far value
            sofar = 10 * sofar + int(c)
        elif c == '*':
            # put into stack so far value
            stack.append(sofar)
            sofar = 0
            multi = True
        else:
            # if multi, then we multiply previous value
            # if not multi, then it means it's addition, so we don't need to pop and insert
            operate_stack_insert(stack, sofar, multi)
            sofar = 0
            multi = False
    if sofar:
        operate_stack_insert(stack, sofar, multi)
    return sum(stack)



solve('2*3+4')
