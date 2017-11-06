'''
Lab 31 - ATM
'''


# ATM class
class ATM:
    # define transaction list
    transactions = []

    # Set __init__ function and set balance to zero
    def __init__(self):
        self.balance = 0

    # Set check_balance function to return balance of account
    def check_balance(self):
        return self.balance

    # Set deposit function which adds deposit amount to balance and set balance as sum, then returns balance
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append('user deposited $' + str(amount))
        return self.balance

    # Set check withdrawal function which checks if the balance minus the amount to withdraw is greater than zero.
    # If it is, return true, otherwise return false.
    def check_withdrawal(self, amount):
        return amount > self.balance

    # Set withdraw function which first uses check_withdrawal to see if balance will be greater than zero. If true,
    # it subtracts the amount from balance and sets the new sum as balance. Otherwise it returns an error.
    def withdraw(self, amount):
        if self.check_withdrawal(amount) is True:
            self.balance -= amount
            self.transactions.append('user withdrew $' + str(amount))
            return self.balance
        else:
            return "Withdrawal exceeds balance."

    # Set calc_interest function, multiplies balance by .1 and sets result as interest, then returns interest
    def calc_interest(self):
        interest = self.balance * .1
        return interest

    # set transaction function, takes each list item in transactions list, joins at newline and returns as string
    def print_transactions(self):
        return "\n".join(self.transactions)


# set ATM class to money
money = ATM()

# REPL loop
while True:
    u_input = input('Would you like to do (d)eposit, (w)ithdraw, check (b)alance, (h)istory or (exit): ')
    if u_input == 'd':
        amount = int(input('How much would you like to deposit? $'))
        money.deposit(amount)
    elif u_input == 'w':
        amount = int(input('How much would you like to withdraw? $'))
        money.withdraw(amount)
    elif u_input == 'b':
        print('Balance is $' + str(money.check_balance()))
    elif u_input == 'h':
        print(money.print_transactions())
    elif u_input == 'exit':
        break
    else:
        print('Invalid input.')
