class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        if len(heights) == 0: return 0
        first_left_small_index_from_cur = [0 for _ in range(len(heights))]
        first_right_small_index_from_cur = [0 for _ in range(len(heights))]
        
        first_left_small_index_from_cur[0] = -1
        first_right_small_index_from_cur[-1] = len(heights)
        
        for i in range(1,len(heights)):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = first_left_small_index_from_cur[p]
            first_left_small_index_from_cur[i] = p
            
        for i in range(len(heights)-2,-1,-1):
            p = i + 1
            while p < len(heights) and heights[p] >= heights[i]:
                p = first_right_small_index_from_cur[p]
            first_right_small_index_from_cur[i] = p
            
        max_val = 0
        for i in range(len(heights)):
            max_val = max(max_val,heights[i]*
                          (first_right_small_index_from_cur[i] - first_left_small_index_from_cur[i] - 1))
        
        return max_val
