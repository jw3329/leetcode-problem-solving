class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        # a = b -> 0 = a ^ b
        # prefix[i] -> arr[0] ^ arr[1] ^ ... ^ arr[i]
        # a ^ b -> arr[i] ^ arr[i+1] ^ ... ^ arr[k] -> prefix[k] ^ prefix[i-1] = 0
        # xor on the side -> prefix[k] = prefix[i-1]
        # 
        # we find i-1, k pair, j will be in between i-1 and k, i ~ k -> k - 1 - i + 1 -> we add k - i
        arr.insert(0, 0)
        for i in range(1, len(arr)):
            arr[i] ^= arr[i-1]
        res = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if arr[j] == arr[i]:
                    res += j - i - 1
        return res
