from datetime import datetime
import random
from loguru import logger
from sqlalchemy import select, text
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
    # entity = engien.get(Test, id)
    db_exec = ''
    entity = engien.execute(db_exec).all()
    return entity


def search(engine: Session, params: dict):
    logger.info(params)

    # select_sql = f"select * from test where id =:id"
    # bind_sql = text(select_sql)
    # entity = engine.execute(bind_sql, params).fetchall()

    select_sql = f"select * from test where id ={params.get('id')}"
    return engine.execute(select_sql).all()
    return entity


def get_by_id(engine: Session, id: int):
    select_sql = f"select * from test where id ={id}"
    return engine.execute(select_sql).all()
