# stdlib
from enum import Enum

# thirdparty
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# project
from settings import FUNCTION_MAP


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

