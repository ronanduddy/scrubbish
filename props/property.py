from .calc import Calc
from .page import Page
from .postal import Postal

class Property(Page):
    def __init__(self, uri):
        super().__init__(uri)

    def to_h(self):
        result = {}
        result['url'] = self.url()

        price_text = self._element('Price').split(' ')[-1].replace('£', '').replace('$', '').replace('€', '').replace(',', '')
        price = 0 if price_text == 'POA' else int(price_text)
        result['Price'] = price

        rates_text = self._element('Rates').replace('£', '').replace('€', '').replace(',', '').split(' ')[0]
        result['Rates'] = 0.0 if (rates_text == '?' or rates_text == '') else float(rates_text)

        result['Style'] = self._element('Style')
        result['Bedrooms'] = self._element('Bedrooms')
        result['Bathrooms'] = self._element('Bathrooms')
        result['Receptions'] = self._element('Receptions')
        result['Heating'] = self._element('Heating')
        result['EPC Rating'] = self._element('EPC Rating')
        result['Status'] = self._element('Status')

        address = self._clean(self.content().h1.text)
        result['Address'] = address
        postal_info = Postal(address).info()
        result['district'] = postal_info['district']
        result['position'] = postal_info['position']
        result['post_town'] = postal_info['post_town']
        result['coverage'] = postal_info['coverage']

        result['Agent'] = self.content().find_all('p', 'enquiry-org')[0].text.strip('\n')
        result['Agent Phone'] = self.content().find_all('a', attrs = {'data-office-phone': True})[0]['data-office-phone']

        stats_list = self.content().find_all('section', 'stats-time')
        stats = stats_list[0].p.text.strip('\n') if len(stats_list) > 0 else '?'
        result['Total Views'] = stats
        result['Features'] = self.content().find_all('div', 'prop-descr-text')[0].text.replace('\n', ' ')

        result[f'deposit@5.0%'] = price / 100 * 5.0
        result[f'deposit@10.0%'] = price / 100 * 10.0
        result[f'deposit@15.0%'] = price / 100 * 15.0
        result[f'deposit@20.0%'] = price / 100 * 20.0

        for example in self._examples(price, result['Rates']):
            calc = Calc(example)
            result['monthly_rates'] = calc.monthly_rates
            result.update(calc.fxd_95_LTV_2yrs())
            result.update(calc.fxd_75_LTV_2yrs())
            result.update(calc.fxd_75_LTV_3yrs())
            result.update(calc.fxd_75_LTV_5yrs())
            result.update(calc.std_var_rate())
            result.update(calc.trkr_75_LTV())

        return result

    def _examples(self, price, rates):
        return [
            {'price': price, 'rates': rates, 'years': 20, 'deposit_percentage': 5.0},
            {'price': price, 'rates': rates, 'years': 25, 'deposit_percentage': 5.0},
            {'price': price, 'rates': rates, 'years': 30, 'deposit_percentage': 5.0},
            {'price': price, 'rates': rates, 'years': 35, 'deposit_percentage': 5.0},
            {'price': price, 'rates': rates, 'years': 20, 'deposit_percentage': 10.0},
            {'price': price, 'rates': rates, 'years': 25, 'deposit_percentage': 10.0},
            {'price': price, 'rates': rates, 'years': 30, 'deposit_percentage': 10.0},
            {'price': price, 'rates': rates, 'years': 35, 'deposit_percentage': 10.0},
            {'price': price, 'rates': rates, 'years': 20, 'deposit_percentage': 15.0},
            {'price': price, 'rates': rates, 'years': 25, 'deposit_percentage': 15.0},
            {'price': price, 'rates': rates, 'years': 30, 'deposit_percentage': 15.0},
            {'price': price, 'rates': rates, 'years': 35, 'deposit_percentage': 15.0},
            {'price': price, 'rates': rates, 'years': 20, 'deposit_percentage': 20.0},
            {'price': price, 'rates': rates, 'years': 25, 'deposit_percentage': 20.0},
            {'price': price, 'rates': rates, 'years': 30, 'deposit_percentage': 20.0},
            {'price': price, 'rates': rates, 'years': 35, 'deposit_percentage': 20.0},
        ]

    def _element(self, text):
        list = self.content().find_all('th', text=text)

        if len(list) > 0:
            text = self._clean(list[0].find_next().text)

            if text == '':
                return '?'
            else:
                return text
        else:
            return '?'

    def _clean(self, text):
        return ' '.join(text.split())
