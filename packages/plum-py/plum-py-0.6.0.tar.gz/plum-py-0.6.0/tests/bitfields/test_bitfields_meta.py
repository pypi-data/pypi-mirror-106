# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
# Copyright 2021 Daniel Mark Gass, see __about__.py for license information.
# # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # # #
"""Test construction of bit field classes."""

# pylint: disable=invalid-name

import pytest
from baseline import Baseline

from plum.bitfields import BitFields, bitfield
from plum.conformance import wrap_message


class TestMethodOverrides:

    """Test __init__ and property getters left alone if supplied in class namespace."""

    def test_init(self):
        class MyBits(BitFields):
            f0 = bitfield(size=1)

            def __init__(self, custom):
                super().__init__()
                MyBits.custom = custom

        MyBits(custom=True)
        assert MyBits.custom is True

    def test_getter(self):
        class MyBits(BitFields):
            f0 = bitfield(size=1)

            @f0.getter
            def f0(self):
                return "custom"

        assert MyBits.from_int(0).f0 == "custom"


class TestExceptions:

    """Test validation of class."""

    @staticmethod
    def test_bitfield_bad_type():
        """Test annotation contains bad type."""

        expected_message = Baseline(
            """
            bit field 'f2' type must be int-like
            """
        )

        with pytest.raises(TypeError) as trap:

            class Sample(BitFields):  # pylint: disable=unused-variable
                """Sample bit field type."""

                f1: int = bitfield(lsb=0, size=8)
                f2: str = bitfield(lsb=8, size=8)

        assert wrap_message(trap.value) == expected_message

    @staticmethod
    def test_bitfield_overlap():
        """Test bit fields overlap."""

        expected_message = Baseline(
            """
            bit field 'f2' overlaps with 'f1'
            """
        )

        with pytest.raises(TypeError) as trap:

            class Sample(BitFields):  # pylint: disable=unused-variable
                """Sample bit field type."""

                f1: int = bitfield(lsb=0, size=8)
                f2: int = bitfield(lsb=7, size=8)

        assert wrap_message(trap.value) == expected_message

    @staticmethod
    def test_nbytes_too_small():
        """Test nbytes argument insufficient size."""

        expected_message = Baseline(
            """
            nbytes must be at least 2 for bitfields specified
            """
        )

        with pytest.raises(TypeError) as trap:

            class Sample(BitFields, nbytes=1):  # pylint: disable=unused-variable
                """Sample bit field type."""

                f1: int = bitfield(lsb=0, size=8)
                f2: int = bitfield(lsb=8, size=8)

        assert wrap_message(trap.value) == expected_message

    @staticmethod
    def test_byteorder_invalid():
        """Test byteorder argument wrong value."""

        expected_message = Baseline(
            """
            byteorder must be either "big" or "little"
            """
        )

        with pytest.raises(ValueError) as trap:
            # pylint: disable=unused-variable
            class Sample(BitFields, byteorder="native"):
                """Sample bit field type."""

                f1: int = bitfield(lsb=0, size=8)

        assert wrap_message(trap.value) == expected_message

    @staticmethod
    def test_default_too_big():
        """Test default argument exceeds max."""

        expected_message = Baseline(
            """
            default must be: 0 <= number <= 0xff
            """
        )

        with pytest.raises(ValueError) as trap:
            # pylint: disable=unused-variable
            class Sample(BitFields, nbytes=1, default=0x100):
                """Sample bit field type."""

                f1: int = bitfield(lsb=0, size=8)

        assert wrap_message(trap.value) == expected_message

    @staticmethod
    def test_default_negative():
        """Test default argument less than zero."""

        expected_message = Baseline(
            """
            default must be: 0 <= number <= 0xff
            """
        )

        with pytest.raises(ValueError) as trap:
            # pylint: disable=unused-variable
            class Sample(BitFields, nbytes=1, default=-1):
                """Sample bit field type."""

                f1: int = bitfield(lsb=0, size=1, default=1)

        assert wrap_message(trap.value) == expected_message

    @staticmethod
    def test_ignore_too_big():
        """Test ignore argument exceeds max."""

        expected_message = Baseline(
            """
            ignore must be: 0 <= number <= 0xff
            """
        )

        with pytest.raises(ValueError) as trap:
            # pylint: disable=unused-variable
            class Sample(BitFields, nbytes=1, ignore=0x100):
                """Sample bit field type."""

                f1: int = bitfield(lsb=0, size=8)

        assert wrap_message(trap.value) == expected_message

    @staticmethod
    def test_ignore_negative():
        """Test ignore argument less than zero."""

        expected_message = Baseline(
            """
            ignore must be: 0 <= number <= 0xff
            """
        )

        with pytest.raises(ValueError) as trap:

            class Sample(
                BitFields, nbytes=1, ignore=-1
            ):  # pylint: disable=unused-variable
                """Sample bit field type."""

                f1: int = bitfield(lsb=0, size=1)

        assert wrap_message(trap.value) == expected_message
