class Solution:
    def pathInZigZagTree(self, label: int) -> List[int]:
        nodes = 1
        level = 1
        while nodes < label:
            level += 1
            nodes = 2**level - 1
        res = []
        while label != 0:
            res.append(label)
            max_val = 2 ** level - 1
            min_val = 2 ** (level - 1)
            label = (max_val + min_val - label) // 2
            level -= 1
        return res[::-1]
