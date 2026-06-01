# Bash: полезные рецепты

## Конвертация сертификата в PEM для Vault

```bash
openssl x509 -inform der -in <certfile>.cer -out <certfile>.pem
```

## Проверка соответствия ключа и сертификата (MD5)

```bash
openssl x509 -in "${cert}" -noout -modulus | openssl md5
openssl rsa -in "${key}" -noout -modulus | openssl md5
```

## Копирование SSH ключа на список хостов

```bash
hosts=""
read -s pass
for hst in ${hosts}; do
  sshpass -p "${pass}" ssh-copy-id "${hst}"
done
```

## Проверка TCP порта

```bash
host=""
port=""
(echo >/dev/tcp/${host}/${port}) &>/dev/null && echo "open" || echo "close"
```

## AstraLinux: запрос списка тегов

```bash
https_proxy=http://usrproxy.headoffice.psbank.local:8080 \
  curl --proxy-negotiate -U : \
  https://registry.red-soft.ru/v2/ubi7/ubi-minimal/tags/list -sk | jq
```

## Ldapsearch

```bash
ldapsearch -H "ldaps://headoffice.psbank.local:636" \
  -D "headoffice\rybakovvd" \
  -W \
  -b "DC=headoffice,DC=psbank,DC=local" \
  "(&(objectCategory=user)(mail=khalaknyu*))"
```