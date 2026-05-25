1. Скачать пакет с https://frmn-app.headoffice.psbank.local/pulp/content/PSB/Library/custom/opensource/rpm/Packages/i/
2. Скопировать на сервер
```
scp intelliJ-2021.2.4_x86_64.rpm $hst:/tmp
```
3. Установить пакет
```
sudo yum -y install /tmp/intelliJ-2021.2.4_x86_64.rpm
```
4. Для корректной работы IDEA необходимо установить корректные права для бинарников встроенной java
```
sudo chmod -R 755 /srv/intelliJ/jbr/bin/*
```
5. В пакете неправильной командой создаются бинарники idea (ln). Для корректной работы IDEA необходимо это исправить
```
sudo rm -f /bin/idea /usr/bin/idea
sudo ln -s /srv/intelliJ/bin/idea.sh /bin/idea
sudo ln -s /srv/intelliJ/bin/idea.sh /usr/bin/idea
```
6. Проверка
```
ls -l {/usr/bin,/bin}/idea
```