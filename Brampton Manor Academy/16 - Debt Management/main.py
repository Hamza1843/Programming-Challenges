from math import ceil

def calc_total_repaid(interest, repayment):
    debt = 100
    total = 0
    interest = interest / 100

    while debt != 0:
        debt = debt + ceil(debt*interest*100)/100
        repayment_amount = repayment/100 * debt
        repayment_amount = ceil(repayment_amount * 100.00)/100.00
        if repayment_amount < 50:
            repayment_amount = 50
        if repayment_amount > debt:
            repayment_amount = debt
        debt -= repayment_amount
        total += repayment_amount
    return total

interest = float(input("Input interest: "))
repayment = float(input("Input repayment: "))
print(calc_total_repaid(interest, repayment))
