import json
import time
from producer import OrderProducer
from consumer import OrderConsumer
from utils import load_data
import logging_config

# configure logging as per your setup
logging_config.configure_logging()


class BenchmarkProducer(OrderProducer):
    def send_orders(self, orders, bench=True):
        if bench:
            start_time = time.time()
        super().send_orders(orders)
        if bench:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Produced {len(orders)} messages in {elapsed_time:.2f} seconds.")
            if elapsed_time > 0:
                print(f"Average messages per second: {len(orders) / elapsed_time}")


class BenchmarkConsumer(OrderConsumer):
    def consume_orders(self, bench=True):
        message_count = 0
        start_time = time.time() if bench else None
        
        message_count = super().consume_orders()
        
        if bench:
            end_time = time.time()
            elapsed_time = end_time - start_time
            print(f"Consumed {message_count} messages in {elapsed_time:.2f} seconds.")
            if elapsed_time > 0:
                print(f"Average messages per second: {message_count / elapsed_time}")


def run_benchmark():
    topic = "orders"
    bootstrap_servers = ["localhost:19092", "localhost:29092", "localhost:39092",]

    # Benchmark Producer
    producer = BenchmarkProducer(bootstrap_servers, topic)
    orders = load_data()
    producer.send_orders(orders)

    # Benchmark Consumer
    consumer = BenchmarkConsumer(bootstrap_servers, topic)
    consumer.consume_orders()
    
if __name__ == "__main__":
    run_benchmark()