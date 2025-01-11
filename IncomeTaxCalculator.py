def calculate(amt,per):
    return (amt*per)/100

def calc_income_tax(total):

    if total <=300000:
        return 0
    elif total <= 700000:
        return calculate(total-300000,5)
    elif total <= 1000000:
        return calculate(total-700000,10)+20000
    elif total <= 1200000:
        return calculate(total-1000000,15)+50000
    elif total <= 1500000:
        return calculate(total-1200000,20)+80000
    else:
        return calculate(total-1500000,30)+140000


total=float(input("Enter Annual Income : "))
tax=calc_income_tax(total)
print("Total Tax : ",tax)
