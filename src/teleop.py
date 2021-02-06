#!/usr/bin/env python3
import rospy
from gamepad_teleop import Gamepad_teleop
from geometry_msgs.msg import Vector3

class teleop(Gamepad_teleop):
    def __init__(self):
        super().__init__()
        rospy.init_node('pad')
        self.rate = rospy.Rate(10)
        self.pub = rospy.Publisher('command', Vector3, queue_size=10)

    def main(self):
        while not rospy.is_shutdown():
            pad_msg = Vector3()
            pad_msg.y = self.y
            pad_msg.x = self.x
            self.pub.publish(pad_msg)
            rospy.loginfo("x:{}, y:{}".format(pad_msg.x, pad_msg.y))
            self.rate.sleep()
        



if __name__=='__main__':
    pad = teleop()
    pad.loop_start()
    try:
        pad.main()

    except rospy.ROSInterruptException as e:
        print('error')
        print(e)

