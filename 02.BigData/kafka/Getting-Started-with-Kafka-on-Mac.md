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





토픽 삭제

kafka-topics.sh --delete --zookeeper localhost --topic __consumer_offsets



현재 열려있는 포트 확인하는 코멘드

netstat -Aan | grep <확인하고자 하는 포트> 9092



**※ netstat 응용**

netstat -na

  열려있는 모든 포트



netstat  -na | grep LISTEN

  LISTEN 되는 모든 포트



netstat  -na | grep ESTABLISHED | wc -l

  모든 서비스 동시 접속자 수



netstat  -na | grep *.9999  | grep ESTABLISHED | wc -l

  위 예시에 적은 포트의 동시 접속자수



netstat  -na | grep *.80 | grep ESTABLISHED | wc -l

  웹 동시 접속자 수



netstat  -na | grep *.1521| grep ESTABLISHED | wc -l 

  DB 동시 접속자 수

출처: 

https://sagittariusof85.tistory.com/346

 [낙서장]



lsof -n -i :9092 | grep LISTEN