class Solution:
    def largestTimeFromDigits(self, arr: List[int]) -> str:
        # get all possibilities of arr first,
        # each compare, if it's formable
        # if it's valid, compare if curr hour and curr min on it
        # if curr hour and min is not set, return empty
        
        def get_all_combs(arr):
            if len(arr) == 1: return [str(arr[0])]
            rests = get_all_combs(arr[1:])
            res = []
            for rest in rests:
                for i in range(len(rest)+1):
                    new_str = rest[:i] + str(arr[0]) + rest[i:]
                    res.append(new_str)
            return res
        
        all_combs = get_all_combs(arr)
        curr_hour = -1
        curr_min = -1
        for comb in all_combs:
            hh = int(comb[:2])
            mm = int(comb[2:])
            if hh < 24 and mm < 60:
                # it's valid
                if curr_hour == -1 and curr_min == -1:
                    curr_hour = hh
                    curr_min = mm
                else:
                    if hh > curr_hour:
                        curr_hour = hh
                        curr_min = mm
                    elif hh == curr_hour:
                        if mm > curr_min:
                            curr_min = mm
        if curr_hour == -1 and curr_min == -1: return ""
        s_hh = str(curr_hour)
        s_mm = str(curr_min)
        if len(s_hh) == 1:
            s_hh = '0' + s_hh
        if len(s_mm) == 1:
            s_mm = '0' + s_mm
        return s_hh + ':' + s_mm
