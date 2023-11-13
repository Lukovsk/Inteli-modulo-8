from launch import LaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
from launch.actions import IncludeLaunchDescription, ExecuteProcess
from launch_ros.actions import Node
import os



def generate_launch_description():
    # depois, lanço:
        # webots para ver o robot com o mapa
        # o rvis com o mapa feito
    
    #ros2 launch webots_ros2_turtlebot robot_launch.py
    webots = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory("webots_ros2_turtlebot"),
                        'launch'),
            '/robot_launch.py'
        ])
    )
    
    

    map_path = "./maps/saved_map"
    
    # ros2 launch nav2_bringup tb3_simulation_launch.py map:=<map_path>.yaml
    mapped_nav2 = ExecuteProcess(
        cmd=["ros2", "launch", "nav2_bringup", "tb3_simulation_launch.py", f"map:={map_path}.yaml"],
        output="screen",
        prefix="xterm -e"
    )
    
    waypoints = Node(
        package="pacote1",
        executable="node",
        output="screen",
        prefix="xterm -e"
    )
    
    delay = ExecuteProcess(
        cmd=["sleep", "5"],
        output="screen",
    )
    
    return LaunchDescription([
        webots,
        mapped_nav2,
        delay,
        waypoints
    ])