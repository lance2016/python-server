from fastapi import APIRouter, Depends
from api.middleware.oauth import token_is_true
from loguru import logger as log

from py_lance_util.config.config_provider import get_config


router = APIRouter(prefix="/main", tags=["main"], dependencies=[Depends(token_is_true)])


@router.get("/")
def read_root():
    log.info("你好,欢迎访问main服务")
    return {"code": "200", "success":True, "msg":"main service"}


def check_token(param_token):
    config = get_config()
    token = config.get_config("security","token")
    return token == param_token
        