```ini
  GET _search
  {
    "query": {
      "match_all": {}
    }
  }
## Работа с кластером
  GET _cluster/health
  GET _cluster/settings?format=yaml
  GET _cluster/settings
  GET _cluster/stats
  GET _cluster/health/?level=shards&pretty
  GET /_cluster/state?filter_path=version
  POST _cluster/reroute?retry_failed
  GET _cluster/pending_tasks
  ## Исключение серверов из репликации
  PUT _cluster/settings
  {
  "persistent":{
    "cluster.routing.allocation.exclude._name" : "SMGOZ-OX-OS05,SMGOZ-ST-OS02"
    }
  }
## Работы с нодами кластера
  GET _cat/nodes?v
  GET _nodes/?filter_path=nodes.*.settings.node
  GET _nodes/stats/indices?filter_path=nodes.*.indices.store
  GET _cat/nodes?h=ip,heap.percent,ram.percent,cpu,load_1m,load_5m,load_15m,node.role,master,name,version&v
## Все шарды кластера
  GET _cat/shards?v
## Работа с индексами
  GET _cat/indices/*audit*?v&h=index,pri,rep,docs.count,store.size
  GET _cat/indices/*log*?v&h=index,pri,rep,docs.count,store.size
  GET _cat/indices/
  GET _cat/indices/pre*audit*?v
  GET _plugins/_security/api/roles/app_journal_presenter_pre
  GET _plugins/_security/api/tenants
  GET ift-smgoz-log.import-payment-service-2024-06-04/_search
## Работа с плагинами
  GET _plugins/_security/api/roles/
  GET _plugins/_security/api/rolesmapping/group_smgoz-iftos-viewer
  GET _plugins/_security/api/roles/group_smgoz-iftos-viewer
  GET _plugins/_security/api/roles 
  GET _plugins/_security/api/rolesmapping/
  GET /_all
  GET _cat/shards?h=index,shard,prirep,state,unassigned.reason
## Добавление маунтпоинта для снапшотов
  PUT /_snapshot/my-fs-repository
  {
    "type": "fs",
    "settings": {
      "location": "/srv/os_snapshot_stest"
    }
  }
```