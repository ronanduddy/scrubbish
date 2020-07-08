class Calc:
    def __init__(self, args):
        self.price = args['price']
        self.monthly_rates = float('%.2f' % (args['rates'] / 12.0))
        self.years = args['years']
        self.deposit_percentage = args['deposit_percentage']

    def deposit(self):
        return self.price / 100 * self.deposit_percentage

    def fxd_95_LTV_2yrs(self):
        interest_rate = 3.99
        key = self._key_name(f'{interest_rate}% (2yr fxd 95% LTV)')
        value = self._monthly_mortgage(interest_rate)

        return {key: value}

    def fxd_75_LTV_2yrs(self):
        interest_rate = 1.49
        key = self._key_name(f'{interest_rate}% (2yr fxd 75% LTV)')
        value = self._monthly_mortgage(interest_rate)

        return {key: value}

    def fxd_75_LTV_3yrs(self):
        interest_rate = 1.7
        key = self._key_name(f'{interest_rate}% (3yr fxd 75% LTV)')
        value = self._monthly_mortgage(interest_rate)

        return {key: value}

    def fxd_75_LTV_5yrs(self):
        interest_rate = 1.99
        key = self._key_name(f'{interest_rate}% (5yr fxd 75% LTV)')
        value = self._monthly_mortgage(interest_rate)

        return {key: value}

    def std_var_rate(self):
        interest_rate = 4.33
        key = self._key_name(f'{interest_rate}% (Std Var Rate)')
        value = self._monthly_mortgage(interest_rate)

        return {key: value}

    def trkr_75_LTV(self):
        interest_rate = 2.34
        key = self._key_name(f'{interest_rate}% (Trkr 75% LTV)')
        value = self._monthly_mortgage(interest_rate)

        return {key: value}

    def _key_name(self, type):
        template = '{years}yrs {percentage}% {type}'
        name = template.format( years=self.years,
                                percentage=self.deposit_percentage,
                                type=type)

        return name

    def _monthly_mortgage(self, yearly_interest_rate):
        monthy_interest_rate = yearly_interest_rate / 100 / 12
        months = self.years * 12
        factor = monthy_interest_rate / (1 - pow(1 + monthy_interest_rate, -months))
        result = ((self.price - self.deposit()) * factor) - self.monthly_rates

        return float('%.2f' % result)
