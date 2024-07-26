import json
import logging
from kafka import KafkaConsumer
from kafka.errors import KafkaError
import logging_config  

class OrderConsumer:
    def __init__(self, brokers="localhost:9092", topic="orders", group_id="demo-group"):
         """
        Initialize an OrderConsumer instance
        """
        self.consumer = KafkaConsumer(
            bootstrap_servers=brokers,
            group_id=group_id,
            auto_offset_reset="earliest",
            enable_auto_commit=False,
            consumer_timeout_ms=1000,
            value_deserializer=lambda m: json.loads(m.decode('ascii'))
        )
        self.topic = topic

    def consume_orders(self):
        """
        Consume and process messages from the Kafka topic, log the message information,
        and return the total number of processed messages.
        """
        self.consumer.subscribe([self.topic])
        msg_count = 0
        try:
            for message in self.consumer:
                msg_count+=1
                topic_info = f"Topic: {message.topic} Partition: {message.partition}| Offset: {message.offset}"
                message_info = f"Key: {message.key}, Value: {message.value}"
                print(f"{topic_info}, {message_info}")
            self.consumer.close()
            logging.info("Consumer closed")
            # self.consumer.commit(message)
        except KafkaError as e:
            logging.error(f"Error occurred while consuming messages: {e}")
        finally:
            self.consumer.close()
            logging.info("Consumer closed")
        return msg_count

if __name__ == "__main__":
    logging_config.configure_logging()
    
    topic = "orders"
    bootstrap_servers = ["localhost:19092", "localhost:29092", "localhost:39092",]
    
    # Assuming I already created the topic with OrderAdmin class
    # admin = OrderAdmin(bootstrap_servers)
    # admin.create_topic(topic)
    
    consumer = OrderConsumer(bootstrap_servers, topic)
    consumer.consume_orders()
