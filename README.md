# Quaternion
The topic of this challenge is the implementation of a quaternions class in Python. In mathematics, the quaternion number system extends the complex numbers. A quaternion q is an expression of the form:

q = a + bi + cj + dk ; (1)

where a; b; c; d are real numbers and i; j; k are symbols that can be interpreted as unit-vectors pointing along the three spatial axes. The real part of a quaternion q is dened as: <(q) = <(a + bi + cj + dk) = a : (2)

for more details please refer to the Quaternion Programming challenge.pdf file

# Task

Use Python to implement a quaternion class called Quaternion with:
 suitable attributes which are set in the init function
 an addition according to equation (3) which is callable with +
 a function named scalar_multiplication according to equation (5) which takes scalar as an argument
 a function named real_part according to equation (2)
 a function named conjugate according to equation (6)
 a function named norm according to equation (7)
 a function named create_real_quarternion which takes an scalar argument called scalar and returns a quarternion with a = scalar ; b = c = d = 0.
 a function named create_multiple_real_quarternions which takes a list of scalars ( e.g [2, 4, 5] ) as argument ( scalar_list ) and returns a list of quarternions with a = scalar ; b = c = d = 0, where a for every quaternion
corresponds to the corresponding element in the input list.
 When calling print on a quaternion a + ib + jc + kd the output should be a + bi + cj + dk . If the quaternion is for example 1 + 2i + 3j + 4k the output should be 1 + 2i + 3j + 4k .

Create a second class called QuaternionHelper . This class should only have a single function perform_on_quaternion with the two arguments input_quaternion (a quaternion object) and action (a string). Possible values for action are: 'real_part', 'conjugate', 'norm', 'itself', 'triple'. For each of these values a
different action is to be triggered:

 real_part: print the real part of the input quaternion
 conjugate: print the conjugate of the input quaternion
 norm: print the norm of the input quaternion
 itself: print the input quaternion
 triple: print the result of multiplication of the input quaternion and 3
 other input: Raise an appropriate error.

# How to run

Precondition:
	Python 3 or above version must be installed
	Numpy python package must be installed
	
RUN Following commands to view the output of the assignment: python quaternionhelpertest.py
