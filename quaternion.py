"""
This file contains the solution of Task 2: Python Programming Challenge - Quaternion
Developer: Karamjeet singh.
Version: 1.0.0
quaternion.py - This file defines the Quaternion class and its functions as per the Task 2
"""
from math import sqrt
import numpy as np


class Quaternion:
    """
    Class to create a quaternion q
    A quaternion q is an expression of the form: q = a + bi + cj + dk
    where a; b; c; d are real numbers and i; j; k are symbols that can be interpreted as
    unit-vectors pointing along the three spatial axes.
    """

    def __init__(self, *args, **kwargs):
        """
        Initialize the Quanterion object.
        the inputs should be
        Quaternion(1,2,3,4),
        Quaternion(5),
        Quaternion(scalar = 3)
        and Quaternion(np_array = [ 3.  6.  9. 12.])
        else raise exception
        """
        if len(args) == 1:
            try:
                self.q = self._is_valid_real(args[0], 1)
                return
            except Exception:
                raise ValueError("Invalid inputs, please enter real number")
        elif len(args) == 4:
            try:
                self.q = self._is_valid_real(args, 4)
                return
            except Exception:
                raise ValueError("Invalid inputs, please enter real number")
        elif kwargs and "scalar" in kwargs:
            scalar_val = kwargs.get("scalar", 0)
            self.q = self._is_valid_real(scalar_val, 1)
        elif kwargs and "np_array" in kwargs:
            np_array_val = kwargs["np_array"]
            self.q = self._is_valid_real(np_array_val, 4)
        else:
            raise ValueError("Invalid inputs, please enter real number")

    def _is_valid_real(self, num, size):
        """
        function to check input number/numbers are real number or not.
        if true:
            returns a numpy array of input number of type float
        else:
            raise exception
        """
        if size == 1:
            try:
                float_num = float(num)
                return np.array([float_num, 0.0, 0.0, 0.0])
            except Exception:
                raise ValueError("Invalid inputs, please enter real number")
        elif size == 4:
            try:
                return np.asarray(np.float_(num))
            except Exception:
                raise ValueError("Invalid inputs, please enter real number")
        else:
            raise Exception("Invalid length of the input args")

    def __addition__(self, quant_2):
        """
        function perform addition and returns sum of 2 quanterion as per the following
        equation: q1 + q2 = (a1 + b1i + c1j + d1k) + (a2 + b2i + c2j + d2k)
        = (a1 + a2) + (b1 + b2) i + (c1 + c2) j + (d1 + d2) k
        """
        if isinstance(quant_2, Quaternion):
            quant_sum = self.q + quant_2.q
            return self.__class__(np_array=quant_sum)
        else:
            raise ValueError("Invalid inputs, addition can be performed on 2 quanternion")

    def scalar_multiplication(self, scalar):
        """
        function perform and return multiplication of scalar with quanternion .
        Assumption: scalar must be an int type number in python.
        """
        if isinstance(scalar, int):
            quant_multi = np.multiply(self.q, scalar)
            return self.__class__(np_array=quant_multi)
        else:
            raise ValueError("Invalid inputs, scalar must be int number")

    def real_part(self):
        """
        function returns the real part of quanternion as per
        equation <(q) = <(a + bi + cj + dk) = a :
        """
        return self.q[0]

    def conjugate(self):
        """
        function returns the conjugation of a quaternion as per equation 6.
        """
        first, *rest = self.q
        quant_multi = np.multiply(rest, -1)
        quant_conj = np.hstack((first, quant_multi))
        return self.__class__(np_array=quant_conj)

    def norm(self):
        """
        function returns norm of a quaternion as per equation 7
        """
        return sqrt(np.sum(np.square(self.q)))

    @classmethod
    def create_real_quarternion(cls, scalar):
        """
        function takes scalar as input and returns quanternion .
        Assumption: scalar must be an int type number in python.
        """
        if isinstance(scalar, int):
            return cls(scalar=scalar)
        else:
            raise ValueError("Invalid inputs, scalar must be int number")

    @classmethod
    def create_multiple_real_quarternions(cls, scalar_list):
        """
        function takes list of scalar as input and returns list of quanternion .
        Assumption: scalar must be an int type number in python.
        """
        if isinstance(scalar_list, list):
            quanternion_list = []
            for scalar_element in scalar_list:
                if isinstance(scalar_element, int):
                    quanternion_list.append(cls(scalar=scalar_element))
                else:
                    raise ValueError("Invalid inputs, scalar must be int number")
            return quanternion_list
        else:
            raise ValueError("Invalid input, please enter list of scalar")

    def __str__(self):
        """
        function returns the string representation of the Quaternion object
        """
        return "{:.2f} {:+.2f}i {:+.2f}j {:+.2f}k".format(
            self.q[0], self.q[1], self.q[2], self.q[3]
        )
