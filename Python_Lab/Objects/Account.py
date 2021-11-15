class Account(object):
        def __init__(self, holder, number, balance, credit_line=1500):
                self.Holder = holder
                self.Number = number
                self.Balance = balance
                self.CreditLine = credit_line

        def deposit(self, amount):
                self.Balance = amount

        def withdraw(self, amount):
                if (self.Balance - amount < -self.CreditLine):
                        #Coverage insufficient
                        return False
                else:
                        self.Balance -= amount
                        return True

        def balance(self):
                return self.Balance

        def transfer(self, target, amount):
                if (self.Balance - amount < -self.CreditLine):
                        #Coverage insufficient
                        return False
                else:
                        self.Balance -= amount
                        tatget.Balance += amount
                        return True


