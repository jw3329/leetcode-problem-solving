import random

from pprint import pprint


def rotate_over_diagonals(m, k):
    def rotate_right(level):
        if len(m) // 2 == level: return
        i = level
        for j in range(i + 1, len(m) - 1 - i):
            temp = m[i][j]
            m[i][j] = m[len(m) - 1 - j][i]
            m[len(m) - 1 - j][i] = m[len(m) - 1 - i][len(m) - 1 - j]
            m[len(m) - 1 - i][len(m) - 1 - j] = m[j][len(m) - 1 - i]
            m[j][len(m) - 1 - i] = temp
        rotate_right(level + 1)

    for _ in range(k):
        rotate_right(0)


def create_matrix(num):
    num_set = set()
    matrix = [[0 for _ in range(num)] for _ in range(num)]
    for i in range(num):
        for j in range(num):
            random_num = 0
            while True:
                random_num = random.randint(1, num * num)
                if random_num not in num_set:
                    num_set.add(random_num)
                    break
            matrix[i][j] = random_num
    return matrix


m = create_matrix(5)
k = 2

pprint(m)

print('After change')

rotate_over_diagonals(m, k)

pprint(m)