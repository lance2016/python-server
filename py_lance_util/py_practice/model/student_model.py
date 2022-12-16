# 导入:
from sqlalchemy import Column, Integer, String, DateTime, create_engine

from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from urllib.parse import quote

from py_lance_util.config.config_provider import get_config

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:


class student(Base):
    # 表的名字:
    __tablename__ = 'student'
    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(20))


class Test(Base):
    __tablename__ = 'test'
    id = Column(Integer, primary_key=True)
    m_id = Column(Integer)
    name = Column(String(255))
    identity_no = Column(String(30))
    address = Column(String(255))
    create_time = Column(DateTime, default=datetime.now)
    modify_time = Column(DateTime, onupdate=datetime.now, default=datetime.now)


# config = get_config()
# db_config = config.get_section("mysql")
# # 创建所有模型对应的表
# DB_URI = "mysql+pymysql://{username}:{password}@{hostname}:{port}/{database}".format(
#     username=db_config["user"],
#     password=quote(db_config["password"], '', "utf-8", None),
#     hostname=db_config["host"],
#     port=db_config["port"],
#     database=db_config["db_name"]
# )
# engine = create_engine(DB_URI, echo=True)
# engine = create_engine(DB_URI, echo=True)
# Base.metadata.create_all(engine)
