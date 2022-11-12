# 导入:
from sqlalchemy import Column, Integer, String

from sqlalchemy.ext.declarative import declarative_base

# 创建对象的基类:
Base = declarative_base()

# 定义User对象:


class student(Base):
    # 表的名字:
    __tablename__ = 'student'
    # 表的结构:
    id = Column(Integer, primary_key=True)
    name = Column(String(20))
