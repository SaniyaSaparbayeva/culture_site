from django.test import TestCase
from kz_culture.models import About
class YourTestClass(TestCase):
    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once to set up non-modified data for all class methods.")
        pass

    def setUp(self):
        print("setUp: Run once for every test method to setup clean data.")
        pass

    def test_isupper(self):
        print("Method: test_isupper.")
        self.assertTrue('DJANGO'.isupper())
        self.assertFalse('dfd'.isupper())

    def test_model(self):
        print("Method: test_model.")
        about = About.objects.create(title='About History', content='some content')
        self.assertEqual(str(about), 'About History')

    def test_homepage(self):
        print("Method: test_homepage.")
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
