Статус сервера

```ini
/srv/zookeeper/bin/zkServer.sh status
```

Статус кластера и нод
```ini
/opt/kafka/bin/kafka-broker-api-versions.sh --bootstrap-server $HOSTNAME:9092 --command-config /opt/kafka/config/admin.properties
```

Удалить topic
```ini
/opt/kafka/bin/kafka-topics.sh --bootstrap-server $HOSTNAME:9092 --command-config /opt/kafka/config/admin.properties --delete --topic ilt-integration.sla-payment
```

Партиции без лидеров
```ini
/opt/kafka/bin/kafka-topics.sh --bootstrap-server ${HOSTNAME}:9092 --command-config /opt/kafka/config/admin.properties --describe --unavailable-partitions
```

Показать конфигурацию топика
```ini
/opt/kafka/bin/kafka-topics.sh --bootstrap-server $HOSTNAME:9092 --command-config /opt/kafka/config/admin.properties --describe --topic pre-loanDataRequestResult
```

Партиции с числом синхр.реплик (ISR) ниже заданного
```ini
/opt/kafka/bin/kafka-topics.sh --bootstrap-server ${HOSTNAME}:9092 --command-config /opt/kafka/config/admin.properties --describe --under-min-isr-partitions
```

Партиции с числом синхр.реплик (ISR) на грани заданного
```ini
/opt/kafka/bin/kafka-topics.sh --bootstrap-server ${HOSTNAME}:9092 --command-config /opt/kafka/config/admin.properties --describe --at-min-isr-partitions
```

Все топики
```ini
/opt/kafka/bin/kafka-topics.sh --bootstrap-server $HOSTNAME:9092 --command-config /opt/kafka/config/admin.properties --list
```

Сообщения в топике
```ini
/opt/kafka/bin/kafka-console-consumer.sh --bootstrap-server $HOSTNAME:9092 --consumer.config /opt/kafka/config/admin.properties --topic lt-payment.import-1 --from-beginning
```

Написать в топик 
```ini
/opt/kafka/bin/kafka-console-producer.sh --broker-list $HOSTNAME:9092 --topic ilt-smgoz-log.import-payment-service --producer.config /opt/kafka/config/admin.properties
```

Показать ACL
```ini
/opt/kafka/bin/kafka-acls.sh --bootstrap-server $HOSTNAME:9092 --command-config /opt/kafka/config/admin.properties --list
```

Удалить ACL
```ini
/opt/kafka/bin/kafka-acls.sh --bootstrap-server $HOSTNAME:9092 --command-config /opt/kafka/config/admin.properties \
--remove --allow-principal "User:CN=smgoz-elst-vector,OU=DIT,O=Promsvyazbank Public Joint-Stock Company,L=Moscow,ST=Moscow,C=RU" \
--operation Read --operation Describe --topic 'lt-smgoz-audit.UCMFileCache-logs' --group 'vector-consumer'
```

Показать Consumer groups
```ini
/opt/kafka/bin/kafka-consumer-groups.sh --bootstrap-server $HOSTNAME:9092 --command-config /opt/kafka/config/admin.properties --all-groups --describe 
```

Добавить партиции в топик
```
/opt/kafka/bin/kafka-topics.sh --bootstrap-server $HOSTNAME:9092 --command-config /opt/kafka/config/admin.properties --alter --topic ilt-payment.import-2 --partitions 100
```

Количество сообщений в разеделе
```ini
/opt/kafka/bin/kafka-run-class.sh kafka.tools.DumpLogSegments --deep-iteration --print-data-log --files /srv/kafka/kafka-logs/ilt-payment.import-4-2/00000000000000011376.log | wc -l
```
```