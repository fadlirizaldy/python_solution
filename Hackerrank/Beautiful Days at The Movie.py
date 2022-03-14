def beautifulDays(i, j, k):
    # Write your code here
    result = 0
    for i in range(i,j+1):
        a = int(str(i)[::-1])
        if abs(i-a) % k == 0:
            result += 1
    return result