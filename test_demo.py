import unittest


def sum_number(a, b):
    return a + b


class MyTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        print("setupClass")

    def setUp(self) -> None:
        print("setUp")

    def test_sum_int(self):
        print("test_sum_int")
        self.assertEqual(sum_number(1, 2), 3)
        self.assertEqual(sum_number(100, 200), 300)

    def test_sum_float(self):
        print("test_sum_float")
        # self.assertEqual(sum_number(1.1, 2.2), 3.3)
        self.assertAlmostEqual(sum_number(1.1, 2.2), 3.3)

    def tearDown(self) -> None:
        print("tearDown")

    @classmethod
    def tearDownClass(cls) -> None:
        print("tearDownClass")


if __name__ == '__main__':
    unittest.main()
