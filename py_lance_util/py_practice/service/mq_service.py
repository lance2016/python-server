

from loguru import logger as log
from config.config import get_settings
from py_lance_util.config.config_provider import get_config
from utils.rabbitmq_util import RabbitMQ

config = get_config("dp-python-server")
rabbitmq_config = config.get_section("rabbit_mq")


def rabbitmq_produce(params: dict):
    try:
        # Create the RabbitMQ object
        rmq = RabbitMQ(
            host=rabbitmq_config["host"],
            port=rabbitmq_config["port"],
            vhost=rabbitmq_config["vhost"],
            username=rabbitmq_config["user"],
            password=rabbitmq_config["password"]
        )
        exchange = 'exchange_hello'
        queue = 'queue_hello'
        key = 'key_hello'
        rmq.bind_queue_exchange(queue=queue, exchange=exchange, routing_key=key)
        for item in params.get("msg"):
            rmq.public_msg(
                exchange=exchange,
                routing_key=key,
                json=item
            )
    except Exception as e:
        log.error(f"error:{e}")
    finally:
        rmq.close()
