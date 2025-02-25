import re


PARSER = re.compile(r'^SELECT (.*) FROM [a-z]+(?: WHERE (.*?))?(?: ORDER BY (.*?))?$')

# Example
# print(PARSER.match("SELECT a, d FROM library WHERE b = 1 AND d = 3 ORDER BY c, d").groups())
# This prints: ('a, d', 'b = 1 AND d = 3', 'c, d')

LIBRARY = [
    {
        'title': 'The Ministry for the Future',
        'author': 'Kim Stanley Robinson',
        'year': 2020,
    },
    {
        'title': 'Circe',
        'author': 'Madeline Miller',
        'year': 2018,
    },
    {
        'title': 'Circe2',
        'author': 'Madeline Miller',
        'year': 2018,
    },
    {
        'title': 'TestCicer',
        'author': 'Madeline Miller',
        'year': 2018,
    },
    {
        'title': 'TestCicer2',
        'author': 'Madeline Miller',
        'year': 2018,
    },
    {
        'title': 'Song of Achilles',
        'author': 'Madeline Miller',
        'year': 2012,
    },
    {
        'title': 'Besigning Climate Solutions',
        'author': 'Hal Harvey',
        'year': 2018,
    },
]

def execute(query: str) -> list[dict]:
    # parse sql using parser
    # target, condition, ordering
    # 1. condition, 2. ordering, 3. target
    target, condition, orders = PARSER.match(query).groups()
    print('target', target)
    print('condition', condition)
    print('orders', orders)
    # split by and
    # split by equal
    # filter by condition
    # filter first if condition exists
    filtered = LIBRARY
    if condition:
        and_splitted = list(map(lambda x: x.strip(), condition.split('AND')))
        # now we split by =
        print(and_splitted)
        # do first with geq or leq first
        # if not matching, then next of = < >
        conditions = []
        for cond_str in and_splitted:
            # check for split
            splitted = cond_str.split('<=')
            if len(splitted) > 1:
                conditions.append(list(map(lambda x: x.strip(), splitted)))
                break
            splitted = cond_str.split('>=')
            if len(splitted) > 1:
                conditions.append(list(map(lambda x: x.strip(), splitted)))
                break
            splitted = cond_str.split('=')
            if len(splitted) > 1:
                conditions.append(list(map(lambda x: x.strip(), splitted)))
                break
            splitted = cond_str.split('<')
            if len(splitted) > 1:
                conditions.append(list(map(lambda x: x.strip(), splitted)))
                break
            splitted = cond_str.split('>')
            if len(splitted) > 1:
                conditions.append(list(map(lambda x: x.strip(), splitted)))
                break
        # print(less, greater, leq, geq)
        print(conditions)
        filtered = []
        for obj in LIBRARY:
            # check condition
            condition_passed = True
            for cond in conditions:
                # if equal[1] is integer, then try to make obj to string
                # if equal[1] is string type, having '', then wrap with ''
                # grab value
                # try:
                    
                # except:
                # if 
                if cond[1].isnumeric():    
                    if str(obj[cond[0]]) != cond[1]:
                        condition_passed = False
                        break
                else:
                    if f"'{obj[cond[0]]}'" != cond[1]:
                        condition_passed = False
                        break
                # check string case
                
            # if condition passes, then append to new filtered
            if condition_passed:
                filtered.append(obj)
        # do ordering
    if orders:
        stripped_orders = list(map(lambda x: x.strip(), orders.split(',')))
        # sort one by one
        for param in stripped_orders:
            # sort by this param
            filtered.sort(key=lambda x: x[param])


    # pick up target
    res = []
    # split the target also
    targets = list(map(lambda x: x.strip(), target.split(',')))
    for obj in filtered:
        res_obj = dict()
        for target in targets:
            res_obj[target] = obj[target]
        res.append(res_obj) 
    return res

def main():
    # print(PARSER.match("SELECT a, d FROM library WHERE b = 1 AND d = 3 ORDER BY c, d").groups())

    print("test1", execute("SELECT title FROM library WHERE year = 2012"))
    print("test 2", execute("SELECT title, author, year FROM library WHERE year = 2020"))
    print("test 3", execute("SELECT title, author, year FROM library WHERE year = 2018"))
    print("test 4", execute("SELECT title, author, year FROM library ORDER BY year"))
    print("test 5", execute("SELECT title, author, year FROM library WHERE author = 'Madeline Miller' ORDER BY year"))
    print("test 6", execute("SELECT title, author, year FROM library WHERE author = 2018 ORDER BY year"))
    print("test 7", execute("SELECT title, author, year FROM library WHERE author = 'Madeline Miller' AND year = 2018 ORDER BY year, title"))
    print("test 8", execute("SELECT title, author, year FROM library WHERE author >= 2012 ORDER BY year"))

    # query_1 = "SELECT title FROM library WHERE year = 2012"
    # print(execute(query_1)) -> [{"title": "Song of Achilles"}]

if __name__ == "__main__":
    main()

