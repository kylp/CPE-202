import unittest
from exp_eval import infix_to_postfix, postfix_eval, postfix_valid


class PostfixTestCase(unittest.TestCase):
    def test_something(self):
        infix_cases = [
            "( ( 5 - 3 ) ^ 2 + ( 4 - 2 ) ^ 2 ) ^ ( 1 / 2 )",
            "( ( 15 / ( 7 - ( 1 + 1 ) ) ) * 3 ) - ( 2 + ( 1 + 1 ) )",
            "10 + 3 * 5 / ( 16 - 4 )",
            "5 * 3 ^ ( 4 - 2 )",
            "( ( 1 * 2 ) + ( 3 / 4 ) )",
            "( ( 2 * ( 3 + 4 ) ) / 5 )",
            "( 3 * ( 4 + 6 / 3 ) )",
            "~ 3 * 3 + 9",
            "( ~ 3 ) ^ 2 + 9",
            "~ 3 ^ 2 + 9",
            "4 ^ ( ~ 1 ) * 4",
            "~ 1",
            "1",
            "7 - 8 + 3",
        ]
        postfix_cases = [
            "5 3 - 2 ^ 4 2 - 2 ^ + 1 2 / ^",
            "15 7 1 1 + - / 3 * 2 1 1 + + -",
            "10 3 5 * 16 4 - / +",
            "5 3 4 2 - ^ *",
            "1 2 * 3 4 / +",
            "2 3 4 + * 5 /",
            "3 4 6 3 / + *",
            "3 ~ 3 * 9 +",
            "3 ~ 2 ^ 9 +",
            "3 2 ^ ~ 9 +",
            "4 1 ~ ^ 4 *",
            "1 ~",
            "1",
            "7 8 - 3 +",
        ]
        results = [2.828, 5.0, 11.25, 45, 2.75, 2.8, 18.0, 0, 18, 0, 1.0, -1, 1, 2]
        for i in range (0, len(postfix_cases)):
            print("testing:", infix_cases[i])
            postfix = infix_to_postfix(infix_cases[i])
            self.assertEqual(postfix_cases[i], postfix)
            self.assertTrue(postfix_valid(postfix))
            self.assertAlmostEqual(results[i], postfix_eval(postfix), 2)

        self.assertFalse(postfix_valid("1 + 1"))
        self.assertFalse(postfix_valid("1 1 + 1"))
        self.assertFalse(postfix_valid("~ 1 1 +"))
        self.assertFalse(postfix_valid(""))

        self.assertRaises(ZeroDivisionError, postfix_eval, "1 0 /")


if __name__ == '__main__':
    unittest.main()
