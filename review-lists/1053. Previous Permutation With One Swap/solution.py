class Solution:
    def prevPermOpt1(self, arr: List[int]) -> List[int]:
        index = -1
        for i in range(len(arr)-2,-1,-1):
            if arr[i] > arr[i+1]:
                index = i
                break 
        if index == -1: return arr
        for i in range(len(arr)-1,index,-1):
            if arr[index] > arr[i] and arr[i] != arr[i-1]:
                arr[index], arr[i] = arr[i], arr[index]
                break
        return arr
