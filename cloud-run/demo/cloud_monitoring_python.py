from flask import Flask
import time
import random
from google.cloud import monitoring_v3

app = Flask(__name__)

# Initialize Google Cloud Monitoring client
client = monitoring_v3.MetricServiceClient()

# Sample product data for our online store
products = {
    '1': {'name': 'Product 1', 'price': 10.99},
    '2': {'name': 'Product 2', 'price': 19.99},
    '3': {'name': 'Product 3', 'price': 5.49}
}

@app.route('/')
def index():
    start_time = time.time()

    # Simulate processing time
    time.sleep(random.uniform(0.1, 0.5))

    # Log the page view metric to Google Cloud Monitoring
    log_metric('PageViews', 1)

    # Log the response time metric to Google Cloud Monitoring
    response_time = (time.time() - start_time) * 1000
    log_metric('ResponseTime', response_time)

    return "Welcome to our Online Store!"

@app.route('/product/<product_id>')
def product(product_id):
    start_time = time.time()

    # Simulate processing time
    time.sleep(random.uniform(0.2, 0.8))

    # Log the page view metric to Google Cloud Monitoring
    log_metric('PageViews', 1)

    # Log the response time metric to Google Cloud Monitoring
    response_time = (time.time() - start_time) * 1000
    log_metric('ResponseTime', response_time)

    if product_id in products:
        return f"Product: {products[product_id]['name']}, Price: ${products[product_id]['price']}"
    else:
        return "Product not found."

def log_metric(metric_name, value):
    # Send custom metric to Google Cloud Monitoring
    project_id = 'your-project-id'  # Replace with your Google Cloud project ID
    project_name = f"projects/{project_id}"
    series = monitoring_v3.types.TimeSeries()
    series.metric.type = f"custom.googleapis.com/{metric_name}"
    series.resource.type = "global"
    point = series.points.add()
    point.value.double_value = value
    now = time.time()
    point.interval.end_time.seconds = int(now)
    point.interval.end_time.nanos = int((now - point.interval.end_time.seconds) * 10**9)
    client.create_time_series(request={"name": project_name, "time_series": [series]})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
