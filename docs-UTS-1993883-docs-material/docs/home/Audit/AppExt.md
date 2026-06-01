# APP EXT

Согласования по требованиям ИБ для компонентов APP EXT.

## Согласования по контурам

| Пункт | PREPROD |
| --- | --- |
| **2.4.4**. п.п. 2.4.4, 3.4.4, 4.4.4. Настроить лимит на максимальный размер буфера для URI - `large_client_header_buffers` | Согласовывается в рамках [IBTASK-1257958](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$110872881:GMtask$PMibtask) |

## Общие согласования на все контура

| Пункт | Причина | IBTASK |
| --- | --- | --- |
| п.п. 2.1.8, 3.1.7, 4.1.7. Каталог `/etc/nginx` и его файлы должны принадлежать пользователю root | Файл `/etc/nginx/off` меняет права из-за директивы `error_log off` в `basic_status.conf`. | Согласовывается в рамках [IBTASK-1268675](https://psbank.local) |
| - п.п. 2.2.2, 3.2.2, 4.2.2. Настроить ведение журнала доступа (access_log) - `access_log off;`<br>- п.п. 2.2.2, 3.2.2, 4.2.2. Настроить ведение журнала доступа (access_log)<br>- п.п. 2.2.3, 3.2.3, 4.2.3. Настроить ведение журнала ошибок (error_log) - `error_log off;`<br>- п.п. 2.2.3, 3.2.3, 4.2.3. Настроить ведение журнала ошибок (error_log)<br>- п.2.4.6. Настроить заголовок `X-Frame-Options`<br>- п.2.4.7. Настроить заголовок `X-Content-Type-Options`<br>- п.2.4.8. Настроить заголовок `X-XSS-Protection`<br>- п.2.4.9. Настроить заголовок `Content Security Policy (CSP)` | keepalive.conf | [IBTASK-12597](https://psbnk.msk.ru) |
| - п.п. 2.2.2, 3.2.2, 4.2.2. Настроить ведение журнала доступа (access_log) - `access_log off;`<br>- п.п. 2.2.2, 3.2.2, 4.2.2. Настроить ведение журнала доступа (access_log)<br>- п.п. 2.2.3, 3.2.3, 4.2.3. Настроить ведение журнала ошибок (error_log) - `error_log off;`<br>- п.п. 2.2.3, 3.2.3, 4.2.3. Настроить ведение журнала ошибок (error_log)<br>- п.2.4.6. Настроить заголовок `X-Frame-Options`<br>- п.2.4.7. Настроить заголовок `X-Content-Type-Options`<br>- п.2.4.8. Настроить заголовок `X-XSS-Protection`<br>- п.2.4.9. Настроить заголовок `Content Security Policy (CSP)` | basic.conf | [IBTASK-18102](https://psbnk.msk.ru)<br>[IBTASK-12536 - error-log](https://psbnk.msk.ru) |