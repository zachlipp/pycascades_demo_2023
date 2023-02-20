# FBaaS (Fizzbuzz as a Service)

A play on the popular programming challenge [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz), but with microservices because I have no shame.

Prepared for and referenced in my PyCascades 2023 talk "Implementing Distributed Tracing".

## Building and running
`docker-compose up --build`

## Using
```
for i in {1..15}; do curl \
  -X POST \
  localhost:6000 \
  -H "Content-Type: application/json" \
  -d '{"number":'${i}'}'; echo; done
```
