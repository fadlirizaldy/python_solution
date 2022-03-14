def birthday(s, d, m):
    return len([1 for i in range(len(s)) if sum(s[i:i+m])==d])