#!/usr/bin/python3
import os
import rclpy
from rclpy.node import Node
from std_msgs.msg import String

# Fill in something for msg type imports
# from duckietown_msgs.msg import SOMETHING
# from std_msgs.msg import SOMETHING

class SkeletonNode(Node):
    def __init__(self):
        super().__init__('example_node')
        self.pub = self.create_publisher(String, 'chatter', 10)  # create publisher
        self.i = 0
        self.timer = self.create_timer(1.0, self.publish_msgs)

    def publish_msgs(self):
        msg = String()
        msg.data = 'Hello World' + f"{self.i}"
        self.pub.publish(msg)
        self.i += 1


def main():
    print('In main')
    rclpy.init()
    node = SkeletonNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
