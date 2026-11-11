import rclpy
from rclpy.node import Node

from seungwoo_interfaces.msg import SeungwooMessage


class SeungwooPublisher(Node):

    def __init__(self):
        super().__init__('SeungwooPublisher')

        self.publisher_ = self.create_publisher(
            SeungwooMessage,
            'SeungwooTopic',
            10
        )

        self.count = 0
        self.timer = self.create_timer(1.0, self.timer_callback)

    def timer_callback(self):
        msg = SeungwooMessage()

        msg.text = 'Hello from Seungwoo'
        msg.number = self.count
        msg.value = self.count * 0.1

        self.publisher_.publish(msg)

        self.get_logger().info(
            f'발행: text="{msg.text}", '
            f'number={msg.number}, value={msg.value:.2f}'
        )

        self.count += 1


def main(args=None):
    rclpy.init(args=args)
    node = SeungwooPublisher()

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
