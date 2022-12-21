class Solution:
    def kthLargestValue(self, matrix: List[List[int]], k: int) -> int:
        # for each row, store, so-far value, then append
        # 5 2
        # 1 6
        # 5 7 4 0
        # so_far[j] ^ so_far[j-1]
        so_far = [0] * len(matrix[0])
        prev = 0
        arr = []
        for i in range(len(matrix)):
            prev = so_far[0]
            so_far[0] = so_far[0] ^ matrix[i][0]
            arr.append(so_far[0])
            for j in range(1, len(matrix[0])):
                temp = so_far[j]
                so_far[j] = so_far[j] ^ so_far[j-1] ^ prev ^ matrix[i][j]
                prev = temp
                arr.append(so_far[j])
        arr.sort()
        return arr[len(arr)-k]
