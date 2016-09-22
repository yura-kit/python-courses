# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

balance = 4842
annual_interest_rate = 0.2
monthly_payment_rate = 0.04


def calculate_month_payment(month):
    
    global balance
    
    monthly_interest_rate = annual_interest_rate / 12.0
    minimum_monthly_payment = monthly_payment_rate  * balance
    monthly_unpaid_balance = balance - minimum_monthly_payment
    updated_balance_month = monthly_unpaid_balance + monthly_interest_rate * monthly_unpaid_balance
    balance = updated_balance_month
    
    print('Month: %i' % int(month+1))    
    print('Minimum montly payment: %0.2f' % minimum_monthly_payment)
    print('Remaining balance: %0.2f' % updated_balance_month)
    return minimum_monthly_payment

if __name__ == '__main__':
    
    total_min_paid = 0
    print('-'*15)
    for i in range(0,12):
        total_min_paid = total_min_paid + calculate_month_payment(i)
        print('-'*15)

    print('Total paid: %0.2f' % total_min_paid)
    print('Remaining balane: %0.2f' % balance)
    

# <codecell>


