
# ctc_trades.dat
# timestamp,symbol,quantity,price,execution_id,theoretical_value,account
# 1664976762,TSLA,-700,241.56,18539,241.54671385427642,CCCC


# TRADE_DATE|TRADE_TIME|SYMBOL          |SIDE            |QUANTITY        |PRICE           |EXECUTION_ID    |COUNTERPARTY
# 2022-10-05|09:44:11  |F               |BUY             |             800|        12.32000|           73817|        6000

# generate id map of ctc_trades

# generate id map of exch_trades

# if matches -> compare values, what the difference

# if not match -> one side exists, one side doesn't -> we just print out the row

def parse_ctc(line):
    timestamp,symbol,quantity,price,execution_id,theoretical_value,account = line.split(',')
    return dict(
        timestamp=timestamp,symbol=symbol,quantity=quantity,price=price,execution_id=execution_id,theoretical_value=theoretical_value,account=account
    )


def parse_exch(line):
    TRADE_DATE,TRADE_TIME,SYMBOL          ,SIDE            ,QUANTITY        ,PRICE           ,EXECUTION_ID    ,COUNTERPARTY = line.split('|')
    TRADE_DATE = TRADE_DATE.strip()
    TRADE_TIME = TRADE_TIME.strip()
    SYMBOL = SYMBOL.strip()
    SIDE = SIDE.strip()
    QUANTITY = QUANTITY.strip()
    PRICE = PRICE.strip()
    EXECUTION_ID = EXECUTION_ID.strip()
    COUNTERPARTY = COUNTERPARTY.strip()
    return dict(
        TRADE_DATE=TRADE_DATE,
        TRADE_TIME=TRADE_TIME,
        SYMBOL=SYMBOL,
        SIDE=SIDE,
        QUANTITY=QUANTITY,
        PRICE=PRICE,
        EXECUTION_ID=EXECUTION_ID,
        COUNTERPARTY=COUNTERPARTY,
    )

# quantity price symbol SIDE

def find_diff(ex_id):
    # check the value in ctc_id_map
    ctc_obj = ctc_id_map[ex_id]
    exch_obj = exch_id_map[ex_id]
    # only returning mismatches
    res = []
    # compare quantity first
    quantity = int(ctc_obj['quantity'])
    # if quantity is buy, then positive, sell negative
    if quantity > 0:
        # check exch_obj side
        if exch_obj['SIDE'] == 'SELL':
            res.append('side')
    if quantity < 0:
        # check exch_obj side
        if exch_obj['SIDE'] == 'BUY':
            res.append('side')
    if abs(quantity) != int(exch_obj['QUANTITY']):
        res.append('quantity')
    if ctc_obj['symbol'] != exch_obj['SYMBOL']:
        res.append('symbol')
    if float(ctc_obj['price']) != float(exch_obj['PRICE']):
        res.append('price')
    return res
    




ctc_id_map = dict()

# open file and read line
with open('/home/coderpad/data/ctc_trades.dat', 'r') as f:
    # read line
    # skipping first
    line = f.readline()
    while True:
        line = f.readline()
        if not line: break
        # parse line, then insert all information
        parsed_dict = parse_ctc(line)
        if parsed_dict['execution_id'] in ctc_id_map:
            print(parsed_dict['execution_id'], 'already exists in ctc')
        ctc_id_map[parsed_dict['execution_id']] = parsed_dict
    

exch_id_map = dict()

# open file and read line
with open('/home/coderpad/data/exch_trades.dat', 'r') as f:
    # read line
    # skipping first
    line = f.readline()
    while True:
        line = f.readline()
        if not line: break
        # parse line, then insert all information
        parsed_dict = parse_exch(line)
        if parsed_dict['EXECUTION_ID'] in exch_id_map:
            print(exch_id_map['EXECUTION_ID'], 'already exists in exchange')
        exch_id_map[parsed_dict['EXECUTION_ID']] = parsed_dict

# make comparion for id euqality first

# first iterate with ctc_id_map

for ex_id in ctc_id_map:
    # check if available in exch_id_map
    if ex_id not in exch_id_map:
        # print out
        print(ex_id, 'not existing in exchange')
        continue
    # exists
    attr_diffs = find_diff(ex_id)
    if not attr_diffs:
        # we don't find any diff
        # print(ex_id, 'is identical')
        pass
    else:
        print(ex_id, 'is not identical,',attr_diffs)
    # we remove from exch_id_map
    exch_id_map.pop(ex_id)

# then only print exch_id_map that it exists in its dict

for ex_id in exch_id_map:
    print(ex_id, 'not existing in ctc')

