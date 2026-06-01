# Kafka: полезные команды

## Статус

Проверка ZooKeeper:

```bash
/srv/zookeeper/bin/zkServer.sh status
```

Состояние кластера и нод:

```bash
/opt/kafka/bin/kafka-broker-api-versions.sh \
	--bootstrap-server $HOSTNAME:9092 \
	--command-config /opt/kafka/config/admin.properties
```

## Работа с топиками

Удалить topic:

```bash
/opt/kafka/bin/kafka-topics.sh \
	--bootstrap-server $HOSTNAME:9092 \
	--command-config /opt/kafka/config/admin.properties \
	--delete --topic ilt-integration.sla-payment
```

Показать конфигурацию топика:

```bash
/opt/kafka/bin/kafka-topics.sh \
	--bootstrap-server $HOSTNAME:9092 \
	--command-config /opt/kafka/config/admin.properties \
	--describe --topic pre-loanDataRequestResult
```

Партиции без лидеров:

```bash
/opt/kafka/bin/kafka-topics.sh \
	--bootstrap-server ${HOSTNAME}:9092 \
	--command-config /opt/kafka/config/admin.properties \
	--describe --unavailable-partitions
```

Партиции с ISR ниже минимума:

```bash
/opt/kafka/bin/kafka-topics.sh \
	--bootstrap-server ${HOSTNAME}:9092 \
	--command-config /opt/kafka/config/admin.properties \
	--describe --under-min-isr-partitions
```

Партиции с ISR на грани минимума:

```bash
/opt/kafka/bin/kafka-topics.sh \
	--bootstrap-server ${HOSTNAME}:9092 \
	--command-config /opt/kafka/config/admin.properties \
	--describe --at-min-isr-partitions
```

Список топиков:

```bash
/opt/kafka/bin/kafka-topics.sh \
	--bootstrap-server $HOSTNAME:9092 \
	--command-config /opt/kafka/config/admin.properties \
	--list
```

Добавить партиции:

```bash
/opt/kafka/bin/kafka-topics.sh \
	--bootstrap-server $HOSTNAME:9092 \
	--command-config /opt/kafka/config/admin.properties \
	--alter --topic ilt-payment.import-2 --partitions 100
```

## Чтение/запись

Сообщения в топике:

```bash
/opt/kafka/bin/kafka-console-consumer.sh \
	--bootstrap-server $HOSTNAME:9092 \
	--consumer.config /opt/kafka/config/admin.properties \
	--topic lt-payment.import-1 --from-beginning
```

Записать в топик:

```bash
/opt/kafka/bin/kafka-console-producer.sh \
	--broker-list $HOSTNAME:9092 \
	--topic ilt-smgoz-log.import-payment-service \
	--producer.config /opt/kafka/config/admin.properties
```

## ACL и группы

Показать ACL:

```bash
/opt/kafka/bin/kafka-acls.sh \
	--bootstrap-server $HOSTNAME:9092 \
	--command-config /opt/kafka/config/admin.properties --list
```

Удалить ACL:

```bash
/opt/kafka/bin/kafka-acls.sh \
	--bootstrap-server $HOSTNAME:9092 \
	--command-config /opt/kafka/config/admin.properties \
	--remove \
	--allow-principal "User:CN=smgoz-elst-vector,OU=DIT,O=Promsvyazbank Public Joint-Stock Company,L=Moscow,ST=Moscow,C=RU" \
	--operation Read --operation Describe \
	--topic 'lt-smgoz-audit.UCMFileCache-logs' --group 'vector-consumer'
```

Показать consumer groups:

```bash
/opt/kafka/bin/kafka-consumer-groups.sh \
	--bootstrap-server $HOSTNAME:9092 \
	--command-config /opt/kafka/config/admin.properties \
	--all-groups --describe
```

## Диагностика

Количество сообщений в разделе:

```bash
/opt/kafka/bin/kafka-run-class.sh kafka.tools.DumpLogSegments \
	--deep-iteration --print-data-log \
	--files /srv/kafka/kafka-logs/ilt-payment.import-4-2/00000000000000011376.log | wc -l
```