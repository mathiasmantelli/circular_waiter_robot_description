#!/usr/bin/env python

import rospy
import time
from geometry_msgs.msg import PoseWithCovarianceStamped

def getNewPose(data):
    x = data.pose.pose.position.x
    y = data.pose.pose.position.y
    z = data.pose.pose.position.z
    rospy.loginfo("X: %s, Y: %s, Z: %s", x,y,z)

if __name__ == '__name__': 
    try:
        rospy.init_node('save_checkpoints', anonymous=True)
        get_robots_pose = rospy.Subscriber("/amcl_pose", PoseWithCovarianceStamped, getNewPose)
        time.sleep(2)

        rospy.spin()
    except rospy.ROSInternalException:
        rospy.loginfo("Node 'Save checkpoints' terminated.")

