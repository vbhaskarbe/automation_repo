class Customer(object):
    """A customer of ABC Bank with a checking account. Customers have the
    following properties:

    Attributes:
        name: A string representing the customer's name.
        balance: A float tracking the current balance of the customer's account.
    """

    def __init__(self, name):
        """Return a Customer object whose name is *name*.""" 
        self.name = name

    def set_balance(self, balance=0.0):
        """Set the customer's starting balance."""
        self.balance = balance

    def withdraw(self, amount):
        """Return the balance remaining after withdrawing *amount*
        dollars."""
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance

    def deposit(self, amount):
        """Return the balance remaining after depositing *amount*
        dollars."""
        self.balance += amount
        return self.balance

if __name__ == '__main__':
    cust_b_obj = Customer('Bhaskar')
    cust_b_obj.set_balance()
    print( cust_b_obj.name)
    print( cust_b_obj.balance)
    cust_b_obj.set_balance( 500.0)
    print( cust_b_obj.balance)
    cust_b_obj.deposit(250.0)
    print( cust_b_obj.balance)
    cust_b_obj.withdraw(125.0)
    print( cust_b_obj.balance)



