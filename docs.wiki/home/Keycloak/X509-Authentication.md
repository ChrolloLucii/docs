# Общая схема передачи клиентского сертификата

[RFC9440](https://datatracker.ietf.org/doc/html/rfc9440) описывает имя и формат содержимого заголовка с клиентским сертификатом, передаваемым TTRP (TLS Terminating Reverse Proxy) в upstream, однако на данный момент предложенный формат не поддерживается [NGINX](https://github.com/nginx/nginx/issues/178), и Keycloak (выявлено экспериментально).

Принято решение использовать имя заголовка `X-Client-Cert`. При появлении полной поддержки со стороны NGINX и Keycloak рекомендуется придерживаться именования и формата, описанного в RFC9440.

На данный момент spi-x509cert для NGINX поддерживает формат содержимого заголовка `$ssl_client_escaped_cert` и не поддерживает `$ssl_client_cert` (выявлено экспериментально).

## Схема передачи заголовка

```plaintext
Client --[HTTPS]--> NGINX --[set_proxy_header X-Client-Cert $ssl_client_escaped_cert]--> Keycloak
```

# Параметры сервера Keycloak

[Опорная статья](https://www.keycloak.org/server/reverseproxy#\_enabling_client_certificate_lookup)

Необходимо запустить Keycloak со следующими параметрами:

```plaintext
--spi-x509cert-lookup-provider=nginx # тип используемого reverse-proxy, от которого зависят возможные форматы содержимого заголовка с сертификатом
--spi-x509cert-lookup-nginx-ssl-client-cert=X-Client-Cert # имя заголовка с сертификатом, передаваемого в upstream Keycloak
```

# Конфигурация NGINX TTRP

Единственным параметром конфигурации, обеспечивающим работоспособность схемы является:

```plaintext
proxy_set_header Client-Cert $ssl_client_escaped_cert;
```

в секции проксирования запросов в upstream Keycloak (обычно `location /auth`).

# Настройка Realm в Keycloak

Для реализации схемы внутри конкретного Realm Keycloak необходимо создать отдельный Client (здесь в терминологии Keycloak), отдельный Authentication Flow, и связать их друг с другом.

## Настройка X509 Direct Grant Flow

Необходимо создать кастомный Authentication Flow, который в дальнейшем будет использоваться в качестве Direct Grant Flow конкретного клиента.

![image](uploads/ae3f0e94a94b04929cf3e2254803fa0a/image.png) Authentication -\> Flows -\> Create Flow

![image](uploads/b39ab0b54931da94777a0a1bac1b8854/image.png) Задаём имя, оставляем Flow type: Basic Flow

![image](uploads/3ac2f28e361bcf61e05d092d2ee2d495/image.png) После создания: Add execution

![image](uploads/1423a0486ce85932eb88b170fe4cb100/image.png) Выбираем X509\\Validate Username (список длинный,необходимо нажать на следующую страницу).

![image](uploads/f9d2c678b85c2de63f6760acbc66d024/image.png) Переходим в Settings этого Step

![image](uploads/50bb18d0bc9ca1929d736a3364a96341/image.png) Придумываем alias, выбираем User Identity Source: Subject's Common Name так как для идентификации будет использоваться CN

![image](uploads/ac97a10d9a630bb915ae046ed61c6ac4/image.png) A regular expression to extract user identity остаётся по-умолчанию и захватывает весь CN целиком. User mapping method: Username or Email

В таком виде Flow полностью готов для использования.

## Настройка Client

Далее необходимо конкретному клиенту привязать новосозданный Authentication Flow в качестве Direct Grant Flow.

![image](uploads/e0feeca9cb41e7c76d267f695e5a86bb/image.png) Clients -\> \<клиент\> -\> Advanced

![image](uploads/0a4b4918875f25fd882656aec9246bd2/image.png) Clients -\\\> Authentication Flow Overrides где в Direct Grant Flow выбираем созданный ранее Authentication Flow

# Проверка работоспособности всей цепочки

```plaintext
curl -sqLk -X POST \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --cert ./client-crt.pem \
  --key ./client-key.pem \
  --data-urlencode 'grant_type=password' \
  --data-urlencode 'client_id=psb-auth' \
  --data-urlencode 'scope=openid' \
  "https://smgoz-ntg-idev4.headoffice.psbank.local:8080/auth/realms/dev-ext/protocol/openid-connect/token"
```

где в качестве адреса в URL используется адрес NGINX TTRP, `dev-ext` - название Realm, в `client_id` указан верный идентификатор Keycloak Client, а CN сертификата соответствует существующему в `dev-ext` пользователю.