# Установка IntelliJ IDEA (RedOS)

## Шаги

1. Скачать пакет:

```
https://frmn-app.headoffice.psbank.local/pulp/content/PSB/Library/custom/opensource/rpm/Packages/i/
```

2. Скопировать на сервер:

```bash
scp intelliJ-2021.2.4_x86_64.rpm $hst:/tmp
```

3. Установить пакет:

```bash
sudo yum -y install /tmp/intelliJ-2021.2.4_x86_64.rpm
```

4. Установить корректные права для бинарников встроенной Java:

```bash
sudo chmod -R 755 /srv/intelliJ/jbr/bin/*
```

5. Исправить бинарники `idea` (в пакете создаются некорректные `ln`):

```bash
sudo rm -f /bin/idea /usr/bin/idea
sudo ln -s /srv/intelliJ/bin/idea.sh /bin/idea
sudo ln -s /srv/intelliJ/bin/idea.sh /usr/bin/idea
```

6. Проверка:

```bash
ls -l {/usr/bin,/bin}/idea
```