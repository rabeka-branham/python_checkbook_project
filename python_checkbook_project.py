import sys

def options():
    print('\nWhat would you like to do?\n')
    print('1) view current balance')
    print('2) record a debit (withdraw)')
    print('3) record a credit (deposit)')
    print('4) exit\n')
    
def balance():
    with open('balance.txt') as f:
        balance = float(f.read())
    print(f'\nYour current balance is ${balance:.2f}.')
    
def debit():
    with open('balance.txt') as f:
         balance = float(f.read())
    debit_amount = float(input('\nHow much is the debit? '))
    balance_with_debit = str(balance + debit_amount)
    with open('balance.txt', 'w') as f:
        f.write(balance_with_debit)

def credit():
    with open('balance.txt') as f:
         balance = float(f.read())
    credit_amount = float(input('\nHow much is the credit? '))
    balance_with_credit = str(balance - credit_amount)
    with open('balance.txt', 'w') as f:
        f.write(balance_with_credit)
        
def exit():
    print('\nThanks, have a great day!')
    
greeting = '~~~ Welcome to your terminal checkbook! ~~~'

print(greeting)
options()

while True:
    choice = input('Your choice? ')
    if choice.isdigit() == True and 0 < int(choice) < 5:
        choice = int(choice)
        if choice == 1:
            balance()
            options()
        elif choice == 2:
            debit()
            options()
        elif choice == 3:
            credit()
            options()
        else:
            exit()
            break
    else:
        print(f'Invalid choice: {choice}\n')