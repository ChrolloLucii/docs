# ceph

## Полезные команды.

Команда `ceph` и `radosgw-admin` может быть запущена на всех серверах кластера. AWS-cli находится обычно на первом мониторе или на любом другом где она была установлена(инструкция по установке ниже). Для работы `aws` необходим сетевой доступ к серверам RGW. 

- Посмотреть общее состояние кластера (с этого следует начинать диагностику)

  ```null
  ceph --cluster smgoz-ceph status
  ```
- Вывести значение параметра

  ```null
  ceph --cluster smgoz-ceph-iht config get client.rgw debug_rgw
  ```
- Установить значение параметра

  ```null
  ceph --cluster smgoz-ceph-iht config set client.rgw debug_rgw 10
  ```
- The zonegroup placement configuration can be queried with

  ```plaintext
  radosgw-admin --cluster smgoz-ceph-stest zonegroup get
  ```
- The zone placement configuration can be queried with

  ```plaintext
  radosgw-admin zone get
  ```
- Список пользователей

  ```plaintext
  radosgw-admin --cluster smgoz-ceph-stest user list
  ```
- Приостановить/включить пользователя

  ```plaintext
  radosgw-admin --cluster smgoz-ceph-stest user suspend  --uid dashboard
  ```

  ```plaintext
  radosgw-admin --cluster smgoz-ceph-stest user enable  --uid dashboard
  ```
- Информация о пользователе

  ```plaintext
  radosgw-admin --cluster smgoz-ceph-stest user info --uid idev-reconciliation | jq .keys
  ```
- Список политик для пользователя

  ```plaintext
  aws --ca-bundle=/etc/ceph/root2.pem --endpoint-url https://ismg-s3-stst.headoffice.psbank.local iam list-user-policies  --user-name sys_smgoz_storage_data_dev
  ```
- Получить политику по имени

  ```plaintext
  aws --ca-bundle=/etc/ceph/root2.pem --endpoint-url https://ismg-s3-stst.headoffice.psbank.local iam get-user-policy  --user-name sys_smgoz_storage_data_dev --policy-name sys-smgoz-storage-data-dev-ReadWrite
  ```
- Список buckets

  ```plaintext
  aws --ca-bundle=/etc/ceph/root2.pem --endpoint-url https://ismg-s3-stst.headoffice.psbank.local s3api list-buckets
  ```
- Удаление bucket

  ```plaintext
  aws --ca-bundle=/etc/ceph/root2.pem --endpoint-url https://ismg-s3-stst.headoffice.psbank.local s3api delete-bucket --bucket smgoz-dev-reports
  ```
- Удаление пользователя

  ```plaintext
  radosgw-admin --cluster smgoz-ceph-stest user rm --uid=sys_smgoz_storage_data_dev
  ```
- Копирование файла в bucket

  ```plaintext
  aws --ca-bundle=/etc/ceph/root2.pem --endpoint-url https://ismg-s3-stst.headoffice.psbank.local s3 cp test s3://smgoz-stest-storage-drp/test1/
  ```
- Удаление файлов в бакете рекурсивно
  - Проверка, удаление без фактического удаления

    ```plaintext
    aws --ca-bundle=/etc/ceph/root2.pem --endpoint-url https://ismg-s3-stst.headoffice.psbank.local s3 rm s3://idev-s3-bucket-tf-smgoz-service-ecmconnector/ --recursive --dryrun
    ```
  - Удаление рекурсивно

    ```plaintext
    aws --ca-bundle=/etc/ceph/root2.pem --endpoint-url https://ismg-s3-stst.headoffice.psbank.local s3 rm s3://idev-s3-bucket-tf-smgoz-service-ecmconnector/ --recursive
    ```

  Управление удалением может быть осуществлено через параметры --exclude "\*" --include "file1.txt" --include "file2.txt"
- Вывод объектов bucket

  ```plaintext
  aws --ca-bundle=/etc/ceph/root2.pem --endpoint-url https://ismg-s3-stst.headoffice.psbank.local s3 ls s3://smgoz-stest-storage-drp/test1/
  ```
