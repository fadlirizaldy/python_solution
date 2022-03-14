def bonAppetit(n, bill, k, b):
    annaBill = sum(bill[i] for i in range(n) if i != k)//2
    if annaBill == b :
        print('Bon Appetit')
    else:
        print(b-annaBill)