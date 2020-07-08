import unittest
from unittest.mock import Mock
from scrubbish.property import Property


class TestProperty(unittest.TestCase):
    def setUp(self):
        self.property = Property("/here")
        self.property.domain = "example.com"

    def stub_request(self, content):
        attributes = {"get.return_value": Mock(content=content)}
        self.property.request = Mock(**attributes)

    def test_to_h(self):
        content = """
                    <h1>25 Greatplace Park,
                        <span>Greatplace, Town, County
                        <span>BTcc 123</span></span>
                    </h1>
                    <table><tbody>
                        <tr><th>Price</th><td>Offers around £149,950</td></tr>
                        <tr><th>Rates</th><td>£869.11 pa*</td></tr>
                        <tr><th>Style</th><td>Semi-detached House </td></tr>
                        <tr><th>Bedrooms</th><td>1</td></tr>
                        <tr><th>Bathrooms</th><td>5</td></tr>
                        <tr><th>Receptions</th><td>2</td></tr>
                        <tr><th>Heating</th><td>good</td></tr>
                        <tr><th>EPC Rating</th><td>also good</td></tr>
                        <tr><th>Status</th><td>sale</td></tr>
                    </tbody></table>
                    <p class="enquiry-org">
                        <span>Property Sales </span><span>(Placehere)</span>
                    </p>
                    <a href="#" data-office-phone="1234567899">
                        <span>01234567899</span></span>
                    </a>
                    <div class="prop-descr-text">great features here</div>
                    <section class="stats-time"><p>1230</p></section>
                    """
        self.stub_request(content)

        expected = {
            "url": "example.com/here",
            "Price": 149950,
            "Rates": 869.11,
            "Style": "Semi-detached House",
            "Bedrooms": "1",
            "Bathrooms": "5",
            "Receptions": "2",
            "Heating": "good",
            "EPC Rating": "also good",
            "Status": "sale",
            "Address": "25 Greatplace Park, Greatplace, Town, County BTcc 123",
            "district": "btcc",
            "position": "?",
            "post_town": "?",
            "coverage": "?",
            "Agent": "Property Sales (Placehere)",
            "Agent Phone": "1234567899",
            "Total Views": "1230",
            "Features": "great features here",
            "deposit@5.0%": 7497.5,
            "deposit@10.0%": 14995.0,
            "deposit@15.0%": 22492.5,
            "deposit@20.0%": 29990.0,
            "monthly_rates": 72.43,
            "20yrs 5.0% 3.99% (2yr fxd 95% LTV)": 790.05,
            "20yrs 5.0% 1.49% (2yr fxd 75% LTV)": 614.31,
            "20yrs 5.0% 1.7% (3yr fxd 75% LTV)": 628.15,
            "20yrs 5.0% 1.99% (5yr fxd 75% LTV)": 647.54,
            "20yrs 5.0% 4.33% (Std Var Rate)": 815.78,
            "20yrs 5.0% 2.34% (Trkr 75% LTV)": 671.38,
            "25yrs 5.0% 3.99% (2yr fxd 95% LTV)": 678.7,
            "25yrs 5.0% 1.49% (2yr fxd 75% LTV)": 496.62,
            "25yrs 5.0% 1.7% (3yr fxd 75% LTV)": 510.77,
            "25yrs 5.0% 1.99% (5yr fxd 75% LTV)": 530.67,
            "25yrs 5.0% 4.33% (Std Var Rate)": 705.68,
            "25yrs 5.0% 2.34% (Trkr 75% LTV)": 555.22,
            "30yrs 5.0% 3.99% (2yr fxd 95% LTV)": 606.84,
            "30yrs 5.0% 1.49% (2yr fxd 75% LTV)": 418.52,
            "30yrs 5.0% 1.7% (3yr fxd 75% LTV)": 432.99,
            "30yrs 5.0% 1.99% (5yr fxd 75% LTV)": 453.39,
            "30yrs 5.0% 4.33% (Std Var Rate)": 635.04,
            "30yrs 5.0% 2.34% (Trkr 75% LTV)": 478.65,
            "35yrs 5.0% 3.99% (2yr fxd 95% LTV)": 557.46,
            "35yrs 5.0% 1.49% (2yr fxd 75% LTV)": 363.04,
            "35yrs 5.0% 1.7% (3yr fxd 75% LTV)": 377.83,
            "35yrs 5.0% 1.99% (5yr fxd 75% LTV)": 398.73,
            "35yrs 5.0% 4.33% (Std Var Rate)": 586.82,
            "35yrs 5.0% 2.34% (Trkr 75% LTV)": 424.7,
            "20yrs 10.0% 3.99% (2yr fxd 95% LTV)": 744.66,
            "20yrs 10.0% 1.49% (2yr fxd 75% LTV)": 578.17,
            "20yrs 10.0% 1.7% (3yr fxd 75% LTV)": 591.28,
            "20yrs 10.0% 1.99% (5yr fxd 75% LTV)": 609.65,
            "20yrs 10.0% 4.33% (Std Var Rate)": 769.03,
            "20yrs 10.0% 2.34% (Trkr 75% LTV)": 632.23,
            "25yrs 10.0% 3.99% (2yr fxd 95% LTV)": 639.17,
            "25yrs 10.0% 1.49% (2yr fxd 75% LTV)": 466.67,
            "25yrs 10.0% 1.7% (3yr fxd 75% LTV)": 480.08,
            "25yrs 10.0% 1.99% (5yr fxd 75% LTV)": 498.93,
            "25yrs 10.0% 4.33% (Std Var Rate)": 664.73,
            "25yrs 10.0% 2.34% (Trkr 75% LTV)": 522.18,
            "30yrs 10.0% 3.99% (2yr fxd 95% LTV)": 571.09,
            "30yrs 10.0% 1.49% (2yr fxd 75% LTV)": 392.68,
            "30yrs 10.0% 1.7% (3yr fxd 75% LTV)": 406.39,
            "30yrs 10.0% 1.99% (5yr fxd 75% LTV)": 425.72,
            "30yrs 10.0% 4.33% (Std Var Rate)": 597.8,
            "30yrs 10.0% 2.34% (Trkr 75% LTV)": 449.65,
            "35yrs 10.0% 3.99% (2yr fxd 95% LTV)": 524.31,
            "35yrs 10.0% 1.49% (2yr fxd 75% LTV)": 340.12,
            "35yrs 10.0% 1.7% (3yr fxd 75% LTV)": 354.13,
            "35yrs 10.0% 1.99% (5yr fxd 75% LTV)": 373.93,
            "35yrs 10.0% 4.33% (Std Var Rate)": 552.12,
            "35yrs 10.0% 2.34% (Trkr 75% LTV)": 398.53,
            "20yrs 15.0% 3.99% (2yr fxd 95% LTV)": 699.27,
            "20yrs 15.0% 1.49% (2yr fxd 75% LTV)": 542.02,
            "20yrs 15.0% 1.7% (3yr fxd 75% LTV)": 554.4,
            "20yrs 15.0% 1.99% (5yr fxd 75% LTV)": 571.75,
            "20yrs 15.0% 4.33% (Std Var Rate)": 722.28,
            "20yrs 15.0% 2.34% (Trkr 75% LTV)": 593.08,
            "25yrs 15.0% 3.99% (2yr fxd 95% LTV)": 599.63,
            "25yrs 15.0% 1.49% (2yr fxd 75% LTV)": 436.72,
            "25yrs 15.0% 1.7% (3yr fxd 75% LTV)": 449.38,
            "25yrs 15.0% 1.99% (5yr fxd 75% LTV)": 467.18,
            "25yrs 15.0% 4.33% (Std Var Rate)": 623.78,
            "25yrs 15.0% 2.34% (Trkr 75% LTV)": 489.15,
            "30yrs 15.0% 3.99% (2yr fxd 95% LTV)": 535.34,
            "30yrs 15.0% 1.49% (2yr fxd 75% LTV)": 366.84,
            "30yrs 15.0% 1.7% (3yr fxd 75% LTV)": 379.79,
            "30yrs 15.0% 1.99% (5yr fxd 75% LTV)": 398.04,
            "30yrs 15.0% 4.33% (Std Var Rate)": 560.57,
            "30yrs 15.0% 2.34% (Trkr 75% LTV)": 420.64,
            "35yrs 15.0% 3.99% (2yr fxd 95% LTV)": 491.16,
            "35yrs 15.0% 1.49% (2yr fxd 75% LTV)": 317.2,
            "35yrs 15.0% 1.7% (3yr fxd 75% LTV)": 330.43,
            "35yrs 15.0% 1.99% (5yr fxd 75% LTV)": 349.14,
            "35yrs 15.0% 4.33% (Std Var Rate)": 517.42,
            "35yrs 15.0% 2.34% (Trkr 75% LTV)": 372.37,
            "20yrs 20.0% 3.99% (2yr fxd 95% LTV)": 653.87,
            "20yrs 20.0% 1.49% (2yr fxd 75% LTV)": 505.88,
            "20yrs 20.0% 1.7% (3yr fxd 75% LTV)": 517.53,
            "20yrs 20.0% 1.99% (5yr fxd 75% LTV)": 533.86,
            "20yrs 20.0% 4.33% (Std Var Rate)": 675.53,
            "20yrs 20.0% 2.34% (Trkr 75% LTV)": 553.93,
            "25yrs 20.0% 3.99% (2yr fxd 95% LTV)": 560.1,
            "25yrs 20.0% 1.49% (2yr fxd 75% LTV)": 406.77,
            "25yrs 20.0% 1.7% (3yr fxd 75% LTV)": 418.69,
            "25yrs 20.0% 1.99% (5yr fxd 75% LTV)": 435.44,
            "25yrs 20.0% 4.33% (Std Var Rate)": 582.82,
            "25yrs 20.0% 2.34% (Trkr 75% LTV)": 456.12,
            "30yrs 20.0% 3.99% (2yr fxd 95% LTV)": 499.59,
            "30yrs 20.0% 1.49% (2yr fxd 75% LTV)": 341.0,
            "30yrs 20.0% 1.7% (3yr fxd 75% LTV)": 353.19,
            "30yrs 20.0% 1.99% (5yr fxd 75% LTV)": 370.37,
            "30yrs 20.0% 4.33% (Std Var Rate)": 523.33,
            "30yrs 20.0% 2.34% (Trkr 75% LTV)": 391.64,
            "35yrs 20.0% 3.99% (2yr fxd 95% LTV)": 458.0,
            "35yrs 20.0% 1.49% (2yr fxd 75% LTV)": 294.28,
            "35yrs 20.0% 1.7% (3yr fxd 75% LTV)": 306.73,
            "35yrs 20.0% 1.99% (5yr fxd 75% LTV)": 324.34,
            "35yrs 20.0% 4.33% (Std Var Rate)": 482.73,
            "35yrs 20.0% 2.34% (Trkr 75% LTV)": 346.2,
        }

        self.assertEqual(self.property.to_h(), expected)


if __name__ == "__main__":
    unittest.main()
