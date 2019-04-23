# Install kafka/zookeeper and start servers

```bash
brew install kafka
brew install zookeeper
zkServer start
kafka-server-start /usr/local/etc/kafka/server.properties
```

# Create a topic

```bash
kafka-topics --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic test
```

# Send a message

```bash
kafka-console-producer --broker-list localhost:9092 --topic test
>HELLO Kafka
```

# Receive a message

```bash
kafka-console-consumer --bootstrap-server localhost:9092 --topic test --from-beginning
```



# Confirm Topic List

➜  ~ kafka-topics --zookeeper localhost:2181 --list

➜  ~ kafka-topics --zookeeper localhost:2181 --topic test --describe