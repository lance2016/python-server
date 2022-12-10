from fastapi import APIRouter, Depends
from api.middleware.oauth import token_is_true
from loguru import logger as log

from config.config import get_settings
from config.zk_config import get_zk
from db.connection import get_session
from py_practice.model.student_model import student, t1
from py_practice.service import main_service
from sqlalchemy.orm import sessionmaker

router = APIRouter(prefix="/main", tags=["main"], dependencies=[Depends(token_is_true)])

setting = get_settings()


@router.get("/")
def read_root():
    log.info("你好")
    return {"Hello": "World"}


@router.post("/email/", name="发送邮件")
def router_send_email(params: dict):
    token = setting.token
    param_token = params.get("token")
    print(token)
    if token != param_token:
        return {"code": 400, "message": "验证失败，无法发送邮件"}
    log.info(f"send email")
    receivers = params.get("receivers")
    if receivers is None or len(receivers) == 0:
        return {"code": 400, "message": "接收方邮件不能为空"}
    title = params.get("title", "default title")
    content = params.get("content", "default content")

    result = main_service.send_email(title, content, receivers)

    if result == 'success':
        return {"code": 200, "message": "send successful"}
    else:
        return {"code": 400, "message": "send fail"}


@router.get("/mysql/batch_insert/", name="批量插入")
def test_mysql(params: dict, db: sessionmaker = Depends(get_session)):
    if not check_token(params.get("token")):
        return {"code": 400, "message": "验证失败，无法发送邮件"}
    data_list = main_service.generate_data(t1, params.get("num", 10))
    main_service.batch_insert_data(db, data_list)
    db.commit()
    entity = db.query(t1).first()
    return {"t1": entity}


@router.get("/zk/", name="zookeeper")
def test_connect_zookeeper():
    zk = get_zk()
    zk.start()  # 与zookeeper连接
    print("exist", zk.exists("/abc"))
    print(zk.get("/abc"))
    node = zk.get_children('/')  # 查看根节点有多少个子节点
    print(type(node))
    zk.stop()  # 与zookeeper断开
    return node



@router.get("/produce/", name="rabbitmq")
def test_connect_rabbitmq(params: dict):
    if not check_token(params.get("token")):
        return {"code": 400, "message": "验证失败，无法发送邮件"}
    main_service.rabbitmq_produce(params)
    return {"code":200, "success": True, "msg":"发送成功"}


def check_token(param_token):
    token = setting.token
    return token == param_token
        