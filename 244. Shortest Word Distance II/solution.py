import sys


words = ["practice", "makes", "perfect", "coding", "makes"]


def solve(word1, word2):
    # find index of each word, and store it into dict
    # then iterate those 2 lists, then find minimum of it
    word_indices = dict()
    for i, word in enumerate(words):
        if word not in word_indices:
            word_indices[word] = []
        word_indices[word].append(i)
    # check two words
    index_1 = word_indices[word1]
    index_2 = word_indices[word2]
    res = sys.maxsize
    for i1 in index_1:
        for i2 in index_2:
            res = min(res, abs(i1 - i2))
    return res


print(solve("coding", "practice"))

print(solve("makes", "coding"))
