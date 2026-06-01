# Logging v2: включение сбора логов для нового микросервиса

Инструкция для проекта 100780 ИЗ СМ ГОЗ по подключению логов микросервисов.

## Необходимая информация

- Название логической группы, в которую входит микросервис.
- Название микросервиса, совпадающее с контейнером Docker (без численного суффикса, если он есть).

## Логические группы микросервисов

Название топика логов формируется по формуле: `<contour>-microservices-logs.<group>`, где:

- `<contour>` — аббревиатура контура.
- `<group>` — логическая группа микросервиса.

### Перечень логических групп (30.06.2025)

| Логическая группа | Топик логов | Описание |
| --- | --- | --- |
| base | `<contour>-microservices-logs.base` | Микросервисы общего назначения |
| integration | `<contour>-microservices-logs.integration` | Микросервисы внешней интеграции |
| security | `<contour>-microservices-logs.security` | Микросервисы безопасности |
| gateway | `<contour>-microservices-logs.gateway` | Микросервисы шлюзов |

### При появлении новой логической группы

- Создать топик логов по формуле (параметры взять из аналогичных топиков).
- Выпустить сертификаты для Vector Log Agent на всех серверах группы. Рекомендуемый CN: `smgoz-<contour>-app-<group>-vector`.
- Выдать права продьюсера `Write + Describe` на топик для Principal сертификатов Vector Agent.
- Выдать права консьюмера `Read + Describe` на топик для Principal сертификатов Vector OpenSearch.
- Выдать права `Read + Describe` на consumer group `vector-consumer-<contour>-microservices-<group>-logs`.

## OpenSearch

### Права

Vector OpenSearch имеет только права записи в существующие индексы (создание индексов запрещено).

```yaml
opensearch_configuration_roles:
  app_vector:
    cluster_permissions:
      ...
    index_permissions:
      - allowed_actions:
        - index
        index_patterns:
          - "ilt-infra-logs.*"
          - "ilt-ms-logs.*"
```

### Index Lifecycle Policy

Убедитесь, что новые индексы попадают под правильную ILM/ISM-политику (rollover + удаление на непродовых контурах).

```yaml
opensearch_configuration_policies:
  - name: "1g-rollover-indexes"
    policy:
      description: "Жизненный цикл индексов с ролловером по 1Гб и удалением через 14 дней"
      default_state: "rollover"
      states:
        - name: "rollover"
          actions:
            - retry:
                count: 10
                backoff: "exponential"
                delay: "1m"
              rollover:
                min_size: "1gb"
                copy_alias: false
          transitions:
            - state_name: "delete"
              conditions:
                min_rollover_age: "14d"
        - name: "delete"
          actions:
            - retry:
                count: 10
                backoff: "exponential"
                delay: "1m"
              delete: {}
          transitions: []
      ism_template:
        - index_patterns:
            - "ilt-infra-logs.*"
            - "ilt-ms-logs.*"
          priority: 1
```

### Index Policy Templates

Добавьте новые шаблоны в `opensearch_configuration_rollover_index_template` и прогоните роль `opensearch-configuration` (>= 0.6.2).

```yaml
opensearch_configuration_rollover_index_template:
  - templates_list:
      - template_name: "ilt-ms-logs.base.smgoz-authorization-service"
      - template_name: "ilt-ms-logs.base.smgoz-file-router-service"
      - template_name: "ilt-ms-logs.base.smgoz-gateway-service"
      - template_name: "ilt-ms-logs.base.smgoz-import-payment-service"
      - template_name: "ilt-ms-logs.base.smgoz-journal-presenter-service"
      - template_name: "ilt-ms-logs.base.smgoz-loan-import-service"
      - template_name: "ilt-ms-logs.base.smgoz-loan-reporting-service"
      - template_name: "ilt-ms-logs.base.smgoz-reporting-service"
      - template_name: "ilt-ms-logs.base.psb-smgoz-jvm-service-controlconfiguration"
      - template_name: "ilt-ms-logs.integration.psb-smgoz-jvm-service-informaticaconnector"
      - template_name: "ilt-ms-logs.integration.smgoz-informatica-connector-service"
      - template_name: "ilt-ms-logs.integration.smgoz-mail-alert-service"
    composed_of:
      - "ms_logs_number_replicas"
      - "ms_logs_source_timestamp_in_date_nanos"
    priority: 100
```

### Алиасы и первичный индекс

Формула алиаса: `<contour>-ms-logs.<group>.<ms-name>`.

Первичный индекс: `<contour>-ms-logs.<group>.<ms-name>-000001`.

После применения Index Policy Templates:

- Индексы логов имеют численный суффикс.
- Первичный индекс должен быть создан вручную (Vector OpenSearch не может создавать индексы).
- Жизненный цикл регулируется ILM/ISM-политикой.

Для создания первичного индекса и alias выполните плейбук `smgoz_opensearch_configuration` с тегами `index_templates,create_rollover_index`.

### OpenSearch Dashboards

Пользователи с правами чтения могут создавать Index Patterns через `Dashboards Management -> Index Patterns`.

## Vector

Термины:

- **Vector OpenSearch** — получает сообщения из Kafka и пишет в OpenSearch.
- **Vector Agent** — читает JournalD, парсит и отправляет события в Kafka.

### Vector OpenSearch

Добавьте инклюд шаблона:

```yaml
vector_custom_conf_list:
  - { name: "kafka_microservices_logs" }
```

Пример параметризации (RTEST):

```yaml
template_kafka_microservices_logs:
  opensearch_healthcheck_enabled: false
  kafka_servers_string: "smgoz-kfk-rtst1.headoffice.psbank.local:9092,smgoz-kfk-rtst2.headoffice.psbank.local:9092"
  opensearch_servers:
    - "https://smgoz-ox-os-rt1:9200"
    - "https://smgoz-ox-os-rt2:9200"
    - "https://smgoz-ox-os-rt3:9200"
  contours:
    ftst:
      microservices_groups:
        base:
          topic: "ftst-microservices-logs.base"
        integration:
          topic: "ftst-microservices-logs.integration"
    ift:
      microservices_groups:
        base:
          topic: "ift-microservices-logs.base"
        integration:
          topic: "ift-microservices-logs.integration"
    pre:
      microservices_groups:
        base:
          topic: "pre-microservices-logs.base"
        integration:
          topic: "pre-microservices-logs.integration"
```

### Vector Agent

Добавьте инклюд шаблона:

```yaml
vector_custom_conf_list:
  - { name: "local_log_agent_v2" }
```

Пример параметризации (ILT):

```yaml
vector_template_vars:
  local_log_agent_v2:
    docker_user_id: "{{ getent_passwd['sys_docker'].1 }}"
    kafka_servers_string: "smgoz-ilkfk-lt1.headoffice.psbank.local:9092,smgoz-ilkfk-lt2.headoffice.psbank.local:9092,smgoz-ilkfk-lt3.headoffice.psbank.local:9092"
    logs_type: "java-plain-multiline"
    siem_address: "ptsiem-sm-log1.headoffice.psbank.local:514"

    microservices_groups:
      integration:
        topic: "ilt-microservices-logs.integration"
        microservices:
          psb-smgoz-jvm-service-informaticaconnector: {}
          smgoz-informatica-connector-service: {}
          smgoz-mail-alert-service: {}
```