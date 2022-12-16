from fastapi import APIRouter, Depends
from api.middleware.oauth import token_is_true
from common.response import Response
from db.connection import get_session
from py_practice.controller.main_controller import check_token
from sqlalchemy.orm.session import Session

from py_practice.model.student_model import Test
from py_practice.service import mysql_service

router = APIRouter(prefix="/mysql", tags=["mysql"], dependencies=[Depends(token_is_true)])


@router.post("/batch_insert/", name="批量插入")
def test_mysql(params: dict, db: Session = Depends(get_session)):
    if not check_token(params.get("token")):
        return Response.error(code=500, message="验证失败")
    num = params.get("num", 10)
    data_list = mysql_service.generate_data(Test, num)
    mysql_service.batch_insert_data(db, data_list)
    db.commit()
    entity = db.query(Test).first()
    return Response.success(data=entity, message=f"插入成功，共插入{num}条")


@router.post("/insert_one/", name="插入")
def insert_data(db: Session = Depends(get_session)):
    entity = mysql_service.insert_into_table(db)
    return Response.success(data=entity, message="插入成功")


@router.delete("/{id}/")
def delete_data_by_id(id: int, db: Session = Depends(get_session)):
    row = mysql_service.delete_data(db, id)
    return Response.success(data=row, message="删除成功")


@router.get("/get/{id}/", name="插入")
def insert_data(id: int, db: Session = Depends(get_session)):
    entity = mysql_service.get_data(db, id)
    return Response.success(data=entity, message="查询成功")


@router.post("/search/", name="搜索")
def search_data(params: dict, db: Session = Depends(get_session)):
    entity = mysql_service.search(db, params)
    return entity


@router.get("/get_by_id")
def get_by_id(id, db: Session = Depends(get_session)):
    entity = mysql_service.get_by_id(db, id)
    return entity
