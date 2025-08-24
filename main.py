from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel
from scalar_fastapi.scalar_fastapi import get_scalar_api_reference

app = FastAPI()


class Item(BaseModel):
    name: str
    price: float
    is_offer: Union[bool, None] = None


# Expose Scalar API client at `/scalar`
@app.get("/scalar", include_in_schema=False)
async def scalar_html():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,  # type: ignore
        title=app.title,
        hide_client_button=True,
        hide_models=True,
    )


@app.get("/")
async def read_root():
    return {"message": "Hello World"}


@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id": item_id}


@app.put("/items/{item_id}")
async def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


@app.get("/users/me")
async def get_user_me():
    return {"user_id": "Current user"}


@app.get("/users/{user_id}")
async def get_user(user_id: str):
    return {"user_id": user_id}
