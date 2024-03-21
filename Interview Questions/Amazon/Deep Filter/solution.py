# import json, sys


# class Solution:

#     def obj_filter(self, obj, cb):
#         if obj == {}:
#             return {}
#         res = {}
#         for key, value in obj.items():
#             if type(value) == dict:
#                 sub_obj = self.obj_filter(value, cb)
#                 if sub_obj != {}:
#                     res[key] = sub_obj
#             elif cb(value):
#                 res[key] = value
#         return res


# def filter_f(n):
#     return type(n) == str


# s = Solution()

# with open(sys.argv[1], "r") as f:
#     obj = json.load(f)
#     print(obj)
#     print(s.obj_filter(obj, filter_f))


# condition of value
# if all filtered, then just remove it all
# if filtered is available, then keep it

# iterate first key
# do recursive for value, with condition
# if value is dictionary type, then check if it's empty
# if empty, then we need to remove
# if it's not dictionary type, then validate if condition is met
# if condition is not met, then just remove
# if condition is met, then keep it

input1 = {"a": 1, "b": {"c": 2, "d": -3, "e": {"f": {"g": -4}}, "h": {"i": 5, "j": 6}}}
input2 = {
    "a": 1,
    "b": {"c": "Hello World", "d": 2, "e": {"f": {"g": -4}}, "h": "Good Night Moon"},
}


def solution(input, func):
    # check if input is dict or not
    if type(input) != dict:
        # then check condition is met, if met, then return, if not met, then return None
        if not func(input):
            return None
        return input
    # now it's dict
    res = input.copy()
    keys = list(res.keys())
    for key in keys:
        val = res[key]
        returned = solution(val, func)
        # check if it's dict or none, if empty dict or none, then pop, if not, then just use returned
        if not returned or returned == dict():
            res.pop(key)
        else:
            res[key] = returned

    return res


print(solution(input1, lambda x: x >= 0))

print(solution(input2, lambda x: type(x) == str))
