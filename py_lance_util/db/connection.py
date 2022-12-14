import os
from urllib.parse import quote

from loguru import logger

from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

from py_lance_util.config.config_provider import get_config

# 数据库连接配置

config = get_config()
db_config = config.get_section("mysql")

engine = None


def init_connection():
    global engine
    # 用户名:密码@localhost:端口/数据库名
    DB_URI = "mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}".format(
        username=db_config["user"],
        password=quote(db_config["password"], '', "utf-8", None),
        hostname=db_config["host"],
        port=db_config["port"],
        database=db_config["db_name"]
    )
    engine = create_engine(DB_URI, echo=True)
    check_connection()
    logger.info("初始化连接数据库成功")


def check_connection():
    try:
        engine.connect()
    except Exception as e:
        print(f"数据库链接错误: {e}")
        os.abort()


def get_session():
    global engine
    if engine is None:
        init_connection()
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
