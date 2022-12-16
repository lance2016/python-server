from datetime import datetime
import random
from loguru import logger
from sqlalchemy import select
from sqlalchemy.orm.session import Session

from py_lance_util.py_practice.model.student_model import Test


def generate_data(model, num):
    data_list = []
    for i in range(num):
        entity = model()
        entity.m_id = i
        entity.name = f"lance_{i}"
        entity.identity_no = f"no_{i}"
        entity.address = f"address_{i}"
        data_list.append(entity)
    return data_list


def batch_insert_data(engine: Session, insert_list):

    t0 = datetime.now()
    engine.bulk_save_objects(insert_list)
    # engine.execute(
    #     entity.__table__.insert(),
    #     insert_list
    # )  # ==> engine.execute('insert into ttable (name) values ("NAME"), ("NAME2")')
    print(
        f"SQLAlchemy Core: Total time for {len(insert_list)} records  {str(datetime.now() - t0)} secs")


def insert_into_table(engine: Session) -> Test:
    entity = Test()
    entity.address = "Beijing"
    entity.name = f"lance_{random.randint(1,100000)}"
    entity.create_time = datetime.now()
    entity.identity_no = random.randint(1, 100)
    engine.add(entity)
    engine.commit()
    return entity


def delete_data(engine: Session, id: int) -> int:
    row = engine.query(Test).filter(Test.id == 1).delete()
    engine.commit()
    logger.info(f"delete {row}")
    return row


def get_data(engien: Session, id: int) -> Test:
    entity = engien.get(Test, id)
    return entity


def search(engien: Session, params: dict):
    logger.info(params)
    # where_cond = " 1 = 1 "
    select_sql = select(Test)
    for key, val in params.items():
        logger.info(f"{key},{val}")
        select_sql = select_sql.where(getattr(Test, key) == val)
    entity = engien.execute(select_sql).first()
    logger.info(entity)
    return entity
    # entity = engien.search()
