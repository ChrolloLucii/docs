# AUTH PROVIDER

Согласования по требованиям ИБ для Keycloak (Auth Provider).

## Keycloak

| Пункт | IIFT, ITEST, PREPROD, IFT, LT, ILT, IDEV, PROD, IPREPROD, IPROD | Комментарий |
| --- | --- | --- |
| 2.2.1-2 | [IBTASK-1146020](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$99615284) | Не используется |
| 2.2.1-3 | [IBTASK-1146020](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$99615284) | Не используется |
| 2.2.1-4 | [IBTASK-1146020](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$99615284) | Не используется |
| 4.2-4 | [IBTASK-1146020](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$99615284) | Согласовано |
| 4.3 | [IBTASK-1146020](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$99615284) | Права 700 на директорию `/srv/keycloak/log` |
| 4.4 | [IBTASK-1146020](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$99615284) | Права 700 на `/srv/keycloak/data/tmp` |

## Дополнительные согласования (IDEV)

| Пункт | IDEV | Комментарий |
| --- | --- | --- |
| Время жизни токена | [IBTASK-1805248](https://alm.headoffice.psbank.local/sd/operator/#uuid:GMtask$168183814:GMtask$PMibtask) | Согласован 1 час |

