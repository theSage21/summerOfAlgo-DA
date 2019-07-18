def boAppetit(bill,k,b):
    value = bill[k]
    paid = (sum(bill) - value) / 2
    if paid ==b:
        return print('Bon Appetit')
    else:
        return print(int(b-paid))
