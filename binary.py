"""
Contains the Binary class.
"""

from typing import Any, Union, Self
from bitarray import bitarray


class Binary:
    """
    Binary class

    This class is used to represent a binary number.
    """

    #########################
    ##### Magic methods #####
    #########################

    def __init__(self, value: Union[Self, int, str, bitarray, list[int]] = 0) -> None:
        self.bits = self.from_value(value)

    def __str__(self) -> str:
        return self.bits.to01()

    def __repr__(self) -> str:
        return f"Binary({self.to_decimal()})"

    def __eq__(self, other: Any) -> bool:
        if isinstance(other, Binary):
            return Binary._compare_binary(self, other, "eq")
        raise NotImplementedError(
            f"Cannot take equality of Binary with {type(other).__name__}"
        )

    def __lt__(self, other: Any) -> bool:
        if isinstance(other, Binary):
            return Binary._compare_binary(self, other, "lt")
        raise NotImplementedError(
            f"Cannot take less than of Binary with {type(other).__name__}"
        )

    def __le__(self, other: Any) -> bool:
        if isinstance(other, Binary):
            return Binary._compare_binary(self, other, "le")
        raise NotImplementedError(
            f"Cannot take less than or equal of Binary with {type(other).__name__}"
        )

    def __gt__(self, other: Any) -> bool:
        if isinstance(other, Binary):
            return Binary._compare_binary(self, other, "gt")
        raise NotImplementedError(
            f"Cannot take greater than of Binary with {type(other).__name__}"
        )

    def __ge__(self, other: Any) -> bool:
        if isinstance(other, Binary):
            return Binary._compare_binary(self, other, "ge")
        raise NotImplementedError(
            f"Cannot take greater than or equal of Binary with {type(other).__name__}"
        )

    def __ne__(self, other: Any) -> bool:
        if isinstance(other, Binary):
            return Binary._compare_binary(self, other, "ne")
        raise NotImplementedError(
            f"Cannot take not equal of Binary with {type(other).__name__}"
        )

    ###################################
    ##### Public Instance methods #####
    ###################################

    def to_decimal(self) -> int:
        """
        Convert the binary number to a decimal number.
        """

        return Binary._to_decimal(self.bits)

    ################################
    ##### Public Class methods #####
    ################################

    @classmethod
    def from_value(cls, value: Any) -> bitarray:
        """
        Checks the type of the value and calls the
        appropriate method to create a bitarray.
        """

        if isinstance(value, Binary):
            return value.bits
        if isinstance(value, bitarray):
            return value
        if isinstance(value, int):
            return cls._create_bit_array(bin(value)[2:])
        if isinstance(value, (str, list, tuple, set)):
            return cls._create_bit_array(value)
        raise ValueError(f"Invalid type of value: {str(type(value))[7:-1]}")

    ###################################
    ##### Private Static methods ######
    ###################################

    @staticmethod
    def _to_decimal(value: Self) -> int:
        return int(value.to01(), 2)

    @staticmethod
    def _create_bit_array(value: Any) -> bitarray:
        return bitarray(value)

    @staticmethod
    def _get_bit(bit_array: bitarray, position: int) -> int:
        return bit_array[position]

    @staticmethod
    def _set_bit(bit_array: bitarray, position: int, bit: int) -> None:
        bit_array[position] = bit

    @staticmethod
    def _normalize_bit_arrays(*bit_arrays: tuple[bitarray]) -> tuple[bitarray]:
        max_len = max(map(len, bit_arrays))
        return tuple(
            bitarray("0") * (max_len - len(bit_array)) + bit_array
            for bit_array in bit_arrays
        )

    @staticmethod
    def _compare_binary(left: Self, right: Self, operator: str) -> bool:
        normalized_left, normalized_right = Binary._normalize_bit_arrays(
            left.bits, right.bits
        )
        if operator == "eq":
            return normalized_left == normalized_right
        if operator == "lt":
            return normalized_left < normalized_right
        if operator == "le":
            return normalized_left <= normalized_right
        if operator == "gt":
            return normalized_left > normalized_right
        if operator == "ge":
            return normalized_left >= normalized_right
        if operator == "ne":
            return normalized_left != normalized_right
        raise ValueError("Invalid operator")
