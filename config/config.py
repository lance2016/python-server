import json
import os
from functools import lru_cache

from pydantic import BaseSettings


class Settings(BaseSettings):
    token: str = ""
    static_log_root: str = ""
    mail_host: str = ""
    mail_user: str = ""
    mail_pass: str = ""
    sender: str = ""
    db_user: str = ""
    db_passwd: str = ""
    db_host: str = ""
    db_port: int = 3306
    db_name: str = ""

    class Config:
        CODE_BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        print(CODE_BASE)
        env_file = f"{CODE_BASE}/config/application.txt"
        env_file_encoding = 'utf-8'


@lru_cache()
def get_settings() -> Settings:
    return Settings()


def export_openapi_docs(open_api):
    # Change "openapi.json" to desired filename
    with open("static/app_openapi.json", "w") as file:
        json.dump(open_api, file)