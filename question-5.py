# stdlib
from __future__ import annotations

from enum import Enum

from fastapi import FastAPI
from fastapi import HTTPException
from pydantic import BaseModel

from settings import FUNCTION_MAP
# thirdparty
# project


app = FastAPI()


class AcceptableFunctionNames(Enum):
    send_email = 'send_email'
    process_data = 'process_data'


class WebhookDataSchema(BaseModel):
    function: AcceptableFunctionNames


class WebhookResponseSchema(BaseModel):
    status: str


@app.post('/Datalore', response_model=WebhookResponseSchema)
async def handle_webhook(data: WebhookDataSchema):
    function_name = data.function.value

    selected_function = FUNCTION_MAP.get(function_name)

    if selected_function:
        result = selected_function()
    else:
        raise HTTPException(status_code=400, detail='Unknown function')

    return result


# uvicorn question-5:app --reload для запуска приложения
