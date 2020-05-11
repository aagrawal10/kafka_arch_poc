- Clone https://github.com/wurstmeister/kafka-docker.git

Now working directory is like this
workspace
  - kafka-docker
  - kafka_arch_poc

- First start kafka-docker & create topics
  - cd kafka-docker && docker-compose up -d --scale kafka=2
  - ./start-kafka-shell.sh 192.168.2.105 192.168.2.105:2181
    - $KAFKA_HOME/bin/kafka-topics.sh --create --topic test_topic_faust --partitions 2 --zookeeper $ZK --replication-factor 1
    - $KAFKA_HOME/bin/kafka-topics.sh --create --topic test_topic_native_1 --partitions 2 --zookeeper $ZK --replication-factor 1
    - $KAFKA_HOME/bin/kafka-topics.sh --create --topic test_topic_native_2 --partitions 2 --zookeeper $ZK --replication-factor 1

- Now build and start kafka_arch_poc
  - Modify kafka_client.py to update broker URL
  - cd kafka_arch_poc && docker build -t kafka_arch_poc:latest . && docker-compose up
