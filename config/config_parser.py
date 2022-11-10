from configparser import ConfigParser
import configparser
from functools import lru_cache
import json
import os


class ReadConfigFile(object):
    def read_config(self, section_list):
        conn = ConfigParser()
        file_path = os.path.join(os.path.abspath('.'), 'config/config.ini')
        if not os.path.exists(file_path):
            raise FileNotFoundError("文件不存在")

        conn.read(file_path)
        print(conn.items('email'))

        config = {}
        for section in section_list:
            config[section] = dict(conn.items(section))
        if len(section_list) == 1:
            return config[section_list[0]]
        return config


rc = ReadConfigFile()


@lru_cache()
def get_settings(section_list: tuple) -> dict:
    return rc.read_config(section_list)
