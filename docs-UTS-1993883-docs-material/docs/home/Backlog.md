# Backlog

Единый список инициатив и технических задач проекта. Обновляйте статус по мере работы.

## Как пользоваться

- Заполняйте ответственного и ссылку на задачу.
- Для завершенных задач используйте статус "Исполнено" и при желании перечеркнутый текст.
- Если задача меняет статус или контур, правьте запись в этом списке.

## Список задач

| Тема | Ответственный | Статус | Ссылка / заметка |
| --- | --- | --- | --- |
| Observability. Поддержка JMX экспортер в виде Java Agent в ролях Galaxy для Java приложений. | — | — | [UTS-1255331](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$110478709) |
| Observability. Настроить мониторинг на графану. Может пойти как KTD на 4-й квартал. Необходимо будет с Ананичем согласовать порт экспортера на всех Opensource серверах, настроить экспортеры и настроить прометей и нарисовать графики. Длящееся задача. | — | — | — |
| Приведение iac opensearch к целевому виду ролевой модели. | @CHALYYSS | Ожидание ревизии smgoz__storage | [UTS-1929222](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$181621344) |
| ~~Pipeline для генерации сертификатов~~ | @DuminikNM | Исполнено | — |
| Ведение реестра выпущенных сертификатов для дальнейшего использования в отчетных документах | — | — | — |
| csr-generator. В случае замены сертификатов вытягивает серийники старых сертификатов | — | — | — |
| NGINX. Создание единого для всех контуров jinja-шаблона в разрезе обслуживаемого сервиса. Все расхождения по контурам должны отражаться только в IaC. | — | — | — |
| ~~Избавиться от prog_type в инвентаре~~ | @IsaevVV | Исполнено | — |
| Реализовать versionlock на устанавливаемое ПО. | — | — | — |
| Сделать дашбоард для отслеживания числа соединений по состояниям TIME_WAIT, CLOSE_WAIT, EST и проч. | @GolubevSV | — | — |
| Проработать установку JMX экспортеров для Kafka и на любое Java ПО | — | — | — |
| ~~На контуре iprod нужно проверить сертификаты для zookeeper app и при необходимости перевыпустить, добавив в них IP~~ | @GuschinAYU | Исполнено | [UTS-1278439](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$113898988) |
| ~~Перевести все метрик под МТЛС с помощью экспортер экспортера и внедрить фильтр CN только с сертом промета + allow.net~~ | @CHALYYSS | Исполнено | [UTS-1725912](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$153142632) |
| Обновить заббикс агент на версию 2.0 (ilt, lt, iift, rtest, ipreprod, itest, iprod). | — | — | — |
| ~~Почистить все упоминание ftest kafka-opensearch~~ | @GuschinAYU | Исполнено | [UTS-1766556](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$162581985:GMtask$PMsubivTask) |
| Создание динамического requirements.yml | @CHALYYSS | — | — |
| Доработать автоматизацию сбора версий ПО через pipeline и пуш в таблицы МТС нужных версий. Использовать apps_finder | @IsaevVV | — | — |
| Разработать систему бекапирования содержимого Consul сервера, дашбордов и настроек Grafana, возможно содержимое Keycloak через pipeline по шедулеру для восстановления в случае аварии. | — | — | — |
| Выставить одинаковые subuid/subgid для пользователя sys_docker для всех контуров внутри роли docker через объявление переменных | — | — | — |
| ~~Выставить ролью RO для директории /etc/opensearch/ssl в роли opensearch, чтобы директория не удалялась~~ | — | Исполнено | Оказалось дело в роли opensearch-configuration |
| Протестировать nginxlog экспортер и написать для него конфигурацию для кастомных логов в nginx (web_system_ui.access.log) | — | — | — |
| Написать post_task или доработать роль по деплою Keycloak плагина SPI (сейчас роль не генерирует keystore и не кладет его на место) | @GolubevSV | — | [UTS-1767327](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$162729434:GMtask$PMsubivTask) |
| Выпустить client cert для IHT Prometheus. Раскатать сертификаты и отключить insecure_skip_verify | — | — | — |
| node-exporter role: в check mode не работает - установка пакета и проверка статуса службы | — | — | — |
| IPREPROD. kafka-log - выпустить сертификаты, прописать ACL | — | — | — |
| IIFT. RTEST Prometheus -> IIFT exporters 9100. Схему дорисовали, ждем МСЭ. Все ПО настроено | На контроле у @CHALYYSS | В работе | — |
| ITEST. kafka-app. kafka-exporter - перевыпустить сертификаты (сейчас используются сертификаты Kafka), добавить ACL, удалить лишние ACL | — | — | — |
| PREPROD. kafka-app. kafka-exporter добавить ACL | — | — | — |
| Настройка glaber для базовых метрик сервисов и узлов, дашборд в Grafana, корректные оповещения | @GolubevSV | — | — |
| Перевести создание Consul токенов в IaC через роль | @CHALYYSS | Назначена | [UTS-1968015](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$192415641:GMtask$PMsubivTask) |
| Перейти на вторую версию роли kafka-cfg. Сократить записи по ACL (избавиться от Describe) | @VoronkovAA | — | — |
| Изучить реализацию мониторинга сертификатов с Ритейла (там без пользователя и sudo), но нет проверки клиентских сертификатов | — | — | [UTS-150628633](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$150628633) |
| Доработать автоматизацию по поиску сертификатов в Vault | @OreshkoVA | — | [Repo](https://ahcode/psb-private/devops-infrastructure/opensource-admins/projects/smgoz/scripts/scripts/-/tree/UTS-1739906_certs_info_exporter/export_cert_info?ref_type=heads)<br>[беклог_вольт.txt](uploads/a0abf33c666e549b11411ff6a5d66fbc/%D0%B1%D0%B5%D0%BA%D0%BB%D0%BE%D0%B3_%D0%B2%D0%BE%D0%BB%D1%8C%D1%82.txt) |
| Разобраться с fetch node data с Kafka по контуру IFT. Постоянно приходят отбивки от IFT по Kafka, нужно понять, что показывает триггер. | — | — | Триггер: `nodata(/smgoz-kfk-ift1.headoffice.psbank.local/jmx["kafka.network:type=SocketServer,name=NetworkProcessorAvgIdlePercent","Value"],{$KAFKA.JMX_TRIGGER_INTERVAL})=1` |
| Поправить отправку инфраструктурных логов с Keycloak (ошибка parse_timestamp при обработке) | — | — | Лог: `ERROR transform ... parse_timestamp ... conversion_failed` |
| Обновление роли haproxy в части обновления до определенной версии на AltLinux | @IsaevVV | Уже есть в роли | — |
| Аналитика и выравнивание subuid/sbgid sys_docker izsmgoz для docker rootless на всех контурах | — | — | — |
| Доработать автоматизацию сбора версий ПО через pipeline и пуш в таблицы МТС нужных версий. Использовать app_finder | @IsaevVV | — | [UTS-125867312](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$125867312) |
| Обновление инструкций для дежурной службы проекта СМ ГОЗ | @IsaevVV | — | — |
| Доработка роли докера (при удалении файлов override не делается daemon-reload и systemctl restart) | @CHALYYSS | — | [Job](https://ahcode/psb-private/devops-infrastructure/opensource-admins/projects/smgoz/playbooks/smgoz-app/-/jobs/50329800) |
| Доработка роли Keycloak в части выдачи корректных прав для модулей в srv/keycloak/providers/ | @GolubevSV | Назначена | [UTS-162729434](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$162729434) |
| Создание линтера для consul-cfg | — | — | — |
| Настроить доступ к ПО OpenSearch по отдельным группам | @IsaevVV | Назначена | [ITSM-1955000](https://itsm-web01.headoffice.psbank.local/sd?callNumber=1955000&page=imGeneral)<br>[UTS-207050449](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$207050449:GMtask$PMsubivTask) |
| Настроить доступ к ПО Grafana по отдельным группам | @IsaevVV | Назначена | [ITSM-1955023](https://itsm-web01.headoffice.psbank.local/sd?callNumber=1955023&page=imGeneral)<br>[UTS-207002430](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$207002430:GMtask$PMsubivTask!%7B%22tab%22:%22GMinfo%22%7D) |
| Настроить доступ к ПО Kafbat-ui по отдельным группам | — | — | [ITSM-1955067](https://itsm-web01.headoffice.psbank.local/sd?callNumber=1955067&page=imGeneral) |
| Увеличить количество одновременных инициализирующих шардов для OpenSearch | @GolubevSV | Назначена | [UTS-207050470](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$207050470:GMtask$PMsubivTask) |

