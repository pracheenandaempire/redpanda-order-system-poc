from kafka import KafkaAdminClient
from kafka.admin import NewTopic
from kafka.admin import KafkaAdminClient, NewTopic

import logging 

class OrderAdmin:
    def __init__(self, brokers="localhost:9092"):
        """
        Initialize an OrderAdmin instance with specified Kafka brokers.
        """
        self.admin = KafkaAdminClient(bootstrap_servers=brokers)
       
    def topic_exists(self, topic_name="orders"):
        """
        Check if a topic with the given name exists in the Kafka server.
        """
        topics_metadata = self.admin.list_topics()
        return topic_name in topics_metadata
    
    def create_topic(self, topic_name="orders", num_partitions=3, replication_factor=3):
        """
        Create a new topic in Kafka with the specified name, number of partitions,
        and replication factor if it does not already exist.
        """
        if not self.topic_exists(topic_name):
            new_topic = NewTopic(name=topic_name, num_partitions=num_partitions, replication_factor=replication_factor)
            self.admin.create_topics([new_topic])
            logging.info(f"Topic {topic_name} created.")
        else:
            logging.info(f"Topic {topic_name} already exists.")
            
    def close(self):
        """
        Close the KafkaAdminClient connection.
        """
        self.admin.close()