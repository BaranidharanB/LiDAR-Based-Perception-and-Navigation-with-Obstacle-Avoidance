#!/usr/bin/env python3

# DISCLAIMER: I have deleted few parts of the code for my safety purpose


import math
import random
import rospy
from geometry_msgs.msg import Twist 
from sensor_msgs.msg import LaserScan
import numpy as np
rospy.init_node('bot2',anonymous=True)


pub = rospy.Publisher('/husky_velocity_controller/cmd_vel',Twist,queue_size=10)

rate=rospy.Rate(10)
drift= Twist()


initial_pt = rospy.get_param("/bot2/x")
print("initial_pt",initial_pt)
goal_pt = rospy.get_param("/bot2/y")
print("goal_pt",goal_pt)


def s(b):
    
    distance = np.sqrt((goal_pt[0] - initial_pt[0])**2 + (goal_pt[1] - initial_pt[1])**2)
    angle_of_line = np.atan2(())

    drift.pose.pose.positon.x = initial_pt[0]
    drift.pose.pose.positon.y = initial_pt[1]

    
rospy.Subscriber("/front/scan",LaserScan,scan)
rospy.spin()
