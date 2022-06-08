class Solution:
    def medianSlidingWindow(self, nums: List[int], k: int) -> List[float]:
        # iterate array, put new element into heap, and index out of window, pop
        # small heap, large heap, assume large heap >= small heap
        small = []
        large = []
        res = []
        
        def push(num, i):
            heapq.heappush(large, (num, i))
            init_popped = heapq.heappop(large)
            heapq.heappush(small, (-init_popped[0], init_popped[1]))
            if len(small) > len(large):
                popped = heapq.heappop(small)
                heapq.heappush(large, (-popped[0], popped[1]))
        
        def median():
            if k % 2 == 0:
                return (large[0][0] - small[0][0]) / 2
            return large[0][0]
        
        def remove(i):
            # if we try to remove num, we need to check if num is in bigger or smaller
            for j in range(len(small)):
                if small[j][1] == i:
                    small[j] = small[-1]
                    small.pop()
                    heapq.heapify(small)
                    return
            for j in range(len(large)):
                if large[j][1] == i:
                    large[j] = large[-1]
                    large.pop()
                    heapq.heapify(large)
                    return
        
        for i, num in enumerate(nums):
            if i - k >= 0:
                remove(i-k)
            push(num, i)
            if i - k + 1 >= 0:
                res.append(median())
        return res
