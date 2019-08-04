def max_distance(s1,s2):
    if not s1 or not s2:
        return len(s1) if not s2 else len(s2)
    i = 0
    while s1[i] == s2[i]: i += 1
    return len(s1[i:]) + len(s2[i:])



s1 = '1011000'
s2 = '1011110'

print(max_distance(s1,s2))
