from typing import List


def find_missing_ranges(nums: List[int], lower: int, upper: int) -> List[str]:
    # write your code here
    # we first create new list, which is only in boundary
    # then we iterate to find diff
    new_list = [lower - 1]
    for num in nums:
        if num < lower:
            continue
        if num > upper:
            break
        new_list.append(num)
    # append end
    new_list.append(upper + 1)
    # now we put the range
    res = []
    for i in range(1, len(new_list)):
        # check numbers bewteen
        diff = new_list[i] - new_list[i - 1] - 1
        # check if one, then append num,
        # if more than two, then we make ->
        if diff == 1:
            res.append(str(new_list[i] - 1))
        if diff > 1:
            res.append(f"{new_list[i-1]+1}->{new_list[i]-1}")
    return res


print(find_missing_ranges([0, 1, 3, 50, 75], 0, 99))
print(find_missing_ranges([0, 1, 2, 3, 7], 0, 7))
