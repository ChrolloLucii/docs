# Consul: дерегистрация сервиса

## Важно перед дерегистрацией

1. Сервис должен быть в статусе `critical` (healthcheck не проходит).
2. Дерегистрация выполняется с агента, который регистрировал сервис.
3. Дерегистрация идет по **Service ID**, а не по имени сервиса.

## Как получить Service ID

### Через Web UI

Откройте `Services` -> выберите сервис -> найдите две записи на разных нодах. Название сервиса и порт в конце — это Service ID.

### Через API (catalog)

Список сервисов:

```bash
curl -H "X-consul-Token: bootstrap токен" \
    --cert "/srv/consul/ssl/$(hostname -s).cer" \
    --key "/srv/consul/ssl/$(hostname -s).key" \
    --cacert "/srv/consul/ssl/root.cer" \
    https://smgoz-cn-ift1:8501/v1/catalog/services/?pretty
```

Статус сервиса и Service ID:

```bash
curl -H "X-consul-Token: bootstrap токен" \
    --cert "/srv/consul/ssl/$(hostname -s).cer" \
    --key "/srv/consul/ssl/$(hostname -s).key" \
    --cacert "/srv/consul/ssl/root.cer" \
    https://smgoz-cn-ift1:8501/v1/catalog/service/psb-smgoz-jvm-service-authorization?pretty
```

Пример фрагмента ответа:

```json
{
    "ID": "secret",
    "Node": "smgoz-app-ift5.headoffice.psbank.local",
    "Address": "secret",
    "Datacenter": "smgoz-ift",
    "TaggedAddresses": {
        "lan": "secret",
        "lan_ipv4": "secret",
        "wan": "secret",
        "wan_ipv4": "secret"
    },
    "NodeMeta": {
        "consul-network-segment": "",
        "consul-version": "1.20.1"
    },
    "ServiceKind": "",
    "ServiceID": "psb-smgoz-jvm-service-authorization-38090",
    "ServiceName": "psb-smgoz-jvm-service-authorization"
}
```

## Экспорт переменных

```bash
export CONSUL_CACERT="/srv/consul/ssl/root.cer"
export CONSUL_CLIENT_CERT="/srv/consul/ssl/$(hostname -s).cer"
export CONSUL_CLIENT_KEY="/srv/consul/ssl/$(hostname -s).key"
export CONSUL_HTTP_TOKEN="bootstrap токен или токен с write на service-id"
export CONSUL_HTTP_ADDR="https://$(hostname):8501"
```

## Дерегистрация

Через CLI (может не сработать):

```bash
consul services deregister -id psb-smgoz-jvm-service-authorization-38090
```

Надежный вариант через API:

```bash
curl -X PUT -H "X-consul-Token: bootstrap" \
    --cert "/etc/consul/ssl/$(hostname -s).cer" \
    --key "/etc/consul/ssl/$(hostname -s).key" \
    --cacert "/etc/consul/ssl/root.cer" \
    https://<node>:8501/v1/agent/service/deregister/<service-id>
```