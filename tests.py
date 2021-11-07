from app import app
import unittest

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class TestConverter(unittest.TestCase):

    def test_currency_converter(self):
        client = app.test_client(self)
        res = client.get('/')
        html = res.get_data(as_text= True)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<h1>Convert your money!</h1>')

    def test_conversion(self):
        client = app.test_client(self)
        res = client.post('/',data={'converting_currency': 'USD','converted_currency' : 'USD', 'amount': 20})
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<div>USD$20</div>', html)

    def test_conversion(self):
        client = app.test_client(self)
        res = client.post('/converted',data={'currency_type': 'MXN','converted_currency' : 'MXN', 'amount': 100})
        html = res.get_data(as_text=True)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<div>$100.0</div>', html)