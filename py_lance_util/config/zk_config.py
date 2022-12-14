from kazoo.client import KazooClient

from py_lance_util.config.config_provider import get_config

config = get_config()
zk = config.get_section("zookeeper")


def get_zk(ip=zk["host"], port=zk["port"]):
    client = KazooClient(hosts=f'{ip}:{port}')
    return client
