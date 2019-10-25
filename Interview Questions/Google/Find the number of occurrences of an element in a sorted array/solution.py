def solution(arr,target):
    
    low, high = 0, len(arr) - 1

    # find left most target first
    left, right = 1, 0
    while low <= high:
        mid = low + (high - low) // 2
        if(arr[mid] < target):
            low = mid + 1
        else:
            high = mid - 1
    left = low
    # find right most target

    low, high = 0, len(arr) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if arr[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
    right = high
    print(left,right)
    return right - left + 1









arr = [4, 4, 8, 8, 8, 15, 16, 23, 23, 42] 


target = 8

print(solution(arr,target))

