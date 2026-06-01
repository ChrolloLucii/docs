# RedOS: временное подключение репозитория latest

Для обновления до последней версии пакета (например, `nginx`) может потребоваться временно подключить репозиторий `latest`, выполнить обновление и вернуть стандартный репозиторий.

!!! warning "Важно"
    Если у вас не сертифицированный RedOS, замените `73c-updates` на `73-update`.

## Плейбук: переключение на latest

```yaml
---
- name: "Set redos-latest"
  hosts: all
  gather_facts: false
  vars:
    repo_file: "/etc/yum.repos.d/RedOS-Updates.repo"
    new_baseurl: "baseurl=https://frmn-app.headoffice.psbank.local/pulp/content/PSB/Library/custom/redos-latest/73c-updates/"
  tasks:
    - name: Replace baseurl in repo file
      replace:
        path: "{{ repo_file }}"
        regexp: '^baseurl=.*redos-latest/73c-updates/$'
        replace: "{{ new_baseurl }}"
    - name: make yum cache
      command:
        cmd: yum makecache
      args:
        warn: false
    - name: Ensure that cache is right
      command:
        cmd: yum repoquery --show-duplicates nginx
      register: repository_nginx
    - name: Ensure nginx 1.30 is present
      assert:
        that: "'1.30' in repository_nginx.stdout"
```

```bash
ansible-playbook -i inventory/itest/hosts.ini --limit smgoz__front_web__nginx playbook-new.yml --ask-pass
```

После этого выполняется основная роль.

## Плейбук: возврат к стандартному репозиторию

```yaml
---
- name: "Set redos-latest"
  hosts: all
  gather_facts: false
  vars:
    repo_file: "/etc/yum.repos.d/RedOS-Updates.repo"
    old_baseurl: "baseurl=https://frmn-app.headoffice.psbank.local/pulp/content/PSB/Library/quater-freeze/custom/redos-latest/73c-updates/"
  tasks:
    - name: Replace baseurl in repo file
      replace:
        path: "{{ repo_file }}"
        regexp: '^baseurl=.*redos-latest/73c-updates/$'
        replace: "{{ old_baseurl }}"
    - name: clean cache
      command:
        cmd: yum clean all
      args:
        warn: false
    - name: make yum cache
      command:
        cmd: yum makecache
      args:
        warn: false
    - name: Ensure that cache is right
      command:
        cmd: yum repoquery --show-duplicates nginx
      register: repository_nginx
    - name: Ensure nginx 1.30 is absent
      assert:
        that: "'1.30' not in repository_nginx.stdout"
```