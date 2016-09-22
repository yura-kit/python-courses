# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

initial_balance = 999999
annual_interest_rate = 0.18
monthly_interest_rate = annual_interest_rate / 12.0


#bisection calculate initial lower and high bounds
monthly_lower_bound = initial_balance/12
monthly_upper_bound = (initial_balance * ((1 + monthly_interest_rate)**12))/12

#initial middle value
minimum_fixed_monthly_payment = (monthly_upper_bound + monthly_lower_bound)/2

#precesion
epsilon = 0.001

counter = 0


def calculate_month_payment(balance, month):
    
    global minimum_fixed_monthly_payment
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
        if monthly_upper_bound - monthly_lower_bound < epsilon:
            break
            
        if balance < 0:
            #print('Balance: %0.2f is negative.' % balance )
            monthly_upper_bound = minimum_fixed_monthly_payment
            minimum_fixed_monthly_payment = (monthly_upper_bound + monthly_lower_bound)/2
            #print('L: %0.2f M: %0.2f  H: %0.2f' %  (monthly_lower_bound, minimum_fixed_monthly_payment, monthly_upper_bound))
            
        if balance > 0:
            #print('Balance: %0.2f is positive.' % balance )
            monthly_lower_bound = minimum_fixed_monthly_payment
            minimum_fixed_monthly_payment = (monthly_upper_bound + monthly_lower_bound)/2
            #print('L: %0.2f M: %0.2f  H: %0.2f' %  (monthly_lower_bound, minimum_fixed_monthly_payment, monthly_upper_bound))
        
        balance = initial_balance
  
        
    #print('Balance: %0.2f' % balance)    
    print('Lowest Payment: %0.2f' % minimum_fixed_monthly_payment)
    #print('Balance %0.7f' % balance)
    #print(counter)

# <codecell>


# <codecell>


