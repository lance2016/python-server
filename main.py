from typing import Union
import uvicorn
from fastapi import FastAPI
from loguru import logger as log

app = FastAPI()


@app.get("/")
def read_root():
    log.info("你好")
    return {"Hello": "World2"}



@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    log.info(f"items:{item_id}")
    return {"item_id": item_id, "q": q}


if __name__=="__main__":
    log.info("server start")
    uvicorn.run("main:app", host="0.0.0.0", port=8004, reload=True)
