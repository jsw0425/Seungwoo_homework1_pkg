import rclpy
from rclpy.node import Node

from seungwoo_interfaces.msg import SeungwooMessage


class SeungwooSubscriber(Node):

    def __init__(self):
        super().__init__('SeungwooSubscriber')

        self.subscription = self.create_subscription(
            SeungwooMessage,
            'SeungwooTopic',
            self.listener_callback,
            10
        )

    def listener_callback(self, msg):
        self.get_logger().info(
            f'수신: text="{msg.text}", '
            f'number={msg.number}, value={msg.value:.2f}'
        )


def main(args=None):
    rclpy.init(args=args)
    node = SeungwooSubscriber()

    try:
        rclpy.spin(node)
    except KeyboardInterrupt:
        pass
    finally:
        node.destroy_node()
        if rclpy.ok():
            rclpy.shutdown()


if __name__ == '__main__':
    main()