- Вывод секретов пользователей ceph

  ```plaintext
  radosgw-admin --cluster smgoz-ceph-stest user list | jq .[] | xargs -I {} radosgw-admin --cluster smgoz-ceph-stest user info --uid {} | jq .keys
  ```
- Загрузка политики пользователя из файла.

  ```plaintext
  aws --ca-bundle=/etc/ceph/root2.pem --endpoint-url https://ismg-s3-stst.headoffice.psbank.local iam put-user-policy --user-name idev-templates --policy-name idev-templates-ReadDeleteWrite --policy-document file:///tmp/policy_idev-templates_ReadDeleteWrite.json
  ```

  Пример политики:

  ```plaintext
  cat /tmp/policy_idev-templates_ReadDeleteWrite.json 
  {
    "Version": "2012-10-17",
    "Statement": [
      {
        "Sid": "idev-templates-ReadDeleteWrite",
        "Effect": "Allow",
        "Action": ["s3:DeleteObject", "s3:GetObject", "s3:PutObject", "s3:GetObjectVersion"],
        "Resource": ["arn:aws:s3:::s3-bucket-tf-smgoz-service-templates", "arn:aws:s3:::s3-bucket-tf-smgoz-service-templates/*"]
      }
    ]
  }
  ```
- Переименование пользователя

  ```plaintext
  # radosgw-admin --cluster smgoz-ceph-stest user rename --uid=idev-ecmconnector --new-uid=idev-s3--tf-smgoz-jvm-service-ecmconnector
  ```
- Переименование бакета

  ```plaintext
  radosgw-admin --cluster smgoz-ceph-stest bucket link --bucket=s3-bucket-eisgoz-output --bucket-new-name=idev-s3-bucket-eisgoz-output --uid=defaultadmin
  ```

## Настройка aws-cli.

* Добавление учетной записи администратора и прав. Возможно для работы aws-cli права можно сократить.

  ```plaintext
  [root@ismg-mon1 ~]# radosgw-admin --cluster smgoz-ceph user create --uid=defaultadmin --display-name=defaultAdmin --admin
  
  [root@ismg-mon1 ~]# radosgw-admin --cluster smgoz-ceph caps add --uid=defaultadmin   --caps="users=*;buckets=*;roles=*;user-policy=*;roles=*;metadata=*;usage=*;zone=*;amz-cache=*;info=*;bilog=*;mdlog=*;datalog=*;oidc-provider=*;ratelimit=*"
  ```
* Настройка pip и установка пакета aws-cli:
  * установка пакета pip:

    ```plaintext
    [root@ismg-mon1 ~]# apt-get install pip
    ```
  * настройка pip на работу с nexus:

    ```plaintext
    [root@ismg-mon-stst01 ~]# cat .pip/pip.conf
    [global]
    trusted-host = nexus-external.psbnk.msk.ru
    index = https://nexus-external.psbnk.msk.ru:1443/repository/pypi.org-group/simple/
    index-url = https://nexus-external.psbnk.msk.ru:1443/index/python/simple
    ```

     Добавляем в `/etc/hosts`

    ```plaintext
    127.0.0.1       localhost.localdomain localhost nexus-external.psbnk.msk.ru
    ```

     C рабочей vdi поднимаем обратный туннель:

    ```plaintext
    $ ssh -R 1443:10.214.37.11:443 admgsv@headoffice@ismg-mon-sts01.headoffice.psbank.local
    ```
  * устанавливаем пакет awscli:

    ```plaintext
    [root@ismg-mon1 ~]# pip3 install awscli
    ```
  * убираем из `/etc/hosts` имя **nexus-external.psbnk.msk.ru**
* Настройка aws-cli

  ```plaintext
  [root@ismg-mon-stst01 ~]# cat .aws/config 
  [default]
  region = default
  
  [root@ismg-mon-stst01 ~]# cat .aws/credentials 
  [default]
  aws_access_key_id = <key-id>
  aws_secret_access_key = <access-key>
  ```
* проверка подключения:

  ```plaintext
  aws --ca-bundle=/etc/ceph/root2.pem --endpoint-url https://ismg-mon-stst01.headoffice.psbank.local:8443 s3api list-buckets
  ```