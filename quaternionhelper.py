'''
This file contains the solution of Task 2: Python Programming Challenge - Quaternions
Developer: Karamjeet singh.
Version: 1.0.0
quaternionhelper.py -This file defines the QuaternionHelper class and its functions.
'''

from quaternion import Quaternion

class QuaternionHelper:
    '''
    Class to perform quaternion operation defined in the Quaternion class
    '''
    @staticmethod
    def perform_on_quaternion(input_quaternion, action):
        '''
        function takes input_quaternion and action as input
        and displays the output as per the action.
        '''
        if isinstance(input_quaternion, Quaternion):
            if action == "real_part":
                quat_real = Quaternion.real_part(input_quaternion)
                print(quat_real)
                return
            elif action == "conjugate":
                quat_conjugate = Quaternion.conjugate(input_quaternion)
                print(quat_conjugate)
                return
            elif action == "norm":
                quat_norm = Quaternion.norm(input_quaternion)
                print(quat_norm)
                return
            elif action == "itself":
                quat_itself = Quaternion.__str__(input_quaternion)
                print(quat_itself)
                return
            elif action == "triple":
                quat_triple = Quaternion.scalar_multiplication(input_quaternion, 3)
                print(quat_triple)
                return
            else:
                print("Undefined action, action can be real_part, conjugate  ")
        else:
            return "input quaternion is invalid"
            