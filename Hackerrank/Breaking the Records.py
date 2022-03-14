def breakingRecords(scores):
    min1 = max1 = scores[0]
    min_count = max_count = 0
    for i in scores[1:]:
        if i > max1:
            max_count += 1
            max1 = i
        if i < min1:
            min_count += 1
            min1 = i
    return max_count, min_count