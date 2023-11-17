#! /bin/env python3
import rclpy
from rclpy.node import Node
from std_msgs.msg import String
import re

class CommandProcessor:
    def __init__(self):
        self.intentions = self._intentions()
        self.actions = self._actions()
    
    def process_command(self, msg: str):
        msg = msg.lower().strip()
        for intention, patterns in self.intentions.items():
            for pattern in patterns:
                match = re.match(pattern, msg, re.IGNORECASE)
                if match:
                    return self.actions[intention](match.group(len(match.groups())))

        return "Desculpe, não entendi."

    def bye(self, _):
        return "Tchau!"
    
    def greetings(self, _) -> str:
        return "Eae! Tudo bem? Como posso te ajudar?"
    
    def go_to_goal(self, goal) -> str:
        return f"Indo para {goal}"
    
    def _intentions(self):
        return {
            "greetings": [
                r"\b(?:(?:[Bb]o[am])\s(tarde|dia|noite))",
                r"\b(?:[Tt]udo)?\s?(?:(?:[Bb]em)|(?:[Bb]ão)|(?:[Ff]irme)|(?:em\sriba))",
                r"\b(?:[Oo](?:(?:l[aá])|(?:[iI]))(?:/!)?)|\b(?:[Ee]ae)"
            ],
            "exit": [
                r"\b(?:[Tt](?:[chau]))"
            ],
            "go_to_goal": [
                r"[Vv][áa]\s(?:pra|para)?\s?(?:[oaAO]\s|pr[oa]\s)?(?:me\s)?(.+)$",
                r"[Ll]eve\s(?:pra|para)?\s?(?:[oaAO]\s|pr[oa]\s)?(.+)$"
                ]
        }
    def _actions(self):
        return {
            "go_to_goal": lambda goal: self.go_to_goal(goal),
            "greetings": lambda _: self.greetings(_),
            "exit": lambda _: self.bye(_)
        }

class OutputNode(Node):
    def __init__(self, command_processor):
        super().__init__('output_node')
        self.command_processor = command_processor
        self.subscription_ = self.create_subscription(
            msg_type=String,
            topic="/chatbot",
            callback=self.listener_callback,
            qos_profile=10
        )
        
        self.get_logger().info("Estou te ouvindo!")
    def listener_callback(self, msg):
        self.get_logger().info(f"Awnsering '{msg.data}' : ")
        response = self.command_processor.process_command(msg.data)
        print(f"[RESPONSE] [CHATBOT] {response}")
        if response == "Tchau!":
            exit()



def main(args=None):
    rclpy.init(args=args)
    command_processor = CommandProcessor()
    output_node = OutputNode(command_processor)
    
    rclpy.spin(output_node)
    
    output_node.destroy_node()
    rclpy.shutdown()

if __name__ == "__main__":
    main()