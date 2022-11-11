from utils.send_simple_email import send_email
from typing import Union

import uvicorn
from fastapi import FastAPI
from loguru import logger as log
from config.config_parser import get_settings
security_setting = get_settings(("security",))
token = security_setting.get("token")
app = FastAPI()


@app.get("/")
def read_root():
    log.info("你好")
    return {"Hello": "World"}


@app.post("/email/", name="发送邮件")
def router_send_email(params: dict):
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

    result = send_email(title, content, receivers)

    if result == 'success':
        return {"code": 200, "message": "send successful"}
    else:
        return {"code": 400, "message": "send fail"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    log.info(f"items:{item_id}")
    return {"item_id": item_id, "q": q}


if __name__ == "__main__":
    log.info("server start")
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=True)
