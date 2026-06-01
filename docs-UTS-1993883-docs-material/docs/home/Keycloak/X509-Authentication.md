# X.509 аутентификация в Keycloak через NGINX

Описание схемы передачи клиентского сертификата от NGINX (TLS Terminating Reverse Proxy) к Keycloak.

## Кратко

[RFC9440](https://datatracker.ietf.org/doc/html/rfc9440) описывает имя и формат заголовка с клиентским сертификатом, но текущие версии NGINX и Keycloak не поддерживают предложенный формат (подтверждено экспериментально). Для работы используется заголовок `X-Client-Cert` и значение `$ssl_client_escaped_cert`.

## Схема передачи заголовка

```plaintext
Client --[HTTPS]--> NGINX --[proxy_set_header X-Client-Cert $ssl_client_escaped_cert]--> Keycloak
```

## Параметры запуска Keycloak

[Опорная статья](https://www.keycloak.org/server/reverseproxy#_enabling_client_certificate_lookup)

```plaintext
--spi-x509cert-lookup-provider=nginx
--spi-x509cert-lookup-nginx-ssl-client-cert=X-Client-Cert
```

## Конфигурация NGINX (TTRP)

В секции проксирования запросов к Keycloak (обычно `location /auth`) добавьте:

```nginx
proxy_set_header X-Client-Cert $ssl_client_escaped_cert;
```

## Настройка Realm в Keycloak

Для работы схемы нужно создать отдельный Client и Authentication Flow и связать их.

### Настройка X509 Direct Grant Flow

![image](uploads/ae3f0e94a94b04929cf3e2254803fa0a/image.png) Authentication -> Flows -> Create Flow

![image](uploads/b39ab0b54931da94777a0a1bac1b8854/image.png) Задаем имя, оставляем Flow type: Basic Flow

![image](uploads/3ac2f28e361bcf61e05d092d2ee2d495/image.png) После создания: Add execution

![image](uploads/1423a0486ce85932eb88b170fe4cb100/image.png) Выбираем X509\Validate Username (список длинный, нужна следующая страница).

![image](uploads/f9d2c678b85c2de63f6760acbc66d024/image.png) Переходим в Settings этого Step

![image](uploads/50bb18d0bc9ca1929d736a3364a96341/image.png) Придумываем alias, выбираем User Identity Source: Subject's Common Name

![image](uploads/ac97a10d9a630bb915ae046ed61c6ac4/image.png) A regular expression to extract user identity остается по умолчанию и захватывает весь CN. User mapping method: Username or Email

### Настройка Client

![image](uploads/e0feeca9cb41e7c76d267f695e5a86bb/image.png) Clients -> <клиент> -> Advanced

![image](uploads/0a4b4918875f25fd882656aec9246bd2/image.png) Clients -> Authentication Flow Overrides, где в Direct Grant Flow выбираем созданный ранее Flow

## Проверка цепочки

```bash
curl -sqLk -X POST \
  --header 'Content-Type: application/x-www-form-urlencoded' \
  --cert ./client-crt.pem \
  --key ./client-key.pem \
  --data-urlencode 'grant_type=password' \
  --data-urlencode 'client_id=psb-auth' \
  --data-urlencode 'scope=openid' \
  "https://smgoz-ntg-idev4.headoffice.psbank.local:8080/auth/realms/dev-ext/protocol/openid-connect/token"
```

В URL используйте адрес NGINX TTRP; `dev-ext` — название Realm, `client_id` — идентификатор клиента Keycloak, CN сертификата должен соответствовать существующему пользователю Realm.