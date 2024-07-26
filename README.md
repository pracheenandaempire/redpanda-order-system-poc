Copy markdown
# README.md for RedPanda Kafka Clients

This project contains two separate directories for Kafka clients, each configured to work with a different RedPanda setup: one with a single node and another with three nodes.

## Project Directory Structure

Below is an overview of each directory and a brief description of the files within them.

### redpanda-1-node-client

* **`admin.py`** - Manages Kafka topic creation and administration.
* **`benchmark.py`** - Provides benchmarking tools for performance testing.
* **`consumer.py`** - Consumes messages from a Kafka topic.
* **`db/`**
  * **`data.json`** - Contains sample data for Kafka messages.
  * **`data_builder.py`** - Generates data for testing purposes.
* **`docker-compose.yml`** - Docker Compose configuration for deploying a single-node RedPanda cluster.
* **`logging_config.py`** - Configures logging for the Kafka clients.
* **`producer.py`** - Produces messages to a Kafka topic.
* **`schema-registry.properties`** - Configuration for the schema registry.
* **`utils.py`** - Utility functions used by other scripts.

### redpanda-3-node-client

The structure and files in the `redpanda-3-node-client` directory are identical to those in the `redpanda-1-node-client` directory but are configured to work with a three-node RedPanda cluster setup.

## Getting Started

To get started with either the single-node or three-node RedPanda Kafka clients, follow these steps:

### Installation

First, install the required Python packages:

```bash
pip install -r requirements.txt
```

### Running the Clients

1. Choose the directory for the RedPanda cluster size you want to work with (redpanda-1-node-client for a single-node cluster or redpanda-3-node-client for a three-node cluster).

2. Navigate to the project directory:

```bash
cd redpanda-1-node-client  # or redpanda-3-node-client
```

3. Start the RedPanda cluster using Docker Compose:

```bash
docker-compose up -d
```

4. After the RedPanda cluster is up and running, produce events by running the producer.py script:

```bash
python producer.py
```

5. In a new terminal, consume events by running the consumer.py script:

```
python consumer.py
```
