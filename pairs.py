def check_pairs(pairs):
    pairs = pairs.upper()
    pairs_list = pairs.split()
    letters = set()
    for pair in pairs_list:
        if len(pair) != 2:
            return False
        if pair[0]==pair[1]:
            return False
        if pair[0] in letters or pair[1] in letters:
            return False
        letters.add(pair[0])
        letters.add(pair[1])
    return True    

def get_pair(symbol, pairs=""):
    if pairs=="":
        return symbol.upper()
    pairs = pairs.upper()
    pairs_list = pairs.split()
    pairs_dict = {}
    for pair in pairs_list:
        pairs_dict[pair[0]]=pair[1]
        pairs_dict[pair[1]]=pair[0]
    if symbol in pairs_dict:
        return pairs_dict[symbol.upper()]
    else:
        return symbol
