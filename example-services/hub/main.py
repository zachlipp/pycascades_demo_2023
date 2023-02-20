import os
from typing import Literal

import requests
from fastapi import FastAPI
from pydantic import BaseModel


class NumberContainer(BaseModel):
    number: float


def get_service_address(service: Literal["fizzer", "buzzer"]) -> str:
    scheme = "http"
    port_envvar = f"{service.upper()}_PORT"
    port = os.environ[port_envvar]
    return f"{scheme}://{service}:{port}"


def call_remote_service(
    number: float, service: Literal["fizzer", "buzzer"]
) -> bool:
    url = get_service_address(service)
    response = requests.post(url, json={"number": number})
    response_payload = response.json()
    return response_payload["result"]


app = FastAPI()


@app.post("/")
def fizzbuzz(nc: NumberContainer):
    number = nc.number
    print(number)
    fizz = call_remote_service(number, "fizzer")
    buzz = call_remote_service(number, "buzzer")
    if fizz and buzz:
        return  f"{number}: Fizzbuzz!"
    elif fizz:
        return f"{number}: Fizz!"
    elif buzz:
        return f"{number}: Buzz!"
    else:
        return f"{number}: :("
