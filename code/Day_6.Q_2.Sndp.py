# Complete the bonAppetit function below.
def bonAppetit(bill, k, b):
    bill.pop(k)
    if sum(bill)//2 == b:
        print("Bon Appetit")
    else:
        print(b-sum(bill)//2)