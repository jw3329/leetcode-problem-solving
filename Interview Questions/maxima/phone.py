'''
Implement dataframe operations
# Min, Sum, Max, Avg, Count

df = [
   {"product": "burger", "country": "US", "cost": 15,  "quantity": 2},
   {"product": "pizza",  "country": "CA", "cost": 11,  "quantity": 4},
   {"product": "cat",    "country": "CA", "cost": 300, "quantity": 1},
   {"product": "cat",    "country": "CA", "cost": 400, "quantity": 30},
   {"product": "pizza",  "country": "US", "cost": 13,  "quantity": 12},
   {"product": "pizza",  "country": "US", "cost": 5,   "quantity": 3},
]


query_1 = {
   "group_by": ["product"],
   "aggregate": [
       {"operator": "sum", "column": "quantity"}
   ]
}


# Result:
# [
#    {"product": "burger",  "quantity": 2},
#    {"product": "pizza",   "quantity": 19},
#    {"product": "cat",     "quantity": 31},
# ]




query_2 = {
   "group_by": ["product", "country"],
   "aggregate": [
       {"operator": "max", "column": "cost"},
       {"operator": "min", "column": "quantity"}
   ]
}


# Result:
# [
#    {"product": "burger", "country": "US", "cost": 15,  "quantity": 2},
#    {"product": "pizza",  "country": "CA", "cost": 11,  "quantity": 4},
#    {"product": "pizza",  "country": "US", "cost": 13,  "quantity": 3},
#    {"product": "cat",    "country": "CA", "cost": 400, "quantity": 1},
# ]
'''

# group by, agg separate
# group by showing up result
# aggr -> condition of calculation
# for each list, we should also output



df = [
   {"product": "burger", "country": "US", "cost": 15,  "quantity": 2},
   {"product": "pizza",  "country": "CA", "cost": 11,  "quantity": 4},
   {"product": "cat",    "country": "CA", "cost": 300, "quantity": 1},
   {"product": "cat",    "country": "CA", "cost": 400, "quantity": 30},
   {"product": "pizza",  "country": "US", "cost": 13,  "quantity": 12},
   {"product": "pizza",  "country": "US", "cost": 5,   "quantity": 3},
]


query_1 = {
   "group_by": ["product"],
   "aggregate": [
       {"operator": "sum", "column": "quantity"}
   ]
}

import sys

def calculate(rows, operator, column):
    # we can have 4 diff operator
    # Min, Sum, Max, Avg, Count
    res = None
    if operator == "min":
        res = sys.maxsize
        for row in rows:
            res = min(res, row[column])
    if operator == "sum":
        res = 0
        for row in rows:
            res += row[column]
    if operator == "max":
        res = -sys.maxsize
        for row in rows:
            res = max(res, row[column])
    if operator == "avg":
        if len(rows) == 0: raise Exception("count is 0")
        res = 0
        for row in rows:
            res += row[column]
        res /= len(rows)
    if operator == "count":
        res = len(rows)
    return res
        
            


def query(df, query_condition):
    # we should make sure group by hits
    # this hit should be distinct
    # for all those hits
    # we are doing additional aggregation

    # gather hits
    group_by = query_condition['group_by']
    aggregate = query_condition['aggregate']
    group_key_rows = dict()
    for row in df:
        group_list = []
        for elem in group_by:
            group_list.append(row[elem])
        # try to combine this to string based
        group_key = '#'.join(group_list)
        # basd on this group key, insert the rows
        if group_key not in group_key_rows:
            group_key_rows[group_key] = []
        group_key_rows[group_key].append(row)
    
    # group_key_rows : group_key -> []
    # burger#US -> [row]
    res = []
    for group_key in group_key_rows:
        # operate aggregate
        local_dict = dict()
        # this will store
        # column as key, and result for the operator
        for aggr in aggregate:
            calculated = calculate(group_key_rows[group_key], aggr["operator"], aggr['column'])
            local_dict[aggr['column']] = calculated
            # aggr will contain format of {"operator": "max", "column": "cost"},
        # calculated
        # now we split group key
        splitted = group_key.split('#')
        # iterate group by, and map now
        res_dict = dict()
        for i, elem in enumerate(group_by):
            res_dict[elem] = splitted[i]
        # insert rest
        for key in local_dict:
            res_dict[key] = local_dict[key]
        res.append(res_dict)
    return res


    # for hits, do aggregation

query_2 = {
   "group_by": ["product", "country"],
   "aggregate": [
       {"operator": "max", "column": "cost"},
       {"operator": "min", "column": "quantity"}
   ]
}

# print(query(df, query_1))
print(query(df, query_2))


# Users -> id, name
# Credentials -> user_id, credential, status
