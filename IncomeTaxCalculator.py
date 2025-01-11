def calculate(amt,per):
    return (amt*per)/100

def calc_income_tax(total):

    if total <=250000:
        return 0
    elif total <= 500000:
        return calculate(total-250000,5)
    elif total <= 750000:
        return calculate(total-500000,10)+12500
    elif total <= 1000000:
        return calculate(total-750000,15)+37500
    elif total <= 1250000:
        return calculate(total-1000000,20)+75000
    elif total <= 1500000:
        return calculate(total-1250000,25)+125000
    else:
        return calculate(total-1500000,30)+187500


total=float(input("Enter Annual Income : "))
tax=calc_income_tax(total)
print("Total Tax : ",tax)
