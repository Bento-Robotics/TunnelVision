from launch import LaunchDescription
from launch_ros.actions import Node
from launch.substitutions import PathJoinSubstitution
from launch_ros.substitutions import FindPackageShare

def generate_launch_description():
    return LaunchDescription([
        Node(
            package='usb_cam',
            namespace='Driver',
            executable='usb_cam_node_exe',
            name='CAM',
            parameters=[(PathJoinSubstitution([FindPackageShare('TunnelVision'), 'parameters', 'Driver_Camera.yaml']))]
        ),
        Node(
            package='usb_cam',
            namespace='CV',
            executable='usb_cam_node_exe',
            name='CAM',
            parameters=[(PathJoinSubstitution([FindPackageShare('TunnelVision'), 'parameters', 'CV_Camera.yaml']))]
        )
    ])
