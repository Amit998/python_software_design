def get_max(lst):
    max=float("-inf")

    for num in lst:
        if (num > max):
            max=num
    return max


def get_min(lst):
    min=float("inf")

    for num in lst:
        if (num < min):
            min=num
    return min

def get_aveage(lst):
    return sum(lst) / len(lst)

def get_median(lst):
    lst=sorted(lst)

    if(len(lst) %2 ==0):
        return (lst[(len(lst) / 2) -1] + lst([len(lst) /2 ])) /2
    else:
        return lst((len(lst)-1)/2)