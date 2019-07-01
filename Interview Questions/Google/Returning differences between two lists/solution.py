from collections import Counter

class Solution:
    def differences(self,l1,l2):
        l1_map = Counter(l1)
        l2_map = Counter(l2)

        l1_calculated = {}
        l2_calculated = {}

        for l1_key in l1_map.keys():
            l1_calculated[l1_key] = l1_map[l1_key] - (l2_map[l1_key] if l1_key in l2_map else 0)
            

        for l2_key in l2_map.keys():
            if l2_key not in l1_map:
                continue
            l2_calculated[l2_key] = l2_map[l2_key] - (l1_map[l2_key] if l2_key in l1_map else 0)

        l1_res, l2_res = [],[]
        
        for key,val in l1_calculated.items():
            if val > 0:
                for i in range(val):
                    l1_res.append(key)

        for key,val in l2_calculated.items():
            if val > 0:
                for i in range(val):
                    l2_res.append(key)

        print(l1_calculated,l2_calculated)
        return l1_res, l2_res




s = Solution()

l1 = [1,2,2,4]

l2 = [1,2]

print(s.differences(l1,l2))