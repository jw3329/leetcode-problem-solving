class Solution:
    def numSquares(self, n: int) -> int:
        
        perfect_squares = []
        count_perfect_squares = [0 for _ in range(n)]
        i = 1
        
        while i* i <= n:
            perfect_squares.append(i*i)
            count_perfect_squares[i*i-1] = 1
            i += 1
        
        if perfect_squares[-1] == n: return 1
        
        queue = [square for square in perfect_squares]
        count = 1
        
        while queue:
            count += 1
            for i in range(len(queue)):
                tmp = queue.pop(0)
                for square in perfect_squares:
                    if tmp + square == n: return count
                    elif tmp + square < n and count_perfect_squares[tmp + square - 1] == 0:
                        count_perfect_squares[tmp + square - 1] = count
                        queue.append(tmp + square)
                    elif tmp + square > n: break
        return 0
