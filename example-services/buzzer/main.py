import json

from flask import Flask, make_response, request
from opentelemetry.exporter.otlp.proto.grpc.trace_exporter import (
    OTLPSpanExporter,
)
from opentelemetry import trace
from opentelemetry.propagate import inject
from opentelemetry.instrumentation.flask import FlaskInstrumentor
from opentelemetry.sdk.resources import Resource
from opentelemetry.sdk.trace import TracerProvider
from opentelemetry.sdk.trace.export import BatchSpanProcessor

resource = Resource(attributes={"service.name": "buzzer"})

trace.set_tracer_provider(TracerProvider(resource=resource))
tracer = trace.get_tracer(__name__)

otlp_exporter = OTLPSpanExporter(endpoint="http://jaeger:4317", insecure=True)

span_processor = BatchSpanProcessor(otlp_exporter)
trace.get_tracer_provider().add_span_processor(span_processor)


app = Flask(__name__)
FlaskInstrumentor().instrument_app(app)


@app.route("/", methods=["POST"])
def buzz():
    headers = {"Content-Type": "application/json"}
    inject(headers)
    x = request.json["number"]
    buzz = bool(x % 5 == 0)
    return make_response(json.dumps({"result": buzz}), 200, headers)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=6002)
