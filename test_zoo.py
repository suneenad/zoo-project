import unittest
from zoo import Zoo

class TestZoo(unittest.TestCase):
    def setUp(self):
        self.zoo = Zoo()

    def test_weird_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(-1), 0)
    def test_child_min_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(0), 50)
    def test_child_max_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(12), 50)
    def test_teenager_min_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(13), 100)
    def test_teenager_max_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(20), 100)
    def test_adult_min_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(21), 150)
    def test_adult_max_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(60), 150)
    def test_old_ticket_price(self):
        self.assertEqual(self.zoo.get_ticket_price(61), 100)
       
    # Add your additional test cases here.

if __name__ == '__main__':
    unittest.main()