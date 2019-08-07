class Solution:
    def totalFruit(self, tree: List[int]) -> int:
        # longest subarray with distinct 2 elements
        ans = i = 0
        count = collections.Counter()
        
        for j, x in enumerate(tree):
            count[x] += 1
            while len(count) >= 3:
                count[tree[i]] -= 1
                if count[tree[i]] == 0:
                    count.pop(tree[i])
                i += 1
            ans = max(ans, j - i + 1)
        return ans
