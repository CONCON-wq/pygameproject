import unittest

class TestAdd(unittest.TestCase):
    def test_integers(self):
        a = 10
        b = 20

        self.assertEqual(a+b, 30, msg = 'test falied')

    def test_lists(self):
        a = [1,2]
        b= [3,4]

        self.assertEqual((a+b),[1,2,3,4],msg = 'test failed')

if __name__ == '__main__':
    unittest.main()