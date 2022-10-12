#!/usr/bin/env python3
import rclpy
from rclpy.node import Node
from geometry.msgs.msgs import Twist

class MyCustomNode(Node): # MODIFY NAME
    def __init__(self):
        super().__init__("base_motor_controller") # MODIFY NAME

def main

