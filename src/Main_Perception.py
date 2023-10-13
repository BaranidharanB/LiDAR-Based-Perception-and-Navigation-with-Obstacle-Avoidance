#!/usr/bin/env python3

# DISCLAIMER: I have deleted few parts of the code for my safety purpose


import math,random,numpy as np
import rospy
from geometry_msgs.msg import Point
from sensor_msgs.msg import LaserScan
from visualization_msgs.msg import Marker

rospy.init_node('my_node',anonymous=True)
rate=rospy.Rate(10)

def ransac(points):
  global publisher
  #print("here")
  global visual
  best_inlier_index = []
  k = 50
  for j in range(k):
    r1,r2 = random.sample(range(len(points)),2)
    x1,y1 = points[r1]
    x2,y2 = points[r2]
    a = y2 - y1
    b = x2 - x1
    #print("here")
    inlier_index = []
    for i in range(len(points)):
      if(r1 != i) and (r2 != i):
        #print("here")
        sqr = math.sqrt(a*a + b*b)
        if sqr == 0:
          sqr = 0.0001
        distance_pts = abs( a*(x1 - x3) - b*(y1 - y3)) / sqr #Calculating points in line formula
        if (distance_pts<0.1):
          inlier_index.append(i)
          #print("here")

    if (len(best_inlier_index) < len(inlier_index)):
      best_inlier_index = inlier_index





# visual.pose.orientation.z = math.radians(92) 

rospy.Subscriber("/front/scan",LaserScan,laserCallback)
rospy.spin()

