import unittest
import os
from wordCounter import count_words


class MyTest(unittest.TestCase):

    def test_count_v1(self):
        self.assertEqual(count_words(os.getcwd(), 'тест'), 3)

    def test_count_v2(self):
        self.assertEqual(count_words(os.getcwd(), 'привет'), 4)

    def test_count_v3(self):
        self.assertEqual(count_words(os.getcwd(), 'письмо'), 3)