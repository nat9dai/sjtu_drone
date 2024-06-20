import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription, DeclareLaunchArgument
from launch.launch_description_sources import PythonLaunchDescriptionSource

def generate_launch_description():
    use_gui = DeclareLaunchArgument('use_gui', default_value='true', description='Flag to enable or disable GUI')
    
    world_file = os.path.join(
        get_package_share_directory("sjtu_drone_description"),
        "worlds", "west_2_with_stuff.world"
    )

    pkg_gazebo_ros = get_package_share_directory('gazebo_ros')

    return LaunchDescription([
        use_gui,
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gzserver.launch.py')
            ),
            launch_arguments={'world': world_file}.items()
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(pkg_gazebo_ros, 'launch', 'gzclient.launch.py')
            ),
            launch_arguments={'verbose': 'true'}.items()
        ),
    ])
