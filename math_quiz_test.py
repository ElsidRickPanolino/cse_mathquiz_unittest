import unittest
import main


class TestMathFunctions(unittest.TestCase):

    def test_add(self):
        self.assertEqual(main.add(2, 3), 5)
        self.assertEqual(main.add(-5, 3), -2)
        self.assertEqual(main.add(0, 0), 0)
        self.assertEqual(main.add(100, 200), 300)

    def test_subtract(self):
        self.assertEqual(main.subtract(5, 3), 2)
        self.assertEqual(main.subtract(10, 7), 3)
        self.assertEqual(main.subtract(10, 10), 0)
        self.assertEqual(main.subtract(50, 30), 20)

    def test_multiply(self):
        self.assertEqual(main.multiply(2, 3), 6)
        self.assertEqual(main.multiply(-5, 4), -20)
        self.assertEqual(main.multiply(5, 0), 0)
        self.assertEqual(main.multiply(7, 8), 56)

    def test_divide(self):
        self.assertAlmostEqual(main.divide(10, 2), 5.0)
        self.assertAlmostEqual(main.divide(7, 3), 2.3333, places=4)
        self.assertAlmostEqual(main.divide(10, 5), 2.0)
        self.assertAlmostEqual(main.divide(15, 4), 3.75, places=2)

    def test_verifyDivide(self):
        result = main.verifyDivide(1, 20)
        self.assertEqual(result, [[18, 2], [16, 2], [14, 2], [12, 2], [18, 3], [15, 3], [12, 3], [16, 4], [12, 4], [15, 5], [18, 6], [12, 6], [14, 7], [16, 8], [18, 9]])

    def test_check_answer(self):
        self.assertTrue(main.check_answer(5, 5))
        self.assertFalse(main.check_answer(5, 3))
        self.assertTrue(main.check_answer(0, 0))
        self.assertFalse(main.check_answer(-5, 5))

    def test_verifyDigit(self):
        self.assertTrue(main.verifyDigit('5'))
        self.assertFalse(main.verifyDigit('a'))
        self.assertFalse(main.verifyDigit('!'))
        self.assertTrue(main.verifyDigit('0'))

    def test_verifyInput(self):
        self.assertTrue(main.verifyInput('A', ['A', 'B', 'C']))
        self.assertTrue(main.verifyInput('b', ['A', 'B', 'C']))
        self.assertFalse(main.verifyInput('D', ['A', 'B', 'C']))
        self.assertTrue(main.verifyInput('c', ['A', 'b', 'C']))
        self.assertFalse(main.verifyInput('E', ['A', 'B', 'C']))

    def test_game(self):

        try:
            main.game()
        except Exception as e:
            self.fail(f"Executing game function raised an exception: {e}")


if __name__ == '__main__':
    unittest.main()
