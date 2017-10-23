'''
Lab 31 - ATM
'''


# ATM class
class ATM:
    # Set __init__ function and set balance to zero
    def __init__(self):
        self.balance = 0

    # Set check_balance function to return balance of account
    def check_balance(self):
        return self.balance

    # Set deposit function which adds deposit amount to balance and set balance as sum, then returns balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance

    # Set check withdrawal function which checks if the balance minus the amount to withdraw is greater than zero.
    # If it is, return true, otherwise return false.
    def check_withdrawal(self, amount):
        if self.balance - amount > 0:
            return True
        else:
            return False

    # Set withdraw function which first uses check_withdrawal to see if balance will be greater than zero. If true,
    # it subtracts the amount from balance and sets the new sum as balance. Otherwise it returns an error.
    def withdraw(self, amount):
        if self.check_withdrawal(amount) is True:
            self.balance -= amount
            return self.balance
        else:
            return "Withdrawal exceeds balance."

    # Set calc_interest function, multiplies balance by .1 and sets result as interest, then returns interest
    def calc_interest(self):
        interest = self.balance * .1
        return interest


# money = ATM()
#
# money.deposit(100)
#
# print(money.calc_interest())
# print(money.check_balance())
