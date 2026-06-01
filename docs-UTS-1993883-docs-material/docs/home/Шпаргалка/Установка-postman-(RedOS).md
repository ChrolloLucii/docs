# Установка Postman (RedOS)

## Шаги

1. Скачать последнюю версию с nexus-external (нужен архив `tar.gz`):

[https://nexus-external/#browse/search=keyword%3Dpostman](https://nexus-external/#browse/search=keyword%3Dpostman)

```bash
scp postman-*.tar.gz $hst:/tmp
```

2. Распаковать архив в `/srv`:

```bash
sudo tar xvfz /tmp/postman-*.tar.gz -C /srv/
```

3. Установить права на последнюю директорию `/srv/postman-*`:

```bash
sudo chown -R root.root $(find /srv -maxdepth 1 -type d -name "postman*" | tail -n 1)
```

4. Проверка:

```bash
stat $(find /srv -maxdepth 1 -type d -name "postman*" | tail -n 1)
```