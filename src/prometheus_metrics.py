from prometheus_client import start_http_server, Counter, Gauge
import random
import time

REQUESTS = Counter('my_app_requests_total', 'Total number of requests')
CPU_USAGE = Gauge('my_app_cpu_usage', 'Current CPU usage in percentage')
HTTP_RESPONSE_CODES = Counter('my_app_http_response_codes_total', 'HTTP response codes', ['status'])


def process_request():
    """request-ს ვიღებთ ვითომ (mockingი აქაც და ცპუშიც, ნამდვილი დატა არ გვაქვს)."""
    time.sleep(random.random())

def simulate_cpu_usage():
    """cpu."""
    return random.uniform(0, 100)

def simulate_response_code():
    """HTTP კოდების სიმულაცია (200 ან 500)."""
    if random.random() < 0.9:  # 90% შანსი მივცეთ 200ს დასაბრუნებლად
        HTTP_RESPONSE_CODES.labels(status="200").inc()
    else:
        HTTP_RESPONSE_CODES.labels(status="500").inc()
def run_app():
    """metrics localhost 800ზე."""
    start_http_server(8000)
    while True:
        process_request()
        simulate_response_code()
        REQUESTS.inc()
        CPU_USAGE.set(simulate_cpu_usage())

if __name__ == '__main__':
    run_app()
