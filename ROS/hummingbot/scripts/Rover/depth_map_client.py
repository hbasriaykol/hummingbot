#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Authors : Hasan Basri Aykol [basri@hummingdrone.co]

import rospy
import message_filters
import cv2
from my_robot_msgs.srv import AddTwoImages
from sensor_msgs.msg import Image
# from rover import action


CAMERA_TOPIC_NAME = '/hummingdrone_camera_1'
CAMERA_TOPIC_NAME_2 = '/hummingdrone_camera_2'


def callback(img, img2):
    """ Gets the images from Gazebo and sends to server """
    rospy.loginfo('Message received: \n%s' % (img.encoding))
    try:
        add_two_images = rospy.ServiceProxy("/add_two_images", AddTwoImages)
        response = add_two_images(img, img2)
        # Add an output here. Eg. action(response)
    except rospy.ServiceException as e:
        rospy.logwarn("Service failed: " + str(e))


if __name__ == '__main__':
    rospy.init_node("add_two_images_client")
    image_sub = message_filters.Subscriber(CAMERA_TOPIC_NAME, Image)
    image_sub_2 = message_filters.Subscriber(CAMERA_TOPIC_NAME_2, Image)
    ts = message_filters.TimeSynchronizer([image_sub, image_sub_2], 10)
    ts.registerCallback(callback)
    rospy.wait_for_service("/add_two_images")
    rospy.spin()
