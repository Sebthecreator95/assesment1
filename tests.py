from app import app
import unittest

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class TestConverter(unittest.TestCase):
    def setUp(self):
        tester = app.test_client(self)

    def test_currency_converter(self):
        res = tester.get('/')
        html = res.get_data(as_text= True)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<h1>Convert your money!</h1>')

    def test_conversion(self):
        res = client.post('/converted',data={'currency_type': 'BTC','converted_currency' : 'BTC', 'amount': 20})
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<div>฿20</div>', html)

    def test_conversion(self):
        res = client.post('/converted',data={'currency_type': 'MXN','converted_currency' : 'MXN', 'amount': 100})
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<div>$100.0</div>', html)