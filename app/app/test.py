from django.test import TestCase

from app.sample_test import multiply

class multiplytest(TestCase):

    def test_multiply(self):
        '''to check the sample unit test work'''
        self.assertEqual(multiply(5, 4), 20)
