# Complexity = log(n)

# Iteration


def bsearch(ar, target):
    low = 0
    high = len(ar)-1

    while low <= high:
        mid = low + (high-low)//2
        if ar[mid] == target:
            return mid
        elif ar[mid] < target:
            low = mid+1
        else:
            high = mid-1
    return -1

# Recursion


def bsearch2(ar, low, high, target):
    if high >= 1:
        mid = low + (high-low)//2
        if ar[mid] == target:
            return mid
        elif ar[mid] > target:
            return bsearch2(ar, low, mid-1, target)
        else:
            return bsearch2(ar, mid+1, high, target)
    else:
        return -1
