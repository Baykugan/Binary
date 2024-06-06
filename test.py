"""
Contains the unit tests for the Binary class.
"""

import unittest

from binary import Binary


class TestBinary(unittest.TestCase):
    """
    TestBinary class

    This class contains the unit tests for the Binary class.
    """

    # pylint: disable=protected-access
    def test_create_byte_array(self):
        """
        Test the _create_bit_array method.
        """

        
        bit_array = Binary._create_bit_array([0])
        self.assertEqual(
            bit_array,
            bytearray([0]),
            "Failed to create byte array from list [0]",
        )

        bit_array = Binary._create_bit_array([1])
        self.assertEqual(
            bit_array,
            bytearray([1]),
            "Failed to create byte array from list [1]",
        )

        large_bit_array = Binary._create_bit_array([1] * 16)
        self.assertEqual(
            large_bit_array,
            bytearray([255, 255]),
            "Failed to create byte array from [1] * 16",
        )
    # pylint: enable=protected-access

    def test_from_decimal(self):
        """
        Test the from_decimal method.
        """

        bit_array = Binary.from_decimal(0)
        self.assertEqual(
            bit_array,
            bytearray([0]),
            "Failed to create byte array from decimal 0",
        )

        bit_array = Binary.from_decimal(1)
        self.assertEqual(
            bit_array,
            bytearray([1]),
            "Failed to create byte array from decimal 1",
        )

        bit_array = Binary.from_decimal(2**16 - 1)
        self.assertEqual(
            bit_array,
            bytearray([255, 255]),
            "Failed to create byte array from decimal 2**16 - 1",
        )

    def test_from_decimal_invalid(self):
        """
        Test the from_decimal method with invalid input.
        """

        with self.assertRaises(ValueError, msg="Invalid decimal value"):
            Binary.from_decimal(-1)

    def test_from_string(self):
        """
        Test the from_string method.
        """

        bit_array = Binary.from_string("0")
        self.assertEqual(
            bit_array,
            bytearray([0]),
            "Failed to create byte array from string '0'",
        )

        bit_array = Binary.from_string("1")
        self.assertEqual(
            bit_array,
            bytearray([1]),
            "Failed to create byte array from string '1'",
        )

        bit_array = Binary.from_string("1" * 16)
        self.assertEqual(
            bit_array,
            bytearray([255, 255]),
            "Failed to create byte array from string '1' * 16",
        )

    def test_from_string_invalid(self):
        """
        Test the from_string method with invalid input.
        """

        with self.assertRaises(ValueError, msg="Invalid binary string"):
            Binary.from_string("2")

    def test_from_list(self):
        """
        Test the from_list method.
        """

        bit_array = Binary.from_list([0])
        self.assertEqual(
            bit_array,
            bytearray([0]),
            "Failed to create byte array from list [0]",
        )

        bit_array = Binary.from_list([1])
        self.assertEqual(
            bit_array,
            bytearray([1]),
            "Failed to create byte array from list [1]",
        )

        bit_array = Binary.from_list([1] * 16)
        self.assertEqual(
            bit_array,
            bytearray([255, 255]),
            "Failed to create byte array from list [1] * 16",
        )

    def test_from_list_invalid(self):
        """
        Test the from_list method with invalid input.
        """

        with self.assertRaises(ValueError, msg="Invalid binary list"):
            Binary.from_list([2])

    def test_to_decimal(self):
        """
        Test the to_decimal method.
        """

        binary = Binary(0)
        self.assertEqual(
            binary.to_decimal(),
            0,
            "Failed to convert byte array [0] to decimal",
        )

        binary = Binary(1)
        self.assertEqual(
            binary.to_decimal(),
            1,
            "Failed to convert byte array [1] to decimal",
        )

        binary = Binary(2**16 - 1)
        self.assertEqual(
            binary.to_decimal(),
            2**16 - 1,
            "Failed to convert byte array [255, 255] to decimal",
        )

    def test_from_value(self):
        """
        Test the from_value method.
        """

        binary = Binary.from_value(Binary(0))
        self.assertEqual(
            binary,
            bytearray([0]),
            "Failed to convert Binary object to byte array",
        )

        binary = Binary.from_value(bytearray([0]))
        self.assertEqual(
            binary,
            bytearray([0]),
            "Failed to convert byte array to byte array",
        )

        binary = Binary.from_value(0)
        self.assertEqual(
            binary,
            bytearray([0]),
            "Failed to convert decimal to byte array",
        )

        binary = Binary.from_value("0")
        self.assertEqual(
            binary,
            bytearray([0]),
            "Failed to convert string to byte array",
        )

        binary = Binary.from_value([0])
        self.assertEqual(
            binary,
            bytearray([0]),
            "Failed to convert list to byte array",
        )

    def test_from_value_invalid(self):
        """
        Test the from_value method with invalid input.
        """

        with self.assertRaises(ValueError, msg="Invalid value"):
            Binary.from_value(None)


if __name__ == "__main__":
    unittest.main()
