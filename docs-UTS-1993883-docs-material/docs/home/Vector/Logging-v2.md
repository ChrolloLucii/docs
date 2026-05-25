# 100780 ИЗ СМ ГОЗ Инструкция по включению сбора логов для нового микросервиса

## Необходимая информация

* Название логической группы, в которую входит новый микросервис.
* Название микросервиса в точности соответствующее названию контейнера Docker, в котором будет запущен микросервис без численного суффикса инстанса, если таковой имеется.

## Логические группы микросервисов

Название топика логов логической группы всегда формируется по формуле: `<contour>-microservices-logs.<group>`, где:

* \- аббревиатура контура на проекте 100780 ИЗ СМ ГОЗ
* \- название логической группы микросервиса

### Перечень логических групп микросервисов на 30.06.2025

| Название логической группы | Топик логов логической группы | Описание |
|----------------------------|-------------------------------|----------|
| base | \-microservices-logs.base | Микросервисы общего назначения; базовые |
| integration | \-microservices-logs.integration | Микросервисы внешней интеграции |
| security | \-microservices-logs.security | Микросервисы безопасности |
| gateway | \-microservices-logs.gateway | Микросервисы шлюзов? |

### При появлении новой логической группы микросервисов

* Создать топик логов для новой логической группы микросервисов согласно формуле. Список параметров взять из уже имеющихся аналогичных топиков или с другого контура, на котором Kafka логов обладает схожими характеристиками
* Выпустить сертификаты для Vector Log Agent для всех серверов, на которых будут располагаться микросервисы этой группы. При выпуске рекомендуется составлять CN по следующей формуле: `smgoz-<contour>-app-<group>-vector` (обсуждаемо).
* Выдать права продьюсера `Write + Describe` на топик для Principal сертификатов из предыдущего пункта.
* Выдать права консьюмера `Read + Describe` на топик для Principal сертификатов Vector OpenSearch, обслуживающих данный контур.
* Выдать или удостовериться в наличии прав `Read + Describe` на консьюмергруппу `vector-consumer-<contour>-microservices-<group>-logs` для Principal сертификатов Vector OpenSearch, обслуживающих данный контур.

## OpenSearch

### Права

Права на создание нового индекса у OpenSearch Vector отсуствуют - только на запись в уже существующие индексы.

#### Пример контура ILT

```plaintext
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

Необходимо убедиться, что новые индексы попадут под правильный Index Lifecycle Policy, которая обеспечивает своевременный rollover и удаление индексов на непродовых контурах.

#### Пример контура ILT

```plaintext
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

Для генерации Index Templates следует внести имена новых темплейтов в секцию `opensearch_configuration_rollover_index_template:` inventory, после чего прогнать роль `opensearch-configuration` начиная с версии `0.6.2`.

#### Пример контура ILT

```plaintext
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

Формула наименования алиасов: `<contour>-ms-logs.<group>.<ms-name>`, где:

* \- аббревиатура контура на проекте 100780 ИЗ СМ ГОЗ
* \- название логической группы микросервиса
* \- точное название контейнера микросервиса, без численного суффикса, определяющего конкретный экземпляр (если имеется)

Таким образом первичный индекс будет иметь имя: `<contour>-ms-logs.<group>.<ms-name>-000001`

**После применения Index Policy Templates**

* индексы логов для МС имеют численный суффикс
* первичный индекс должен быть предсоздан, у Vector OpenSearch нет прав на создание индексов МС
* жизненный цикл индексов, включая rollover, регулируется соответствующей Index Lifecycle Policy

Для создания первичного индекса и alias для записи, необходимо прогнать плейбук `smgoz_opensearch_configuration` с тэгами `index_templates,create_rollover_index`.

### OpenSearch Dashboards

Пользователи, имеющие права на просмотр индексов вольны создавать индекспаттерны OpenSearch Dashboards через раздел бокового меню `Dashboards Management -> Index Patterns` самостоятельно, как им удобно для работы.

## Vector

* Vector OpenSearch - сторона, принимающая сообщения из топиков Kafka, отправляющая документы в индексы OpenSearch
* Vector Agent - сторона, принимающая события из JournalD, производящая склейку, парсинг и отправку сообщений в Kafka

### Vector OpenSearch

В конфигурацию Vector OpenSearch должен быть добавлен инклюд шаблона файла конфигурации:

```yaml
vector_custom_conf_list:
  - { name: "kafka_microservices_logs" }
```

Шаблон должен быть параметризован следующим образом (на примере RTEST):

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

В конфигурацию Vector Agent должен быть добавлен инклюд шаблона файла конфигурации:

```yaml
vector_custom_conf_list:
  - { name: "local_log_agent_v2" }
```

Шаблон должен быть параметризован следующим образом (на примере ILT):

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