from flask import Flask
from prometheus_client import Counter, Histogram, generate_latest
import logging
import time
import random

app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Prometheus metrics
REQUEST_COUNT = Counter('http_requests_total', 'Total HTTP requests', ['method', 'endpoint', 'status'])
REQUEST_LATENCY = Histogram('http_request_duration_seconds', 'HTTP request latency', ['method', 'endpoint'])

@app.route('/')
def hello():
    start_time = time.time()
    logger.info("Handling request to /")
    # Simulate some processing
    time.sleep(random.uniform(0.1, 0.5))
    REQUEST_COUNT.labels(method='GET', endpoint='/', status='200').inc()
    REQUEST_LATENCY.labels(method='GET', endpoint='/').observe(time.time() - start_time)
    return 'Hello, World!'

@app.route('/metrics')
def metrics():
    return generate_latest()

@app.route('/error')
def error():
    logger.error("Simulated error occurred")
    REQUEST_COUNT.labels(method='GET', endpoint='/error', status='500').inc()
    raise Exception("Simulated error")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)