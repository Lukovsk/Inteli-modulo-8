# webots.launch.py
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument, ExecuteProcess

def generate_launch_description():
    return LaunchDescription([
        DeclareLaunchArgument(
            'use_sim_time',
            default_value='true',
            description='Use simulation (Webots) clock if true'
        ),
        # Adicione outros argumentos conforme necessário

        # Adicione outras configurações e nós conforme necessário

        ExecuteProcess(
            cmd=["python3", "/caminho/para/seu/launch_webots.py"],  # Substitua pelo caminho real
            output='screen',
        ),
    ])