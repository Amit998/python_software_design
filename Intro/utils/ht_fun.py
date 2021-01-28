

def get_keys(ht):
    return ht.keys()


def has_keys(ht,key):
    return key in ht


def get_max(ht):
    max=float("-inf")
    for k,v in ht.items():
        if (v > max):
            max=v
    return max

def get_min(ht):
    min=float("-inf")
    for k,v in ht.items():
        if (v < min):
            min=v
    return min