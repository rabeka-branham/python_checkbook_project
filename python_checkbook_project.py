greeting = '\n~~~ Welcome to your terminal checkbook! ~~~'

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
    while True:
        debit_amount = input('\nHow much is the debit? ')
        if debit_amount.isdigit() == True:
            debit_amount = float(debit_amount)
            balance_with_debit = str(balance - debit_amount)
            with open('balance.txt', 'w') as f:
                f.write(balance_with_debit)
            break
        else:
            print('Invalid input!')

def credit():
    with open('balance.txt') as f:
        balance = float(f.read())
    while True:
        credit_amount = input('\nHow much is the credit? ')
        if credit_amount.isdigit() == True:
            credit_amount = float(credit_amount)
            balance_with_credit = str(balance + credit_amount)
            with open('balance.txt', 'w') as f:
                f.write(balance_with_credit)
            break
        else:
            print('Invalid input!')
        
def exit():
    print('\nThanks, have a great day!\n')
      
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