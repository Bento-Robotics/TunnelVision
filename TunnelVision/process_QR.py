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

    def __init__(self, fd):
        super().__init__('barcode_reader')
        self.subscription = self.create_subscription(String, 'barcode', self.barcode_callback, 10)
        self.publisher_ = self.create_publisher(String, 'barcode_antiduplicate', 10)
        self.fd = fd

    def barcode_callback(self, msg):
        if msg.data not in self.barcodeText:
            self.get_logger().info('#%s ' % self.barcodeNo + msg.data)
            self.publisher_.publish(msg)
            self.barcodeText.append(msg.data)
            self.fd.write(f'#{self.barcodeNo} {msg.data}\n')
            self.fd.seek(len(msg.data) + 4)
            self.barcodeNo += 1


def main(args=None):

    if os.path.exists("qr_codes.txt"):
        os.remove("qr_codes.txt")
    fd = open("qr_codes.txt", "wt")

    try:
        rclpy.init(args=args)
        barcode_reader = BarcodeReader(fd)
        print('\033[0;32m###started####\033[0m')
        rclpy.spin(barcode_reader)

    # shut down cleanly
    except KeyboardInterrupt:
        pass
    except ExternalShutdownException:
        fd.close()
        sys.exit(1)

if __name__== '__main__':
    main()
