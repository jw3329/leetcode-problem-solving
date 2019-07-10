import json,sys

class Solution:


    def obj_filter(self,obj, cb):
        if obj == {}:
            return {}
        res = {}
        for key,value in obj.items():
            if type(value) == dict:
                sub_obj = self.obj_filter(value,cb)
                if sub_obj != {}:
                    res[key] = sub_obj
            elif cb(value):
                res[key] = value
        return res


def filter_f(n):
    return type(n) == str

s = Solution()

with open(sys.argv[1], 'r') as f:
    obj = json.load(f)
    print(obj)
    print(s.obj_filter(obj,filter_f))
