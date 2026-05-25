# FRONT WEB

## NGINX

### Поконтурные согласования

| № пп | DEV | IDEV | IIFT | IFT | IHT | IPREPROD | IPROD | ITEST | HT | PREPROD | PROD | TEST |
|------|-----|------|------|-----|-----|----------|-------|-------|----|---------|------|------|
| п.п. 2.2.1., 3.2.1., 4.2.1. Необходимо настроить подробный аудит событий ИБ - 'log_format main' | [IBTASK-15135](https://jira.psbnk.msk.ru/browse/IBTASK-15135) | [IBTASK-15135](https://jira.psbnk.msk.ru/browse/IBTASK-15135) |  | [IBTASK-15135](https://jira.psbnk.msk.ru/browse/IBTASK-15135) | [IBTASK-15135](https://jira.psbnk.msk.ru/browse/IBTASK-15135) |  |  |  | [IBTASK-15135](https://jira.psbnk.msk.ru/browse/IBTASK-15135) | [IBTASK-15135](https://jira.psbnk.msk.ru/browse/IBTASK-15135) | [IBTASK-15135](https://jira.psbnk.msk.ru/browse/IBTASK-15135) |  |
| п.п. 2.4.4, 3.4.4, 4.4.4. Настроить лимит на максимальный размер буфера для URI - 'large_client_header_buffers' | [IBTASK-12145](https://jira.psbnk.msk.ru/browse/IBTASK-12145) | [IBTASK-12145](https://jira.psbnk.msk.ru/browse/IBTASK-12145) |  | [IBTASK-12602](https://jira.psbnk.msk.ru/browse/IBTASK-12602) | [IBTASK-12145](https://jira.psbnk.msk.ru/browse/IBTASK-12145) |  |  |  | [IBTASK-12145](https://jira.psbnk.msk.ru/browse/IBTASK-12145) | [IBTASK-12602](https://jira.psbnk.msk.ru/browse/IBTASK-12602) | [IBTASK-12145](https://jira.psbnk.msk.ru/browse/IBTASK-12145) | [IBTASK-12145](https://jira.psbnk.msk.ru/browse/IBTASK-12145) |
| п.2.4.9. Настроить заголовок 'Content Security Policy (CSP)' |  |  | [IBTASK-23224](https://jira.psbnk.msk.ru/browse/IBTASK-23224) | [IBTASK-24265](https://jira.psbnk.msk.ru/browse/IBTASK-24265) | [IBTASK-24265](https://jira.psbnk.msk.ru/browse/IBTASK-24265) | [IBTASK-23224](https://jira.psbnk.msk.ru/browse/IBTASK-23224) | [IBTASK-23224](https://jira.psbnk.msk.ru/browse/IBTASK-23224) | [IBTASK-23224](https://jira.psbnk.msk.ru/browse/IBTASK-23224) |  | [IBTASK-24265](https://jira.psbnk.msk.ru/browse/IBTASK-24265) |  |  |
| п.2.4.3.Настроить лимит по максимальному размеру тела запроса от клиента |  |  | [IBTASK-1997659](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$201514889:GMtask$PMibtask) |  |  |  |  |  |  |  |  |  |

### Общие согласования на все контура

<table>
<tr>
<th>пп №</th>
<th>Причина</th>
<th>IBTASK</th>
</tr>
<tr>
<td>п.п. 2.1.8, 3.1.7, 4.1.7. Каталог '/etc/nginx' и его файлы должны принадлежать пользователю root</td>
<td>Файл /etc/nginx/off меняет свои права из-за директивы error_log off в basic_status.conf.</td>
<td>

Согласовывается в рамках [IBTASK-1268675](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$113322890:GMtask$PMibtask)
</td>
</tr>
<tr>
<td>

* п.п. 2.2.2, 3.2.2, 4.2.2. Настроить ведение журнала доступа (access_log) - 'access_log off;'. 
* п.п. 2.2.2, 3.2.2, 4.2.2. Настроить ведение журнала доступа (access_log). 
* п.п. 2.2.3, 3.2.3, 4.2.3. Настроить ведение журнала ошибок (error_log) - 'error_log off;'
* п.п. 2.2.3, 3.2.3, 4.2.3. Настроить ведение журнала ошибок (error)
* п.2.4.6. Настроить заголовок 'X-Frame-Options'
* п.2.4.7. Настроить заголовок 'X-Content-Type-Options'
* п.2.4.8. Настроить заголовок 'X-XSS-Protection'
* п.2.4.9. Настроить заголовок 'Content Security Policy (CSP)'
</td>
<td>keepalive.conf</td>
<td>

[IBTASK-12597](https://jira.psbnk.msk.ru/browse/IBTASK-12597)
</td>
</tr>
<tr>
<td>

* п.п. 2.2.2, 3.2.2, 4.2.2. Настроить ведение журнала доступа (access_log) - 'access_log off;'. 
* п.п. 2.2.2, 3.2.2, 4.2.2. Настроить ведение журнала доступа (access_log). 
* п.п. 2.2.3, 3.2.3, 4.2.3. Настроить ведение журнала ошибок (error_log) - 'error_log off;'
* п.п. 2.2.3, 3.2.3, 4.2.3. Настроить ведение журнала ошибок (error)
* п.2.4.6. Настроить заголовок 'X-Frame-Options'
* п.2.4.7. Настроить заголовок 'X-Content-Type-Options'
* п.2.4.8. Настроить заголовок 'X-XSS-Protection'
* п.2.4.9. Настроить заголовок 'Content Security Policy (CSP)'
</td>
<td>basic.conf</td>
<td>

[IBTASK-18102](https://jira.psbnk.msk.ru/browse/IBTASK-18102) [IBTASK-12536](https://jira.psbnk.msk.ru/browse/IBTASK-12536)
</td>
</tr>
</table>

