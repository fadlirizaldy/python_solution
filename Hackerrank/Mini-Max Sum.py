def miniMaxSum(arr):
    # Write your code here
    a = sorted(arr)
    b = a[0:4]
    c = a[1:5]
    print(sum(b), sum(c))   