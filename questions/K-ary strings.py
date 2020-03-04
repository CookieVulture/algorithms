# Generate all the strings of length n drawn from 0...k-1


def kary(arr, k):
    num = len(arr)
    printkary(arr, k, num, "")


def printkary(arr, k, num, str):
    if k == 0:
        print(str)
        return
    for i in range(num):
        newstr = str + arr[i]
        printkary(arr, k-1, num, newstr)


test1 = ['a', 'b']
k = 2
kary(test1, k)
