import json
import time

from flask import Flask, make_response, request
from opentelemetry import trace
from opentelemetry.context import Context
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry.propagate import inject
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor
from opentelemetry.trace.propagation import tracecontext

FORMAT = tracecontext.TraceContextTextMapPropagator()

resource = Resource(attributes={"service.name": "fizzer"})

trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(endpoint="http://jaeger:4317", insecure=True)

span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)


app = Flask(__name__)


@app.route("/", methods=["POST"])
def fizz():
    traceparent = request.headers.get("traceparent")
    with tracer.start_as_current_span(
        "/", context=FORMAT.extract({"traceparent": traceparent})
    ) as fizzspan:
        headers = {"Content-Type": "application/json"}
        inject(headers)
        user_agent = request.headers.get("user-agent")
        fizzspan.set_attribute("http.user_agent", user_agent)
        time.sleep(0.5)
        x = request.json["number"]
        fizz = bool(x % 3 == 0)
        return make_response(json.dumps({"result": fizz}), 200, headers)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6001)
