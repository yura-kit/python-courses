# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

choises = ('Soup and salad',
           'Pasta with meat sauce',
           'Chef\'s special')


def print_menu():
    i = 1
    for choise in choises:
        print(str(i) + '.',choise)
        i = i+1
    
def read_answer():
    choise = input('Which number would you like to order?')
    return choises[int(choise) - 1]

if __name__ == '__main__':
    
    print_menu()
    
    while True:
        try:
            answer = read_answer()
        except Exception as e:
            print('Sorry, that is not a valid choice.')
        else:
            print('One ' + answer + ' coming right up!')       

# <codecell>


