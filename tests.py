"""
Contains tests for the Binary class.
"""

import unittest

from bitarray import bitarray
from parameterized import parameterized

from binary import Binary


class TestBinaryInitialization(unittest.TestCase):
    """
    Test cases for Binary class initialization.
    """

    @parameterized.expand(
        [
            (10, 10),
            ("1010", 10),
            (bitarray("1010"), 10),
            ([1, 0, 1, 0], 10),
            (Binary(10), 10),
        ]
    )
    def test_init(self, value, expected):
        """
        Test Binary initialization with various types.
        """

        self.assertEqual(
            Binary(value).to_decimal(), expected, msg=f"Failed for value: {value}."
        )


class TestBinaryRepresentation(unittest.TestCase):
    """
    Test cases for string and repr representations of Binary class.
    """

    @parameterized.expand(
        [
            (Binary(10), "1010"),
            (Binary("1010"), "1010"),
        ]
    )
    def test_str(self, binary, expected):
        """
        Test __str__ method of Binary class.
        """

        self.assertEqual(str(binary), expected, msg=f"Failed for binary: {binary}.")

    @parameterized.expand(
        [
            (Binary(10), "Binary(10)"),
            (Binary("1010"), "Binary(10)"),
        ]
    )
    def test_repr(self, binary, expected):
        """
        Test __repr__ method of Binary class.
        """

        self.assertEqual(repr(binary), expected, msg=f"Failed for binary: {binary}.")


class TestBinaryComparisonOperators(unittest.TestCase):
    """
    Test cases for comparison operators of Binary class.
    """

    @parameterized.expand(
        [
            (Binary(10), Binary(10), True),
            (Binary(7), Binary(10), False),
            (Binary(10), Binary(7), False),
            (Binary(7), Binary(7), True),
        ]
    )
    def test_eq(self, left, right, expected):
        """
        Test __eq__ method of Binary class.
        """

        self.assertEqual(
            left == right, expected, msg=f"Failed for expression: {left} == {right}."
        )

    @parameterized.expand(
        [
            (Binary(7), Binary(10), True),
            (Binary(10), Binary(7), False),
        ]
    )
    def test_lt(self, left, right, expected):
        """
        Test __lt__ method of Binary class.
        """

        self.assertEqual(
            left < right, expected, msg=f"Failed for expression: {left} < {right}."
        )

    @parameterized.expand(
        [
            (Binary(10), Binary(10), True),
            (Binary(9), Binary(10), True),
            (Binary(10), Binary(9), False),
        ]
    )
    def test_le(self, left, right, expected):
        """
        Test __le__ method of Binary class.
        """

        self.assertEqual(
            left <= right, expected, msg=f"Failed for expression: {left} <= {right}."
        )

    @parameterized.expand(
        [
            (Binary(11), Binary(10), True),
            (Binary(10), Binary(11), False),
        ]
    )
    def test_gt(self, left, right, expected):
        """
        Test __gt__ method of Binary class.
        """

        self.assertEqual(
            left > right, expected, msg=f"Failed for expression: {left} > {right}."
        )

    @parameterized.expand(
        [
            (Binary(10), Binary(10), True),
            (Binary(11), Binary(10), True),
            (Binary(10), Binary(11), False),
        ]
    )
    def test_ge(self, left, right, expected):
        """
        Test __ge__ method of Binary class.
        """

        self.assertEqual(
            left >= right, expected, msg=f"Failed for expression: {left} >= {right}."
        )

    @parameterized.expand(
        [
            (Binary(10), Binary(9), True),
            (Binary(10), Binary(10), False),
        ]
    )
    def test_ne(self, left, right, expected):
        """
        Test __ne__ method of Binary class.
        """

        self.assertEqual(
            left != right, expected, msg=f"Failed for expression: {left} != {right}."
        )

    # pylint: disable=pointless-statement
    @parameterized.expand(
        [
            (Binary(10), 10),
            (Binary(10), "1010"),
            (Binary(10), []),
            (Binary(10), {}),
            (Binary(10), 10.5),
            (Binary(10), object()),
        ]
    )
    def test_comparisons_with_invalid_type(self, binary, other):
        """
        Test comparison operators with invalid types.
        """

        with self.assertRaises(
            NotImplementedError, msg=f"Failed for expression: {binary} == {other}."
        ):
            binary == other
        with self.assertRaises(
            NotImplementedError, msg=f"Failed for expression: {binary} != {other}."
        ):
            binary != other
        with self.assertRaises(
            NotImplementedError, msg=f"Failed for expression: {binary} < {other}."
        ):
            binary < other
        with self.assertRaises(
            NotImplementedError, msg=f"Failed for expression: {binary} <= {other}."
        ):
            binary <= other
        with self.assertRaises(
            NotImplementedError, msg=f"Failed for expression: {binary} > {other}."
        ):
            binary > other
        with self.assertRaises(
            NotImplementedError, msg=f"Failed for expression: {binary} >= {other}."
        ):
            binary >= other

    # pylint: enable=pointless-statement


