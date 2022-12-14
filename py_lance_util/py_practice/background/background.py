import threading
import time

from loguru import logger
from py_lance_util.config.config_provider import get_config


from utils.rabbitmq_util import RabbitMQ
config = get_config()
rabbitmq_config = config.get_section("rabbit_mq")
class MyThread(threading.Thread):
    def __init__(self, thread_id, name, counter):
        threading.Thread.__init__(self)
        self.thread_id = thread_id
        self.name = name
        self.counter = counter

    def run(self):
        print(f'Starting {self.name}')
        # 这里可以写要执行的任务代码
        rabbitmq_consume()
        print(f'Exiting {self.name}')


def rabbitmq_consume():
    try:
        logger.info("开始消费")
        # Create threads
        rmq = RabbitMQ(
            host=rabbitmq_config["host"],
            port=rabbitmq_config["port"],
            vhost=rabbitmq_config["vhost"],
            username=rabbitmq_config["user"],
            password=rabbitmq_config["password"]
        )
        print(rmq)
        # 声明一个队列
        queue = 'queue_hello'
        rmq.receive_message(
            queue=queue,
            callback=message_callback
        )
    except Exception as e:
        logger.error(f"comsumer exception{e}")
    finally:
        rmq.close()


# Define a callback function
def message_callback(channel, method, properties, body):
    time.sleep(1)
    logger.info(f'Received: {body.decode("utf-8")}')


def start_background_job():
    t1 = MyThread(1, "Thread-Comsumer", 1)
    t1.start()
