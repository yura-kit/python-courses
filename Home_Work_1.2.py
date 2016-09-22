# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

initial_balance = 4773
annual_interest_rate = 0.2
minimum_fixed_monthly_payment = 10
counter = 0


def calculate_month_payment(balance, month):
    
    global minimum_fixed_monthly_payment  
    monthly_interest_rate = annual_interest_rate / 12.0
    monthly_unpaid_balance = balance - minimum_fixed_monthly_payment
    updated_balance_month = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
    
    return updated_balance_month

if __name__ == '__main__':
    
    print('-'*15)
    balance = initial_balance
    
    while True:
        for i in range(0,12):
            #print(balance)
            balance = calculate_month_payment(balance, i)
        counter += 1
        if balance <= 0:
            break
        balance = initial_balance    
        minimum_fixed_monthly_payment += 10

    #print('Balance: %0.2f' % balance)    
    print('Lowest Payment: %0.2f' % minimum_fixed_monthly_payment)
    #print(count)

# <codecell>


# <codecell>


