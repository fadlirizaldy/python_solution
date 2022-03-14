def migratoryBirds(arr):
    # Write your code here
    count = [0]*(max(arr)+1)
    for t in arr:
        count[t] += 1
    return count.index(max(count))