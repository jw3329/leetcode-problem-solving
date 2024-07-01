class Solution:
    def maxHeightOfTriangle(self, red: int, blue: int) -> int:
        # try with both reversed, return maximum value
        
        def helper(red, blue, is_blue, consume):
            if is_blue:
                if blue < consume: return 0
                return 1 + helper(red, blue - consume, not is_blue, consume + 1)
            if red < consume: return 0
            return 1 + helper(red - consume, blue, not is_blue, consume + 1)
        
        return max(helper(red, blue, True, 1),helper(red, blue, False, 1))
