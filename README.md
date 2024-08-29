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

### redpanda-1-node-client

To get started with the single-node RedPanda client:

1. First, install the required Python packages:

```bash
pip install -r requirements.txt
```

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

### redpanda-3-node-client


To get started with the single-node RedPanda client:

1. First, install the required Python packages:

```bash
pip install -r requirements.txt
```

2. Navigate to the project directory:

```bash
cd redpanda-3-node-client  # or redpanda-3-node-client
```

3. To use docker-compose tool to build and deploy, change Tiltfile to look like this and run `tilt up`:

```
docker_build('producer', context='.', dockerfile='Dockerfile.producer')
docker_build('consumer', context='.', dockerfile='Dockerfile.consumer')

docker_compose('docker-compose.yml')
```

The current version uses Kubernetes, so simply run `tilt up`. 

Note: 
There is an error with using Tilt and Kubernetes that we have not been able to resolve:
`Failure during startup: std::runtime_error (vectorized internal rpc protocol - Error attempting to listen on {://10.105.137.128:33145:PLAINTEXT}: std::__1::system_error (error system:99, posix_listen failed for address 10.105.137.128:33145: Cannot assign requested address))`. 