from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import RegisterEventHandler, ExecuteProcess, IncludeLaunchDescription, LogInfo
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.event_handlers import OnExecutionComplete, OnProcessExit
from ament_index_python.packages import get_package_share_directory
import os

def generate_launch_description():
    # primeiro, preciso lançar:
        # webots para ver o robot
        # o rvis para começar o mapeamento
        # o teleop_key para mapear
    # depois de fechar essas coisas:
        # salvo o mapa
    # depois, lanço:
        # webots para ver o robot com o mapa
        # o rvis com o mapa feito
    
    
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
    
    map_name = "saved_map"
    
    # ros2 run nav2_map_server map_saver_cli -f <caminho-arquivo-mapa>
    save_map = RegisterEventHandler(
        OnProcessExit(
            target_action=webots,
            on_exit=[
                LogInfo(msg=("Closed turlte window")),
                ExecuteProcess(
                    cmd=[["ros2", "run", "nav2_map_server", "map_saver_cli", "-f", f"./{map_name}"]],
                    output="screen"
                )
            ]
        )
    )
    
    #lançar o webots novamente
    #ros2 launch webots_ros2_turtlebot robot_launch.py
    webots_again = RegisterEventHandler(
        OnExecutionComplete(
            target_action=save_map,
            on_completion=[
                LogInfo(msg=("Launching webots again")),
                ExecuteProcess(
                    cmd=[["ros2", "launch", "webots_ros2_turtlebot", "robot_launch.py"]],
                    output="screen"
                )
            ]
        )
    )
    
    #ros2 launch nav2_bringup tb3_simulation_launch.py map:=<arquivo-do-mapa>.yaml
    mapped_nav2 = RegisterEventHandler(
        OnExecutionComplete(
            target_action=save_map,
            on_completion=[
                LogInfo(msg=("Launching webots again")),
                ExecuteProcess(
                    cmd=[["ros2", "launch", "nav2_bringup", "tb3_simulation_launch.py", f"map:={map_name}.yaml"]],
                    output="screen"
                )
            ]
        )
    )
    
    return LaunchDescription([
        webots,
        nav2,
        teleop,
        save_map,
        webots_again,
        mapped_nav2,
    ])