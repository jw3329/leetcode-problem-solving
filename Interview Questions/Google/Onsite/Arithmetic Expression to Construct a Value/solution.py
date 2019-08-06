
def construct(nums,target):
    operator = ['+','-','*','/','()']
    map = {}
    for i in range(len(nums)):
        value = helper(nums[:i] + nums[i+1:], target, operator, str(nums[i]), map)
        if value:
            return value
    return ''

def helper(nums,target,operator,curr, map):
    if curr in map: return map[curr]
    if target == eval(curr): return curr
    if not nums or not operator: return ''
    for i in range(len(operator)):
        if operator[i] == '()':
            return helper(nums,target,operator[:i] + operator[i+1:],'(' + curr + ')', map)
        else:
            for j in range(len(nums)):
                if operator[i] == '-' and nums[j] < 0:
                    if '()' in operator:
                        operator_copy = operator.copy()
                        operator_copy.remove('()')
                        value = helper(nums[:j] + nums[j+1:], target, operator[:i] + operator[i+1:], curr + operator[i] + '(' + str(nums[j]) + ')', map)
                    else:
                        continue
                else:   
                    value = helper(nums[:j] + nums[j+1:], target, operator[:i] + operator[i+1:], curr + operator[i] + str(nums[j]), map)
                if value: 
                    map[curr + operator[i] + str(nums[j])] = value
                    return value
    map[curr] = ''
    return ''
    




nums = [2,-2]

target = 4

print(construct(nums,target))
