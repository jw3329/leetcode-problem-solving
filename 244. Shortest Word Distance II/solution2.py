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
    i = j = 0
    while i < len(index_1) and j < len(index_2):
        res = min(res, abs(index_1[i] - index_2[j]))
        if index_1[i] < index_2[j]:
            i += 1
        else:
            j += 1
    return res


print(solve("coding", "practice"))

print(solve("makes", "coding"))
