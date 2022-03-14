def countApplesAndOranges(s, t, a, b, apples, oranges):
    print(sum([1 for x in apples if (x+a)<=t and (x+a)>=s]))
    print(sum([1 for x in oranges if (x+b)<=t and (x+b)>=s]))