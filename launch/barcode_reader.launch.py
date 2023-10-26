from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='zbar_ros',
            executable='barcode_reader',
            name='barcode',
            parameters=[{'image_transport': 'compressed'}],
	    remappings=[('image', '/CV/image_raw')]
       ),
        Node(
            package='TunnelVision',
            executable='Process_QR.py',
            name='qr_antiduplicate',
            output='screen',
            emulate_tty=True,
       ),
    ])
