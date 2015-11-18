def find_payment(loan, r, m):
    """
    :param loan: float
    :param r: float
    :param m: int
    :return: monthly payment at a rate of r for m months
    """
    return loan * ((r * (1 + r) ** m) / ((1 + r) ** m - 1))


class Mortgage(object):
    """
    Abstract class for building different kinds of mortgages
    """
    def __init__(self, loan, annual_rate, months):
        """
        Create a new mortgage
        """
        self.loan = loan
        self.rate = annual_rate
        self.months = months
        self.paid = [0.0]
        self.owed = [loan]
        self.payment = find_payment(loan, self.rate, months)
        self.legend = None  # description of mortgage

    def make_payment(self):
        """
        Make a payment
        """
        self.paid.append(self.payment)
        reduction = self.payment - self.owed[-1] * self.rate
        self.owed.append(self.owed[-1] - reduction)
