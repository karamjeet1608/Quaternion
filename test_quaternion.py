"""
This file contains the unit tests of Quaternion class
Developer: Karamjeet singh.
Version: 1.0.0
"""
import unittest
from quaternion import Quaternion



class TestQuaternionInitialize(unittest.TestCase):
    """
    Class to test Quaternion object initialization function with valid and invalid inputs.
    """
    def test_init_one(self):
        """
        function test Quaternion object initialization with valid single parameter.
        """
        q = Quaternion(1)
        self.assertIsInstance(q, Quaternion)
        self.assertEqual(q.__str__(), "1.00 +0.00i +0.00j +0.00k")

    def test_init_four(self):
        """
        function test Quaternion object initialization with valid 4 parameters.
        """
        q = Quaternion(1, 2, 3, 4)
        self.assertIsInstance(q, Quaternion)
        self.assertEqual(q.__str__(), "1.00 +2.00i +3.00j +4.00k")

    def test_init_scalar(self):
        """
        function test Quaternion object initialization with valid key as scalar parameter.
        """
        q = Quaternion(scalar=4)
        self.assertIsInstance(q, Quaternion)
        self.assertEqual(q.__str__(), "4.00 +0.00i +0.00j +0.00k")

    def test_init_nparray(self):
        """
        function test Quaternion object initialization with valid key as np_array parameter.
        """
        q = Quaternion(np_array=[5, 6, 7, 8])
        self.assertIsInstance(q, Quaternion)
        self.assertEqual(q.__str__(), "5.00 +6.00i +7.00j +8.00k")

    def test_init_invalid_noinput(self):
        """
        function test Quaternion object initialization with no parameter.
        """
        with self.assertRaises(ValueError):
            Quaternion()

    def test_init_invalid_string(self):
        """
        function test Quaternion object initialization with string as parameter.
        """
        with self.assertRaises(ValueError):
            Quaternion()

    def test_init_invalid_twoinputs(self):
        """
        function test Quaternion object initialization with 2 parameter.
        """
        with self.assertRaises(ValueError):
            Quaternion(3, 4)

    def test_init_invalid_threeinputs(self):
        """
        function test Quaternion object initialization with 3 parameter.
        """
        with self.assertRaises(ValueError):
            Quaternion(3, 4, 5)

    def test_init_invalid_four(self):
        """
        function test Quaternion object initialization with 4 parameter one of which is number.
        """
        with self.assertRaises(Exception):
            Quaternion(3, "karam", 4, 5)


class TestQuaternionAddition(unittest.TestCase):
    """
    Class to test Quaternion class Addition function with valid and invalid inputs.
    """
    def test_addition_valid(self):
        """
        function test Quaternion object Addition with valid inputs.
        """
        quant1 = Quaternion(2)
        quant2 = Quaternion(3)
        quant_sum = quant1.__addition__(quant2)
        self.assertEqual(quant_sum.__str__(), "5.00 +0.00i +0.00j +0.00k")

    def test_addition_invalid(self):
        """
        function test Quaternion object Addition with invalid inputs.
        """
        with self.assertRaises(ValueError):
            quant1 = Quaternion(2)
            quant2 = 3
            quant1.__addition__(quant2)


class TestQuaternionScalarMultiplication(unittest.TestCase):
    """
    Class to test Quaternion class Scalar Multiplication function with valid and invalid inputs.
    """
    def test_scalar_multiplication_valid(self):
        """
        function test Quaternion Scalar Multiplication with valid inputs.
        """
        quant1 = Quaternion(1, 2, 3, 4)
        scalar = 3
        quant_scalar_prod = quant1.scalar_multiplication(scalar=scalar)
        self.assertEqual(quant_scalar_prod.__str__(), "3.00 +6.00i +9.00j +12.00k")

    def test_scalar_multiplication_invalid(self):
        """
        function test Quaternion Scalar Multiplication with invalid inputs.
        """
        with self.assertRaises(ValueError):
            quant1 = Quaternion(1, 2, 3, 4)
            scalar = "karam"
            quant1.scalar_multiplication(scalar=scalar)


class TestQuaternionRealPart(unittest.TestCase):
    """
    Class to test Quaternion class real part function with valid and invalid inputs.
    """
    def test_real_part_valid(self):
        """
        function test Quaternion real part with valid inputs.
        """
        quant1 = Quaternion(1, 2, 3, 4)
        quant_real_part = quant1.real_part()
        self.assertEqual(quant_real_part, 1)

    def test_real_part_invalid(self):
        """
        function test Quaternion real part with invalid inputs.
        """
        with self.assertRaises(ValueError):
            quant1 = Quaternion("kara")
            quant1.real_part()


class TestQuaternionConjugate(unittest.TestCase):
    """
    Class to test Quaternion class Scalar Multiplication function with valid input.
    """
    def test_conjugate_valid(self):
        """
        function test Quaternion conjugate with valid inputs.
        """
        quant1 = Quaternion(1, 2, 3, 4)
        quant_conjugate = quant1.conjugate()
        self.assertEqual(quant_conjugate.__str__(), "1.00 -2.00i -3.00j -4.00k")


class TestQuaternionNorm(unittest.TestCase):
    """
    Class to test Quaternion class Norm function with valid and invalid inputs.
    """
    def test_norm_valid(self):
        """
        function test Quaternion Norm with valid inputs.
        """
        quant1 = Quaternion(1, 2, 3, 4)
        quant_conjugate = quant1.norm()
        self.assertEqual(float(quant_conjugate), 5.477225575051661)

    def test_norm_invalid(self):
        """
        function test Quaternion Norm with invalid inputs.
        """
        with self.assertRaises(ValueError):
            quant1 = Quaternion()
            quant1.norm()


class TestQuaternionCreateReal(unittest.TestCase):
    """
    Class to test Quaternion class create real function with valid and invalid inputs.
    """
    def test_create_real_quarternion_valid(self):
        """
        function test Quaternion create real with valid inputs.
        """
        scalar = 3
        quant_scalar = Quaternion.create_real_quarternion(scalar=scalar)
        self.assertIsInstance(quant_scalar, Quaternion)
        self.assertEqual(quant_scalar.__str__(), "3.00 +0.00i +0.00j +0.00k")

    def test_create_real_quarternion_invalid(self):
        """
        function test Quaternion create real with invalid inputs.
        """
        with self.assertRaises(ValueError):
            Quaternion.create_real_quarternion(scalar="karam")


class TestQuaternionCreateMultipleReal(unittest.TestCase):
    """
    Class to test Quaternion class create multiple real function with valid and invalid inputs.
    """
    def test_create_multiple_real_quarternions_valid(self):
        """
        function test Quaternion create multiple real with valid inputs.
        """
        scalar_list = [1, 2, 3]
        quant_scalar_list = Quaternion.create_multiple_real_quarternions(
            scalar_list=scalar_list
        )
        self.assertIsInstance(quant_scalar_list, list)

    def test_create_multiple_real_quarternions_invalid(self):
        """
        function test Quaternion create multiple real with invalid inputs.
        """
        with self.assertRaises(ValueError):
            Quaternion.create_multiple_real_quarternions(scalar_list=[1, 2, "karam"])


if __name__ == "__main__":
    unittest.main()
