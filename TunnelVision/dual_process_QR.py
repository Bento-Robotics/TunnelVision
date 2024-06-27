#!/usr/bin/env python3

#_______         ____
#___/ _ )__________/ /_____
#__/ _ )/ -_)/ _ \/ __// _ )
#_/___/ \__//_//_/\__/(___/
# Bento Robotics zbar_ros QR code anti-duplicate logger

import os, rclpy
from rclpy.node import Node
from std_msgs.msg import String

class BarcodeReader(Node):
    barcodeText = []
    barcodeNo = 0

    def __init__(self):
        super().__init__('barcode_reader')
        self.subscription = self.create_subscription(String, '/CV/barcode', self.barcode_callback, 10)
        self.subscription = self.create_subscription(String, '/Driver/barcode', self.barcode_callback, 10)

    def barcode_callback(self, msg):
        if msg.data not in self.barcodeText:
            self.get_logger().info('#%s ' % self.barcodeNo + msg.data)
            self.barcodeText.append(msg.data)
            self.barcodeNo += 1

def main(args=None):
    try:
        rclpy.init(args=args)
        barcode_reader = BarcodeReader()
        print('\033[0;32m###started####\033[0m')
        rclpy.spin(barcode_reader)

    # shut down cleanly
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        sys.exit(1)

if __name__== '__main__':
    main()
