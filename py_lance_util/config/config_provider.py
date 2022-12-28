import configparser
from loguru import logger
import os
from functools import lru_cache
import nacos

ENV = os.getenv("env", "dev")
NACOS_ADDRESS = "49.234.42.199:8848"
NAMESPACE_ID = "py_lance"
GROUP = "DEV"
# !!!!此处namesace为Namespace ID
client = nacos.NacosClient(NACOS_ADDRESS, namespace=NAMESPACE_ID)


class ConfigProvider:

    def __init__(self, appname: str):
        self.config_data_id = f'{appname}_pro'
        logger.info(f'config_data_id: {self.config_data_id}')
        try:
            config_raw = client.get_config(self.config_data_id, group=GROUP)
            self.config = configparser.ConfigParser()
            self.config.read_string(config_raw)
            logger.info(f'config: {self.config}')
        except Exception as e:
            logger.error(f'get config failed: {e}')

    def get_config(self, section: str, key: str):
        return self.config[section][key]

    def get_section(self, section: str):
        return self.config[section]


@lru_cache()
def get_config(appname="py_server") -> ConfigProvider:
    return ConfigProvider(appname)


if __name__ == "__main__":
    config = get_config()
    rabbit_mq = config.get_section("rabbit_mq")
    print(rabbit_mq["user"])
    print(rabbit_mq["password"])
    print(rabbit_mq["host"])
