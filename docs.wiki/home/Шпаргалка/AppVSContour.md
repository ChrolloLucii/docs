Таблица логических групп и контуров, где они развернуты Таблица создана на основании group_vars

| Group | dev | fiat | idev | ift | iift | ilt | ipreprod | itest | lt | preprod | rtest | stest | test | iprod | prod |
|-------|-----|------|------|-----|------|-----|----------|-------|----|---------|-------|-------|------|-------|------|
| api-gw |  |  |  |  | &#10133; | &#10133; | &#10133; | :heavy_plus_sign: |  |  |  |  |  | :heavy_plus_sign: |  |
| app |  | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: |  |  |  | :heavy_plus_sign: | :heavy_plus_sign: |
| app-ext | :heavy_plus_sign: |  | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: |  |  |  | :heavy_plus_sign: | :heavy_plus_sign: |
| auth-provider |  |  | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: |  |  |  | :heavy_plus_sign: | :heavy_plus_sign: |
| balancer |  |  |  | :heavy_plus_sign: |  |  |  |  |  | :heavy_plus_sign: |  |  |  |  | :heavy_plus_sign: |
| front-web |  |  | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: |  |  |  | :heavy_plus_sign: | :heavy_plus_sign: |
| kafka-app | :heavy_plus_sign: |  | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: |  |  | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: |
| kafka-log |  |  |  |  |  | :heavy_plus_sign: | :heavy_plus_sign: |  | :heavy_plus_sign: |  | :heavy_plus_sign: | :heavy_plus_sign: |  | :heavy_plus_sign: | :heavy_plus_sign: |
| loginom |  |  |  |  |  |  |  | :heavy_plus_sign: |  |  |  |  |  |  |  |
| monitoring |  |  |  |  |  | :heavy_plus_sign: | :heavy_plus_sign: |  | :heavy_plus_sign: |  | :heavy_plus_sign: | :heavy_plus_sign: |  | :heavy_plus_sign: | :heavy_plus_sign: |
| monolit-lb |  |  |  | :heavy_plus_sign: |  | :heavy_plus_sign: |  |  |  | :heavy_plus_sign: |  |  |  |  |  |
| opensearch |  |  |  |  |  | :heavy_plus_sign: | :heavy_plus_sign: |  | :heavy_plus_sign: |  | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: |
| runner | :heavy_plus_sign: |  |  |  |  | :heavy_plus_sign: |  |  |  | :heavy_plus_sign: |  |  | :heavy_plus_sign: |  | :heavy_plus_sign: |
| service-discovery |  |  | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: |  | :heavy_plus_sign: |  |  | :heavy_plus_sign: | :heavy_plus_sign: |  |
| service-discovery-dba |  |  |  |  |  |  |  |  |  |  |  |  |  | :heavy_plus_sign: | :heavy_plus_sign: |
| storage |  |  |  |  |  | :heavy_plus_sign: | :heavy_plus_sign: |  |  |  | :heavy_plus_sign: | :heavy_plus_sign: |  | :heavy_plus_sign: |  |
| zookeeper-app | :heavy_plus_sign: |  | :heavy_plus_sign: | :heavy_plus_sign: | :heavy_plus_sign: |  | :heavy_plus_sign: | :heavy_plus_sign: |  | :heavy_plus_sign: |  |  | :heavy_plus_sign: | :heavy_plus_sign: |  |
| zookeeper-log |  |  |  |  |  |  | :heavy_plus_sign: |  |  |  | :heavy_plus_sign: | :heavy_plus_sign: |  | :heavy_plus_sign: |  |
| zookeeper-shared |  |  |  |  |  | :heavy_plus_sign: |  |  | :heavy_plus_sign: |  |  |  |  |  | :heavy_plus_sign: |

Таблица для WHITE_LIST

| Group | Contour (no prod) | Contour (prod) |
|-------|-------------------|----------------|
| api-gw | iift, ilt, ipreprod, itest | iprod |
| app | fiat, idev, ift, iift, ilt, ipreprod, itest, lt, preprod | iprod, prod |
| app-ext | dev,idev, ift, iift, ilt, ipreprod, itest, lt, preprod | iprod, prod |
| auth-provider | idev, ift, iift, ilt, ipreprod, itest, lt, preprod | iprod, prod |
| front-web | idev, ift, iift, ilt, ipreprod, itest, lt, preprod | iprod, prod |
| kafka-app | dev,idev, ift, iift, ilt, ipreprod, itest, lt, preprod, test | iprod, prod |
| kafka-log | ilt, ipreprod, lt, rtest, stest | iprod, prod |
| loginom | itest |  |
| monitoring | ilt, ipreprod, lt, rtest, stest | iprod, prod |
| monolit-lb | ift, ilt, preprod |  |
| opensearch | ilt, ipreprod, lt, rtest, stest, test | iprod, prod |
| runner | dev, ilt, preprod, test | prod |
| service-discovery | idev, ift, iift, ilt, ipreprod, itest, lt, preprod | iprod |
| service-discovery-dba |  | iprod, prod |
| storage | ilt, ipreprod, rtest, stest | iprod |
| zookeeper-app | dev,idev, ift, iift, ipreprod, itest, preprod, test | iprod |
| zookeeper-log | ipreprod, rtest, stest | iprod |
| zookeeper-shared | ilt, lt | prod |

