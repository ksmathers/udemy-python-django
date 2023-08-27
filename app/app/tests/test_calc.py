#from django.test import TestCase
from django.test import SimpleTestCase as TestCase

from app.util import Calc

class ViewsTests(TestCase):
    def test_sum(self):
        c = Calc()
        c.add(32)
        c.add(16)
        self.assertEqual(c.accum(), 48)

        c.add(8)
        self.assertEqual(c.accum(), 56)

    def test_clear(self):
        c = Calc()
        c.add(12)
        self.assertEqual(c.accum(), 12)
        c.clear()
        self.assertEqual(c.accum(), 0)

        

        