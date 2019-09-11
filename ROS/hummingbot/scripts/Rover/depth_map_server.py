#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Authors : Hasan Basri Aykol [basri@hummingdrone.co]

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from my_robot_msgs.srv import AddTwoImages
# from depth_map import disparity_map


def handle_add_two_images(req):
    """
    Gets the images from client, converts to OpenCV image format,
    generates and returns the disparity map.
    """
    result = req.imgL
    result2 = req.imgR
    try:
        left = bridge.imgmsg_to_cv2(result, 'bgr8')
        right = bridge.imgmsg_to_cv2(result2, 'bgr8')
    except CvBridgeError, e:
        print e
    # print(left.shape)
    # return(disparity_map(left,right))


if __name__ == '__main__':
    rospy.init_node("add_two_images_server")
    bridge = CvBridge()
    service = rospy.Service("/add_two_images", AddTwoImages, handle_add_two_images)
    rospy.spin()
