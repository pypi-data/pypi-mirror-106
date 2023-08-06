def emi(amount, tenure, interest, is_year=True, is_percent=True):
    tenure = tenure*12 if is_year else tenure
    interest = interest/100 if is_percent else interest
    interest /= 12
    emi = (amount*interest*(1+interest)**tenure) / ((1+interest)**tenure-1)
    total_payable = emi*tenure
    interest_amount = total_payable - amount
    return {'EMI': emi, 'Total Repayment Amount': total_payable, 'Interest Amount': interest_amount}

def sip(investment, tenure, interest, amount=0, is_year=True, is_percent=True, show_amount_list=False):
    tenure = tenure*12 if is_year else tenure
    interest = interest/100 if is_percent else interest
    interest /= 12
    amount_every_month = {}
    for month in range(tenure):
        amount = (amount + investment)*(1+interest)
        amount_every_month[month+1] = amount
    return {'Amount @ Maturity': amount, 'Amount every month': amount_every_month} if show_amount_list else {'Amount @ Maturity': amount} 
