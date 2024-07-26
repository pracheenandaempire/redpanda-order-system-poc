import json
import logging
import logging_config
from admin import OrderAdmin

from kafka import KafkaProducer
from kafka.errors import KafkaError
from utils import load_data

class OrderProducer:
  def __init__(
    self, 
    brokers="localhost:9092", 
    topic="orders"
  ):
    """
    Initialize OrderProducer with Kafka brokers 
    """
    self.topic = topic
    self.brokers = brokers
    self.producer = KafkaProducer(
        bootstrap_servers = brokers,
        value_serializer=lambda m: json.dumps(m).encode('ascii')
    )
  
  def on_success(self, metadata):
    """
    Callback for successful message delivery to a Kafka topic.
    """
    print(f"Message produced to topic '{metadata.topic}' at offset {metadata.offset}")

  def on_error(self, e):
    """
    Callback for errors encountered when sending a message.
    """
    log.error(f"Error sending message: {e}")

  def send_orders(
    self,
    orders
  ):
    """
      Send messages to the Kafka topic associated with orders.
    """
    for i in range(0, len(orders)):
      msg = orders[i]
      future = self.producer.send(self.topic, msg)
      future.add_callback(self.on_success)
      future.add_errback(self.on_error)
      
    self.producer.flush()
    self.producer.close()

if __name__ == "__main__":
  logging_config.configure_logging()
  
  topic = "orders"
  bootstrap_servers = "localhost:9092"
  
  admin = OrderAdmin(bootstrap_servers)
  producer = OrderProducer(bootstrap_servers, topic)
  admin.create_topic(topic)
  
  orders = load_data()
  producer.send_orders(orders)
  