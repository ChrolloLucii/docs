<table>
<tr>
<th>Тема</th>
<th>Ответственный</th>
<th>Статус</th>
<th>Задача</th>
</tr>
<tr>
<td>

Observability. Поддержка JMX экспортер в виде Java Agent в ролях Galaxy для Java приложений. Анализ необходимости: [UTS-1255331](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$110478709)
</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>Observability. Настроить мониторинг на графану. Может пойти как KTD на 4-й квартал. Необходимо будет с Ананичем согласовать порт экспортера на всех Opensource серверах, настроить экспортеры и настроить прометей и нарисовать графики. Длящееся задача.</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>Приведение iac opensearch к целевому виду ролевой модели.</td>
<td>

@CHALYYSS
</td>
<td>Ожидание ревизии smgoz__storage</td>
<td>

[UTS-1929222](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$181621344)
</td>
</tr>
<tr>
<td>

~~Pipeline для генерации сертификатов~~
</td>
<td>

@DuminikNM
</td>
<td>Исполнено</td>
<td>

</td>
</tr>
<tr>
<td>Ведение реестра выпущенных сертификатов для дальнейшего использования в отчетных документах</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>csr-generator. В случае замены сертификатов вытягивает серийники старых сертфикатов</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>NGINX. Создание единого для всех контуров jinja-шаблона в разрезе обслуживаемого сервиса. Все расхождения по контурам должны отражаться только в IaC.</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>

~~Избавиться от prog_type в инвентаре~~
</td>
<td>

@IsaevVV
</td>
<td>Исполнено</td>
<td>

</td>
</tr>
<tr>
<td>Реализовать versionlock на устанавливаемое ПО.</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>Сделать дашбоард, для отслеживания числа соединений по состояниями TIME_WAILT, CLOSE_WAITE, EST, и проч.</td>
<td>

@GolubevSV
</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>Проработать установку jmx эксплортеров для кафка и на любое джава ПО</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>

~~На контуре iprod нужно проверить сертификаты для zookeeper app и при необходимости перевыпустить, добавив в них ip -~~
</td>
<td>

@GuschinAYU
</td>
<td>Исполнено</td>
<td>

[UTS-1278439](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$113898988)
</td>
</tr>
<tr>
<td>

~~Перевести все метрик под МТЛС с помощью экспортер экспортера и внедрит фильтр CN только с сертом промета + allow.net~~
</td>
<td>

@CHALYYSS
</td>
<td>Исполнено</td>
<td>

[UTS-1725912](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$153142632)
</td>
</tr>
<tr>
<td>Обновить заббикс агент на версию 2.0 ilt, lt, iift, rtest, ipreprod, itest, iprod контура.</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>

~~Почистить все упоминание ftest kafka-opensearch~~
</td>
<td>

@GuschinAYU
</td>
<td>Исполнено</td>
<td>

[UTS-1766556](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$162581985:GMtask$PMsubivTask)
</td>
</tr>
<tr>
<td>Создание динамического requirements.yml</td>
<td>

@CHALYYSS
</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>Доработать автоматизацию сбора версий ПО через pipeline и пуш в таблицы МТС нужных версий. Использовать apps_finder</td>
<td>

@IsaevVV
</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>Разработать систему бекапирования содержимого консул сервера, дашбордов и настроек графаны, возможно содержимое кейклок через pipeline по шедулеру для восстановления в случае аварии.</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>Выставить одинаковые subuid/subgid для пользователя sys_docker для всех контуров внутри роли docker через объявление переменных</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>

~~Выставить ролью RO для директориии /etc/opensearch/ssl в роли opensearch, чтобы директория не удалялась~~
</td>
<td>

</td>
<td>Исполнено</td>
<td>Оказалось дело в роли opensearch-configuration</td>
</tr>
<tr>
<td>Протестировать nginxlog экспортер и написать для него конфигурацию для кастомных логов в нашем nginx(web_system_ui.access.log)</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>Написать post_task или доработать роль по деплою Кейлок плагина spi. ( сейчас роль не генерирует keystore и не кладёт его на место)</td>
<td>

@GolubevSV
</td>
<td>

</td>
<td>

[UTS-1767327](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$162729434:GMtask$PMsubivTask)
</td>
</tr>
<tr>
<td>Выпустить client cert для IHT Prometheus. Раскатать сертификаты и отключить insecure_skip_verify</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>node-exporter role: в check mode не работает - установка пакета и проверка статуса службы</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>IPREPROD. kafka-log - выпустить сертификаты, прописать ACL</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>

IIFT. RTEST Prometheus -\> IIFT exporters 9100 - Схему дорисовали, ждем МСЭ. Все ПО настроено
</td>
<td>

На контроле у @CHALYYSS
</td>
<td>В работе</td>
<td>

</td>
</tr>
<tr>
<td>ITEST. kafka-app. kafka-exporter - перевыпустить сертификаты (сейчас используются сертификаты kafka), добавить ACL, удалить лишние ACL</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>PREPROD. kafka-app. kafka-exporter добавить ACL</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>

Настройка glaber для базовых метрик сервисов, узлов. Например доступность узлов, основные параметры загрузки памяти, ЦПУ, диска и т.д. Systemd статус основных сервисов узла. Статус который отдает сам сервис/кластер(если есть). На основании этого построить дашборд в графане глабера отражающий проблемы по контуру, статусы узлов и работающих на них сервисов.

Настроить оповещение, убрать оповещение о проблемах не относящихся к ЗО Opensource.
</td>
<td>

@GolubevSV
</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>

