# Настройка оповещений OpenSearch

!!! warning "Важно"
		Monitor в OpenSearch не являются системой мониторинга, Opensource не несет ответственность за них. Сообщения следует воспринимать в информационном порядке.

## 1. Заказать ТУЗ для почтовой рассылки

- Ответственный: сотрудник-инициатор задачи.
- Данные: логин и пароль ТУЗ.
- Комментарий: после исполнения заявки ГУПД предоставляет логин/пароль.

## 2. Настройка postfix

- Ответственный: ОАПЛ.
- Действия:

```bash
# /etc/postfix/sasl_passwd
relay-int.psbank.ru email:password

postmap /etc/postfix/sasl_passwd

# /etc/postfix/main.cf
smtp_sasl_auth_enable = yes
smtp_sasl_password_maps = hash:/etc/postfix/sasl_passwd
smtp_sasl_security_options = noanonymous

systemctl postfix reload
```

- Комментарий: организация доверия с почтовым сервером.
- Заявка: [UTS-1952340](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$188524459:GMtask$PMsubivTask).

## 3. OpenSearch: Notification / Email senders

- Ответственный: Opensource или инициатор при наличии прав.
- Параметры:
	- Name
	- Email address: ТУЗ (с @)
	- Host: `127.0.0.1` (локальный postfix)
	- Port: `25`
	- Encryption method: `None`
- Комментарий: от кого будут отправляться уведомления.

## 4. OpenSearch: Notification / Email recipient groups

- Ответственный: Opensource или инициатор при наличии прав.
- Параметры: Name, Description, Emails.
- Комментарий: кому будут отправляться уведомления.

## 5. OpenSearch: Notification / Channels

- Ответственный: Opensource или инициатор при наличии прав.
- Параметры:
	- Name и Description
	- Channel Type: SMTP sender
	- SMTP sender: из шага 3
	- Default recipients: из шага 4
- Комментарий: канал оповещений для Monitors.

## 6. OpenSearch: Alerting / Monitors

### 6.1 Для Opensource

- Monitor type: _Per cluster metrics monitor_
- Monitor defining method: любой удобный
- Schedule: частота запуска запроса (Frequency, Run every)
- Select data: имя кластера
- Query: тип запроса
- Triggers: имя триггера, уровень оповещения, условия
- Actions: имя, канал из шага 5, тема и текст

Для передачи параметров из Query используйте шаблон `{{ctx.results.0.<имя_параметра>}}`.

### 6.2 Для остальных подразделений

- Monitor type: _Per cluster metrics monitor_
- Monitor defining method: любой удобный
- Schedule: частота запуска запроса (Frequency, Run every)
- Select data: кластер, индекс, поле времени
- Query: метрики, период, фильтр и группировка
- Triggers: имя триггера, уровень оповещения, условия
- Actions: имя, канал из шага 5, тема и текст

OpenSearch Dashboards игнорирует системное время и отображает его в UTC 0 в переменных `{{ctx.periodStart}}` и `{{ctx.periodEnd}}`.

