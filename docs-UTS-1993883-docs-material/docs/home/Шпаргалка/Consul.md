:red_circle: Дерегистрация сервиса

Для того, чтобы сработала дерегистрация, нужно помнить 3 вещи.

1) Чтобы сработала дерегистрация сервис должен быть в статусе critical ( не должен проходить healthcheck)
2) Производить дерегистрацию надо с агента, с которого был зарегистрирован сервис
3) Дерегистрируется сервис по Service ID, а не по имени сервиса

Подготовка в дерегистрации

Первый способ через Web UI

Открываете services ----\> кликаете на имя сервиса ---\> И там будет 2 сервиса на разных нодах. Вот название сервиса и порт на конце и есть Service ID.

Второй способ через клиент.

:red_circle: Посмотреть список всех сервисов

```bash
curl -H "X-consul-Token: bootstrap токен" --cert "/srv/consul/ssl/$(hostname -s).cer" --key "/srv/consul/ssl/$(hostname -s).key" --cacert "/srv/consul/ssl/root.cer" https://smgoz-cn-ift1:8501/v1/catalog/services/?pretty 
```

:red_circle:Посмотреть статус сервиса и service-id

```bash
curl -H "X-consul-Token: bootstrap токен" --cert "/srv/consul/ssl/$(hostname -s).cer" --key "/srv/consul/ssl/$(hostname -s).key" --cacert "/srv/consul/ssl/root.cer" https://smgoz-cn-ift1:8501/v1/catalog/service/psb-smgoz-jvm-service-authorization?pretty`
```

где psb-smgoz-jvm-service-authorization - имя сервиса

В выводе нас интересует Service ID

Пример вывода

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

:red_circle: Тут самый сок, чтобы дерегистрировать сервис, ему нужен write на Service ID. То есть нам нужно давать write не только на service name, но и на service ID

Перед этим делаем

```bash
export CONSUL_CACERT="/srv/consul/ssl/root.cer"
export CONSUL_CLIENT_CERT="/srv/consul/ssl/$(hostname -s).cer"
export CONSUL_CLIENT_KEY="/srv/consul/ssl/$(hostname -s).key"
export CONSUL_HTTP_TOKEN="лучше bootstrap токен или токен с write на service-id"
export CONSUL_HTTP_ADDR="https://$(hostname):8501" ( тут имя консул сервера именно)
```

:red_circle: Выполняем саму команду дерегистрации :smiley_cat:

```bash
consul services deregister -id psb-smgoz-jvm-service-authorization-38090 # может не работать
```

Точно работает curl

```bash
curl -X PUT -H "X-consul-Token: bootstrap" --cert "/etc/consul/ssl/$(hostname -s).cer" --key "/etc/consul/ssl/$(hostname -s).key" --cacert "/etc/consul/ssl/root.cer" https://имя ноды, на котрой сервис:8501/v1/agent/service/deregister/ServiceID нужного сервиса
```