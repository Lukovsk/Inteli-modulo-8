from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import RegisterEventHandler, ExecuteProcess, IncludeLaunchDescription, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.event_handlers import OnProcessExit
from ament_index_python.packages import get_package_share_directory
import os
from random import randint


map_name = str(input("Name of the map: "))

def generate_launch_description():
    # primeiro, preciso lançar:
        # webots para ver o robot
        # o rvis para começar o mapeamento
        # o teleop_key para mapear
    # depois de fechar essas coisas:
        # salvo o mapa

    
    
    #ros2 launch webots_ros2_turtlebot robot_launch.py
        
    webots = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
        os.path.join(get_package_share_directory('webots_ros2_turtlebot'), 'launch'),
        '/robot_launch.py'])
    )
    
    #ros2 launch nav2_bringup tb3_simulation_launch.py slam:=True
    nav2 = IncludeLaunchDescription(
        PythonLaunchDescriptionSource([
            os.path.join(get_package_share_directory('nav2_bringup'), 'launch'),
            '/tb3_simulation_launch.py']),
        launch_arguments={'slam': 'True'}.items(),
    )

    teleop = Node(
        package="turtlebot3_teleop",
        executable="teleop_keyboard",
        output="screen",
        prefix="xterm -e"
    )
    
    
    # # ros2 run nav2_map_server map_saver_cli -f <caminho-arquivo-mapa>
    save_map = RegisterEventHandler(
        OnProcessExit(
            target_action=teleop,
            on_exit=[
                LogInfo(msg=("Closed teleop window, saving map.")),
                ExecuteProcess(
                    cmd=["ros2", "run", "nav2_map_server", "map_saver_cli", "-f", f"./maps/{map_name}"],
                    output="screen",
                    prefix="xterm -e"
                )
            ]
        )
    )
    
    return LaunchDescription([
        webots,
        nav2,
        teleop,
        save_map,
    ])