class TestBinaryMethods(unittest.TestCase):
    """
    Test cases for Binary class methods.
    """

    @parameterized.expand(
        [
            ("1010", 10),
            (bitarray("1010"), 10),
        ]
    )
    def test_to_decimal(self, value, expected):
        """
        Test to_decimal method of Binary class.
        """

        self.assertEqual(
            Binary(value).to_decimal(), expected, msg=f"Failed for value: {value}."
        )


class TestBitwiseOperators(unittest.TestCase):
    """
    Test cases for bitwise operators of Binary class.
    """

    @parameterized.expand(
        [
            (Binary("1101 1001"), Binary("1001 1011"), Binary("1001 1001")),
            (Binary("1101 1001"), Binary("1001 1010"), Binary("1001 1000")),
        ]
    )
    def test_and(self, left, right, expected):
        """
        Test __and__ method of Binary class.
        """

        self.assertEqual(
            left & right, expected, msg=f"Failed for operator: {left} & {right}."
        )

    @parameterized.expand(
        [
            (Binary("1101 1001"), Binary("1001 1011"), Binary("1101 1011")),
            (Binary("1101 1001"), Binary("1001 1010"), Binary("1101 1011")),
        ]
    )
    def test_or(self, left, right, expected):
        """
        Test __or__ method of Binary class.
        """

        self.assertEqual(
            left | right, expected, msg=f"Failed for opreator: {left} | {right}."
        )

    @parameterized.expand(
        [
            (Binary("1101 1001"), Binary("1001 1011"), Binary("0100 0010")),
            (Binary("1101 1001"), Binary("1001 1010"), Binary("0100 0011")),
        ]
    )
    def test_xor(self, left, right, expected):
        """
        Test __xor__ method of Binary class.
        """

        self.assertEqual(
            left ^ right, expected, msg=f"Failed for operator: {left} ^ {right}."
        )

    @parameterized.expand(
        [
            (Binary("1101 1001"), 2, Binary("110 0100")),
            (Binary("1101 1001"), 3, Binary("1100 1000")),
            (Binary("1101 1001"), 8, Binary("0000 0000")),
        ]
    )
    def test_lshift(self, binary, shift, expected):
        """
        Test __lshift__ method of Binary class.
        """

        self.assertEqual(
            binary << shift, expected, msg=f"Failed for operator: {binary} << {shift}."
        )

    @parameterized.expand(
        [
            (Binary("1101 1001"), 2, Binary("0011 0110")),
            (Binary("1101 1001"), 3, Binary("0001 1011")),
            (Binary("1101 1001"), 8, Binary("0000 0000")),
        ]
    )
    def test_rshift(self, binary, shift, expected):
        """
        Test __rshift__ method of Binary class.
        """

        self.assertEqual(
            binary >> shift, expected, msg=f"Failed for operator: {binary} >> {shift}."
        )


class TestSmallerMethods(unittest.TestCase):
    """
    Test cases for smaller methods of Binary class.
    """

    @parameterized.expand(
        [
            (Binary("1101 1001"), 3, Binary("1101 0001")),
            (Binary("1101 1001"), (3, 4, 5), Binary("1110 0001")),
        ]
    )
    def test_flip_bit(self, binary, position, expected):
        """
        Test flip_bit method of Binary class.
        """

        binary.flip_bit(position)
        self.assertEqual(binary, expected, msg="Failed for bit flip.")


if __name__ == "__main__":
    unittest.main()
