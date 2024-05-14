from typing import Optional

import uvicorn as uvicorn
from fastapi import FastAPI
from pydantic import BaseModel
from starlette.responses import JSONResponse

from src.trigger import trigger_message_printing, trigger_messaging

app = FastAPI()


class RequestBody(BaseModel):
    message: str
    number_of_times: Optional[int] = None
    stream: bool


@app.post("/api/my_project")
def sanjer_request(request_body: RequestBody):
    if request_body.stream:
        response = trigger_messaging(request_body)
    else:
        response = trigger_message_printing(request_body)
    return JSONResponse(
        status_code=200,
        content={"status": response}
    )


if __name__ == "__main__":
    uvicorn.run("main:app", host='0.0.0.0', port=15151, reload=True)

