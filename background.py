from typing import Union
import uvicorn
from fastapi import FastAPI, APIRouter
from loguru import logger as log
import os
app = APIRouter(prefix="/start")


@app.post("/")
def read_root():
    log.info("github pushed, start exec auto_pull.sh")
    ret = os.system('sh /home/lance/python/python-server/sh/auto_pull.sh')
    print(f"finish: {ret}")
    print(f"status: {ret>>8}")
    return {"Hello": "World2"}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    log.info(f"items:{item_id}")
    return {"item_id": item_id, "q": q}


if __name__=="__main__":
    log.info("server start")
    uvicorn.run("main:app", host="0.0.0.0", port=18000, reload=True)
