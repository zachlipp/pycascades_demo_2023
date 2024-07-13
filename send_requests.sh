#! /bin/bash
set -uo pipefail

send_request() {
  result=$(
    curl \
      -s \
      -X POST \
      localhost:6000 \
      -H "Content-Type: application/json" \
      -d '{"number":'${1}'}' \
  )
  echo "Sent ${1}, Received ${result}"
}

for i in {1..15}; do
  send_request $i
done
