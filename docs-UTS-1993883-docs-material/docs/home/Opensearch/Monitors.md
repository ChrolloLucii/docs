# **Инструкция по настройке оповещения Opensearch**

Перед исполнение заявки инициаторам следует напомнить, что Monitor в Opensearch не являются системой мониторинга и Opensource не несет ответственность за него. Сообщения от них необходимо воспринимать строго в информационном порядке

<table>
<tr>
<th>№</th>
<th>Действие</th>
<th>Ответственное подразделение</th>
<th>Параметры</th>
<th>Комментарий</th>
</tr>
<tr>
<td>1</td>
<td>Заказать ТУЗ для почтовой рассылки</td>
<td>Сотрудник-инициатор задачи</td>
<td>

Login

Password
</td>
<td>После исполнения заявки ГУПД предоставят логин/пароль ТУЗ</td>
</tr>
<tr>
<td>2</td>
<td>Настройка postfix</td>
<td>ОАПЛ</td>
<td>

Создаем файл с учетными данными /etc/postfix/sasl_passwd формата:

* relay-int.psbank.ru   email:password

Выполняем команду

* postmap /etc/postfix/sasl_passwd

В конфиг postfix /etc/postfix/main.cf добавляем строки:

* smtp_sasl_auth_enable = yes
* smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
* smtp_sasl_security_options = noanonymous

5\. применяем конфиг

systemctl postfix reload
</td>
<td>

Организация доверия с почтовым сервером

[UTS-1952340](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$188524459:GMtask$PMsubivTask)
</td>
</tr>
<tr>
<td>3</td>
<td>Opensearch - Notification/Email senders</td>
<td>Opensource или Инициатор при наличии прав</td>
<td>

Имя

Email address - ТУЗ (с @)

Host - 127.0.0.1 - [localhost](http://localhost) указывается, так как передача сообщения будет через локальный postfix на сервере. У Opensearch нет возможности подключения к почтовому серверу с учетными данными

Port - 25 - Порт, на котором запущен локальный postfix.

Encryption method - None
</td>
<td>От кого будут отправляться уведомления</td>
</tr>
<tr>
<td>4</td>
<td>Opensearch - Notification/Email recipient groups</td>
<td>Opensource или Инициатор при наличии прав</td>
<td>

Name - Роль группы

Description - Описание

Emails - почтовые адреса сотрудников группы
</td>
<td>Кому будут отправляться уведомления</td>
</tr>
<tr>
<td>5</td>
<td>Opensearch - Notification/Chanells</td>
<td>Opensource или Инициатор при наличии прав</td>
<td>

Name - подходящее по смыслу название канала

Description - подробное описание

Channel Type - SMTP sender

SMTP sender - из пп.3

Default recipients - из пп.4
</td>
<td>Канал оповещений, который будет подключаться на уровне Monitors</td>
</tr>
<tr>
<td>6.1</td>
<td>Opensearch - Alerting/Monitors (для Opensource)</td>
<td>Opensource</td>
<td>

Monitor type - _Per cluster metrics monitor_

Monitor defining methost - любой удобный

Shedule - Частота запуска запроса (Frequency,Run every)

Select data - имя кластера

Query - Выбираем тип запроса

Triggers - имя триггера, уровень оповещения, условия срабатывания

Actions - Имя, канал из пп.5, Описание сообщение: тема и текст
</td>
<td>

Чтобы передать в сообщении какие-либо параметры из запроса Query необходимо его вызвать по следующему шаблону - {{ctx.results.0.\<имя параметра\>}}
</td>
</tr>
<tr>
<td>6.2</td>
<td>Opensearch - Alerting/Monitors (для остальных подразделений)</td>
<td>Opensource или Инициатор при наличии прав</td>
<td>

Monitor type - _Per cluster metrics monitor_

Monitor defining methost - любой удобный

Shedule - Частота запуска запроса (Frequency,Run every)

Select data - выбираем кластер, индекс, поле времени

Query - Метрики, за какой промежуток времени собрать, фильтр и группировка

Triggers - имя триггера, уровень оповещения, условия срабатывания

Actions - Имя, канал из пп.5, Описание сообщение: тема и текст
</td>
<td>

Пока не победил время.

Opensearch dashboard игнорирует системное время и отображает его в UTC 0 в переменных {{ctx.periodStart }} и {{ctx.periodEnd }}
</td>
</tr>
</table>

