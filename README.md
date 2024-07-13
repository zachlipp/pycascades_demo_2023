<pre align="center">
    _______            ____
   / __/ _ )___ ____ _/ __/
 / _// _  / _ `/ _ `/\ \
/_/ /____/\_,_/\_,_/___/

</pre>

# FBaaS (Fizzbuzz as a Service)

## 📝 Overview
Prepared for my PyCascades 2023 talk [*Implementing Distributed Tracing*](https://www.youtube.com/watch?v=hkYZDoIxE74), this project demonstrates how to trace HTTP requests in various Python web servers. It's a play on the popular programming challenge [FizzBuzz](https://en.wikipedia.org/wiki/Fizz_buzz) but implemented with microservices as a bit.

## 💥 Features
### 🔍 **Find bottlenecks from traces**
This project is primarily a reference implementation for implementing distributed tracing in Python. Users can send requests through and gauge their speed with Jaeger's UI.

### 💻 **Unnecessary microservices**
I needed an example distributed system to trace, and I had to keep an audience engaged for 20 minutes, so I came up with a goofy one.

## ⚡ Quick Start
- Clone this repository: `git clone https://github.com/zachlipp/pycascades_demo_2023.git`
- Build and run the servers (requires `docker`): `docker compose --profile tracing up -d --build`
- Send some requests with `./send_requests.sh`
- View the traces in Jaeger at [http://localhost:16686](http://localhost:16686)

## 🥁 Personal rating + reflection 🥁
<details open="">
<summary>Personal rating</summary>
<h3>❤️❤️❤️️❤️🖤 (4/5)</h3>
<h3>Reflection</h3>
<p>I made this repo for my first conference talk. My goal for the talk was to demystify distributed tracing in Python. I had been on several teams that had expressed interest in tracing, but none of them had delivered because it seemed too daunting. Once I had implemented it myself, I felt the straightforward path to traces, if presented correctly, wasn't very complicated at all. I had a theory that the right presentation of concepts and code examples could help more teams adopt (or at least evaluate!) this tool.</p>

<p>After my talk, a conference attendee approached me and shared she wished she had seen this presentation months ago as it would have saved her team weeks of effort - exactly my hope.</p>
</details>

## 🤗 Kudos
- The PyCascades 2023 organizers for the opportunity

