def diagonalDifference(arr):
    d1, d2 = 0, 0
    n = len(arr)
    for i in range(n):
        d1+=arr[i][i]
        d2+=arr[i][-i-1]
    return abs(d1-d2)