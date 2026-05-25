Convert cert to pem for VAULT

```ini
openssl x509 -inform der -in <certfile>.cer -out <certfile>.pem; done
```

MD5SUM

```ini
  openssl x509 -in ${cert} -noout -modulus | openssl md5
  openssl rsa -in ${key} -noout -modulus | openssl md5
```

COPY SSH-KEY

```ini
  hosts=
  read -s pass; for hst in ${hosts}; do sshpass -p ${pass} ssh-copy-id $hst ;done
```

TELNET

```ini
  host=''
  port=''
  (echo >/dev/tcp/$host/$port) &>/dev/null && echo "open" || echo "close"
```

AstraLinux Get URL

```ini
https_proxy=http://usrproxy.headoffice.psbank.local:8080 curl --proxy-negotiate -U : https://registry.red-soft.ru/v2/ubi7/ubi-minimal/tags/list -sk | jq
```

Ldapsearch
```ini
ldapsearch -H "ldaps://headoffice.psbank.local:636" -D "headoffice\rybakovvd" \
 -W -b "DC=headoffice,DC=psbank,DC=local" "(&(objectCategory=user)(mail=khalaknyu*))
```