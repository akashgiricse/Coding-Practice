class CreditCard:

    """A consumer credit card"""

    def __init__(self, customer, bank, acnt, limit):
        """
        Create a new credit card instance
        :param customer: the name of the customer
        :param bank: name of the bank of the customer
        :param account: account number of the customer
        :param limit: credit limit (in rupees)
        """
        self._customer = customer
        self._bank = bank
        self._account = acnt
        self._limit = limit
        self._balance = 0

    def get_customer(self):
        """Return name of the customer"""
        return self._customer

    def get_bank(self):
        """Return name of the bank"""
        return self._bank

    def get_account(self):
        """Return account number"""
        return self._account

    def get_limit(self):
        """Return credit limit"""
        return self._limit

    def get_balance(self):
        """Return current balance"""
        return self._balance

    def charge(self, price):
        """ Charge given price to the card, assuming sufficient credit limit
            Return True if charge was processed, False if denied
        """
        if price + self._balance > self._limit:
            return False
        else:
            self._balance += price
            return True

    def make_payment(self, ammount):
        """Process customer payment that reduces balance"""
        self._balance -= ammount


class PredatoryCreditCard(CreditCard):
    """An extension to CreditCard that compounds interest and fees"""

    def __init__(self, customer, bank, acnt, limit, apr):
        """Create a new predatory credit card instance
            apr: annual percentage rate (e.g. 0.0825 for 8.25% APR)
        """

        super().__init__(customer, bank, acnt, limit)       # call super constructor
        self._apr = apr

        def charge(self, price):

            success = super().charge(self, price)

            if not success:
                self._balance += 5
            return success

        def process_month(self):
            """Access monthly interest on outstanding balance"""
            if self._balance > 0:
                # if positive balance, covert APR to monthly multiplicative factor
                monthly_factor = pow(1 + self._apr, 1/12)
                self._balance *= monthly_factor


if __name__ == "__main__":
    wallet = []
    wallet.append(CreditCard('Akash Giri', 'Punjab National Bank',
                             '2565 2584 2548 5896', 10000))
    wallet.append(CreditCard('Vishal Giri', 'Central Bank',
                             '2565 2564 2548 5896', 15000))
    wallet.append(CreditCard('Panjak Giri', 'ICICI Bank',
                             '2565 2584 9658 5896', 7000))

    for val in range(1, 17):
        wallet[0].charge(val)
        wallet[1].charge(2*val)
        wallet[2].charge(3*val)

    for c in range(3):
        print('Customer = ', wallet[c].get_customer())
        print('Bank = ', wallet[c].get_bank())
        print('Account = ', wallet[c].get_account())
        print('Limit = ', wallet[c].get_limit())
        print('Balance = ', wallet[c].get_balance())
        while wallet[c].get_balance()> 100:
            wallet[c].make_payment(100)
            print('New balance = ', wallet[c].get_balance())
        print("***********")


