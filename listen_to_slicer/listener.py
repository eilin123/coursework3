#!/usr/bin/env python
import rospy
import geometry_msgs.msg
from std_msgs.msg import String
from ros_igtl_bridge.msg import igtltransform 


def callback(data):
    rospy.loginfo("%0.2f is my x-coordinate,%0.2f is my y-coordinate,%0.2f is my z-coordinate,",data.transform.translation.x, data.transform.translation.y, data.transform.translation.z)

    
def listener():

    # In ROS, nodes are uniquely named. If two nodes with the same
    # name are launched, the previous one is kicked off. The
    # anonymous=True flag means that rospy will choose a unique
    # name for our 'listener' node so that multiple listeners can
    # run simultaneously.
    rospy.init_node('listener', anonymous=True, log_level=rospy.INFO)

    rospy.Subscriber('/IGTL_TRANSFORM_IN', igtltransform, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
