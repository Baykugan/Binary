"""
Contains the Binary class.
"""

from typing import Any, Self


class Binary:
    """
    Binary class

    This class is used to represent a binary number.
    """

    #########################
    ##### Magic methods #####
    #########################

    def __init__(self, value: Self | int | str | bytearray | list[int]) -> None:
        self.value = Binary.from_value(value)

    def __str__(self) -> str:
        return "".join(
            str(Binary._get_bit(self.value, i))
            for i in reversed(range(len(self.value) * 8))
        )

    def __repr__(self) -> str:
        return f"Binary({self.value})"

    ##########################
    ##### Public methods #####
    ##########################

    def to_decimal(self) -> int:
        """
        Convert the binary number to a decimal number.
        """

        return Binary._to_decimal(self)

    #########################
    ##### Class methods #####
    #########################

    @classmethod
    def from_value(cls, value: Any) -> bytearray:
        """
        Checks the type of the value and calls the
        appropriate method to create a byte array.
        """

        if isinstance(value, Binary):
            return value.value
        if isinstance(value, bytearray):
            return value
        if isinstance(value, int):
            return cls.from_decimal(value)
        if isinstance(value, str):
            return cls.from_string(value)
        if isinstance(value, list):
            return cls.from_list(value)
        raise ValueError("Invalid value")

    @classmethod
    def from_decimal(cls, decimal: int) -> bytearray:
        """
        Create a byte array from a decimal number.
        """

        binary = []
        if decimal < 0:
            raise ValueError("Invalid decimal value")
        if decimal == 0:
            binary.append(0)

        while decimal > 0:
            binary.append(decimal % 2)
            decimal //= 2
        return cls._create_bit_array(list(reversed(list(binary))))

    @classmethod
    def from_string(cls, string: str) -> bytearray:
        """
        Create a byte array from a binary string.
        """

        if not all(bit in "01" for bit in string):
            raise ValueError("Invalid binary string")
        return cls._create_bit_array([int(bit) for bit in string])

    @classmethod
    def from_list(cls, lst: list[int]) -> bytearray:
        """
        Create a byte array from a binary list.
        """

        if not all(bit in [0, 1] for bit in lst):
            raise ValueError("Invalid binary list")
        return cls._create_bit_array(lst)

    ###########################
    ##### Static methods ######
    ###########################

    @staticmethod
    def _to_decimal(binary: Self) -> int:
        decimal = 0
        for i in range(len(binary.value) * 8):
            decimal += Binary._get_bit(binary.value, i) * 2**i
        return decimal

    @staticmethod
    def _create_bit_array(lst: list[int]) -> bytearray:
        bit_array = bytearray((len(lst) + 7) // 8)
        for position, bit in enumerate(reversed(lst)):
            Binary._set_bit(bit_array, position, bit)
        return bit_array

    @staticmethod
    def _get_bit(value: bytearray, position: int) -> int:
        byte_index, bit_index = divmod(position, 8)
        return (value[byte_index] & (1 << bit_index)) >> bit_index

    @staticmethod
    def _set_bit(value: bytearray, position: int, bit: int) -> None:
        byte_index, bit_index = divmod(position, 8)
        if bit == 1:
            value[byte_index] |= 1 << bit_index
        else:
            value[byte_index] &= ~(1 << bit_index)
