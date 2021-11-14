from app import app
import unittest

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class TestConverter(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['WTF_CSRF_ENABLED'] = False

    def test_currency_converter(self):
        client = app.test_client(self)
        res = client.get('/')
        html = str(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<h1 class="title">Convert your money!</h1>',html)

    def test_conversion(self):
        client = app.test_client(self)
        res = client.post('/',data={'converting_from': 'USD','converting_to' : 'USD', 'amount': 20}, follow_redirects=True)
        html = str(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<div>US$20.0</div>', html)

    def test_conversion_2(self):
        client = app.test_client(self)
        res = client.post('/',data={'converting_from': 'MXN','converting_to' : 'MXN', 'amount': 100}, follow_redirects=True)
        html = str(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<div>$100.0</div>', html)

    def test_conversion_decimal(self):
        client = app.test_client(self)
        res = client.post('/',data={'converting_from': 'MXN','converting_to' : 'MXN', 'amount': 20.88}, follow_redirects=True)
        html = str(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<div>$20.88</div>', html)

    def test_invalid_conversion_from(self):
        client = app.test_client(self)
        res = client.post('/',data={'converting_from': 'NJK','converting_to' : 'MXN', 'amount': 100}, follow_redirects=True)
        html = str(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<h1 class="title">Convert your money!</h1>', html)

    def test_invalid_conversion_to(self):
        client = app.test_client(self)
        res = client.post('/',data={'converting_from': 'MXN','converting_to' : 'MJK', 'amount': 100}, follow_redirects=True)
        html = str(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<h1 class="title">Convert your money!</h1>', html)


    def test_invalid_conversion_amount(self):
        client = app.test_client(self)
        res = client.post('/',data={'converting_from': 'MXN','converting_to' : 'MXN', 'amount': "NOT MONEY"}, follow_redirects=True)
        html = str(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertIn('<h1 class="title">Convert your money!</h1>', html)