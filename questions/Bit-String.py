# Generate all the strings of n-bits. Assumes A[0..n-1] is an array of size n.


def binary(A, num, start):
    if num == start:
        for i in range(0,num):
            print(A[i], end=" ")
        print()

    else:
        A[start] = 0
        binary(A, num, start+1)
        A[start] = 1
        binary(A, num, start+1)


arr = [None]*3
binary(arr, 3, 0)
