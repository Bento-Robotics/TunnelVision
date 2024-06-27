from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='zbar_ros',
            executable='barcode_reader',
            name='barcode',
            parameters=[{'image_transport': 'compressed'}],
	    remappings=[('image', '/CV/image_raw'), ('barcode', '/CV/barcode')]
       ),
        Node(
            package='zbar_ros',
            executable='barcode_reader',
            name='barcode',
            parameters=[{'image_transport': 'compressed'}],
	    remappings=[('image', '/Driver/image_raw'), ('barcode', '/Driver/barcode')]
       ),
        Node(
            package='TunnelVision',
            executable='dual_process_QR',
            name='qr_antiduplicate',
            output='screen',
            emulate_tty=True,
       ),
    ])
