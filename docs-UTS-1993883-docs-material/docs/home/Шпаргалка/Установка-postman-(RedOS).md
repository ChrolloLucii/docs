1. Скачать с nexus-external последнюю версию пакета postman - [https://nexus-external/#browse/search=keyword%3Dpostman](https://nexus-external/#browse/search=keyword%3Dpostman) - нам необходим архив tar.gz
```
scp postman-*.tar.gz  $hst:/tmp
```
2. Копируем архив на сервер и распаковываем в /srv
```
sudo tar xvfz /tmp/postman-*.tar.gz -C /srv/
```
3. Устанавливаем корректные права на самую свежую директорию /srv/postman-*
```
sudo chown -R root.root $(find /srv -maxdepth 1 -type d -name "postman*"| tail -n 1)
```
4. Проверка
```
stat $(find /srv -maxdepth 1 -type d -name "postman*"| tail -n 1)
```