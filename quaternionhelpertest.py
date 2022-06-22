from quaternionhelper import QuaternionHelper
from quaternion import Quaternion

qs1 = Quaternion(3,5,4,8)

quanthelp1 = QuaternionHelper.perform_on_quaternion(qs1,"real_part")

quanthelp2 = QuaternionHelper.perform_on_quaternion(qs1,"conjugate")

quanthelp3 = QuaternionHelper.perform_on_quaternion(qs1,"norm")

quanthelp4 = QuaternionHelper.perform_on_quaternion(qs1,"itself")

quanthelp5 = QuaternionHelper.perform_on_quaternion(qs1,"triple")