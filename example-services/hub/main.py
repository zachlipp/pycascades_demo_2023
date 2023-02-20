import os
from typing import Literal

import requests
from fastapi import FastAPI
from opentelemetry import trace
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry.instrumentation.fastapi import FastAPIInstrumentor
from opentelemetry.propagate import inject
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from pydantic import BaseModel

resource = Resource(attributes={"service.name": "hub"})

trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(endpoint="http://jaeger:4317", insecure=True)

span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)


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
    headers = {}
    inject(headers)
    url = get_service_address(service)
    response = requests.post(url, json={"number": number}, headers=headers)
    response_payload = response.json()
    return response_payload["result"]


app = FastAPI()
FastAPIInstrumentor.instrument_app(app)


@app.post("/")
def fizzbuzz(nc: NumberContainer):
    number = nc.number
    fizz = call_remote_service(number, "fizzer")
    buzz = call_remote_service(number, "buzzer")
    if fizz and buzz:
        return f"{number}: Fizzbuzz!"
    elif fizz:
        return f"{number}: Fizz!"
    elif buzz:
        return f"{number}: Buzz!"
    else:
        return f"{number}: :("