Перевести создание консул токенов в IAC через роль ([https://ahcode/psb-private/devops-infrastructure/opensource-admins/ansible-galaxy/deploy/consul-cfg](https://ahcode/psb-private/devops-infrastructure/opensource-admins/ansible-galaxy/deploy/consul-cfg))
</td>
<td>

@CHALYYSS
</td>
<td>Назначена</td>
<td>

[UTS-1968015](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$192415641:GMtask$PMsubivTask)
</td>
</tr>
<tr>
<td>Перейти на вторую версию роли kafka-cfg. Сократить записи по ACL ( избавиться от Describe)</td>
<td>

@VoronkovAA
</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>

Изучить реализацию мониторинга сертов с Ритейла ( там без пользователя и sudo) , но нет проверки клиентских сертов https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$150628633
</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>

Доработать автоматизацию по поиску сертов в Вольте

[https://ahcode/psb-private/devops-infrastructure/opensource-admins/projects/smgoz/scripts/scripts/-/tree/UTS-1739906_certs_info_exporter/export_cert_info?ref_type=heads](https://ahcode/psb-private/devops-infrastructure/opensource-admins/projects/smgoz/scripts/scripts/-/tree/UTS-1739906_certs_info_exporter/export_cert_info?ref_type=heads)

Полное описание -

[беклог\_вольт.txt](uploads/a0abf33c666e549b11411ff6a5d66fbc/%D0%B1%D0%B5%D0%BA%D0%BB%D0%BE%D0%B3\_%D0%B2%D0%BE%D0%BB%D1%8C%D1%82.txt)
</td>
<td>

@OreshkoVA
</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>

Разобраться с fetch node data с kafka по контуру IFT.

Постоянно приходят отбивки от ift по кафке, надо разобраться что показывает этот триггер.
</td>
<td>

</td>
<td>

</td>
<td>

Вот триггер, скорее всего надо время просить увеличивать

nodata(/smgoz-kfk-ift1.headoffice.psbank.local/jmx\["kafka.network:type=SocketServer,name=NetworkProcessorAvgIdlePercent","Value"\],{$KAFKA.JMX_TRIGGER_INTERVAL})=1
</td>
</tr>
<tr>
<td>

Поправить отправку инфраструктурных логов с Кейлок.

( ошибка - Apr 08 09:58:38 smgoz-app15.headoffice.psbank.local vector\[200572\]: 2026-04-08T06:58:38.022313Z ERROR transform{component_kind="transform" component_id=tf-keycloak-all component_type=remap}: vector::internal_events vector::internal_events::remap: Mapping failed with event. error="function call error for "parse_timestamp" at (179:240): unable to convert value to timestamp" error_type="conversion_failed" stage="processing" internal_log_rate_limit=true )
</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>Обновление роли haproxy в части обновления до определенной версии на altlinux</td>
<td>

@IsaevVV 
</td>
<td>Уже есть в роли</td>
<td>

</td>
</tr>
<tr>
<td>Аналитика и выравнивание subuid/sbgid sys_docker izsmgoz для docker rootles на всех контурах</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>

Доработать автоматизацию сбора версий ПО через pipeline и пуш в таблицы МТС нужных версий. Использовать app_finder(https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$125867312)
</td>
<td>

@IsaevVV
</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>Обновление инструкций для дежурной службы проекта СМ ГОЗ</td>
<td>

@IsaevVV
</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>

Доработка роли докера

([https://ahcode/psb-private/devops-infrastructure/opensource-admins/projects/smgoz/playbooks/smgoz-app/-/jobs/50329800](https://ahcode/psb-private/devops-infrastructure/opensource-admins/projects/smgoz/playbooks/smgoz-app/-/jobs/50329800) При удаление файлов override не делается daemon-reload и systemctl restart)
</td>
<td>

@CHALYYSS
</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>

Доработка роли keycloak в части выдачи корректных прав для модулей в srv/keycloak/providers/

Подробности в https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$197786412
</td>
<td>

@GolubevSV
</td>
<td>Назначена</td>
<td>

https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$162729434
</td>
</tr>
<tr>
<td>Создание линтера для consu-cfg</td>
<td>

</td>
<td>

</td>
<td>

</td>
</tr>
<tr>
<td>Настроить доступ к ПО Opensearch по отдельным группам</td>
<td>

@IsaevVV
</td>
<td>Назначена</td>
<td>

https://itsm-web01.headoffice.psbank.local/sd?callNumber=1955000&page=imGeneral ( [https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$`207050449:GMtask`$PMsubivTask](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$207050449:GMtask$PMsubivTask) )
</td>
</tr>
<tr>
<td>Настроить доступ к ПО Grafana по отдельным группам</td>
<td>

@IsaevVV
</td>
<td>Назначена</td>
<td>

https://itsm-web01.headoffice.psbank.local/sd?callNumber=1955023&page=imGeneral ( [https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$`207002430:GMtask`$PMsubivTask!%7B%22tab%22:%22GMinfo%22%7D](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$207002430:GMtask$PMsubivTask!%7B%22tab%22:%22GMinfo%22%7D) )
</td>
</tr>
<tr>
<td>Настроить доступ к ПО Kafbat-ui по отдельным группам</td>
<td>

</td>
<td>

</td>
<td>

https://itsm-web01.headoffice.psbank.local/sd?callNumber=1955067&page=imGeneral
</td>
</tr>
<tr>
<td>Увеличить количество одновременных инициализирующих шардов для Opensearch</td>
<td>

@GolubevSV
</td>
<td>Назначена</td>
<td>

[https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$`207050470:GMtask`$PMsubivTask](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$207050470:GMtask$PMsubivTask)
</td>
</tr>
</table>

