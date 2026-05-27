---
template: home.html
title: СМ ГОЗ Opensource
hide:
  - navigation
  - toc
---

<style>
/* Hero Section */
.hero-section {
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 16px;
  padding: 3rem 2rem;
  margin-bottom: 2rem;
  text-align: center;
  position: relative;
  overflow: hidden;
}

[data-md-color-scheme="slate"] .hero-section {
  background: linear-gradient(135deg, #1a1a2e 0%, #16213e 100%);
  border: 1px solid rgba(255, 255, 255, 0.1);
}

.hero-section::before {
  content: "";
  position: absolute;
  top: -50%;
  left: -50%;
  width: 200%;
  height: 200%;
  background: radial-gradient(circle, rgba(255,255,255,0.1) 0%, transparent 50%);
  animation: pulse 4s ease-in-out infinite;
}

@keyframes pulse {
  0%, 100% { transform: scale(1); opacity: 0.5; }
  50% { transform: scale(1.1); opacity: 0.8; }
}

.hero-title {
  color: white !important;
  font-size: 2.5rem !important;
  font-weight: 800 !important;
  margin-bottom: 0.5rem !important;
  position: relative;
  z-index: 1;
}

.hero-subtitle {
  color: rgba(255, 255, 255, 0.9) !important;
  font-size: 1.2rem !important;
  margin-bottom: 1.5rem !important;
  position: relative;
  z-index: 1;
}

.hero-badges {
  display: flex;
  justify-content: center;
  gap: 1rem;
  flex-wrap: wrap;
  position: relative;
  z-index: 1;
}

.hero-badge {
  background: rgba(255, 255, 255, 0.2);
  color: white;
  padding: 0.5rem 1rem;
  border-radius: 20px;
  font-size: 0.85rem;
  backdrop-filter: blur(10px);
  border: 1px solid rgba(255, 255, 255, 0.3);
}

/* Cards Grid */
.cards-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 1.5rem;
  margin-bottom: 2rem;
}

.card {
  background: var(--md-default-bg-color);
  border-radius: 12px;
  padding: 1.5rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  transition: all 0.3s ease;
  position: relative;
  overflow: hidden;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.12);
  border-color: var(--md-primary-fg-color);
}

[data-md-color-scheme="slate"] .card {
  background: rgba(255, 255, 255, 0.02);
  border-color: rgba(255, 255, 255, 0.08);
}

[data-md-color-scheme="slate"] .card:hover {
  box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
  background: rgba(255, 255, 255, 0.05);
}

.card-icon {
  font-size: 2.5rem;
  margin-bottom: 1rem;
  display: block;
}

.card-title {
  font-size: 1.25rem !important;
  font-weight: 700 !important;
  margin-bottom: 0.5rem !important;
  color: var(--md-default-fg-color) !important;
}

.card-description {
  color: var(--md-default-fg-color--light);
  font-size: 0.9rem;
  line-height: 1.6;
  margin-bottom: 1rem;
}

.card-links {
  display: flex;
  flex-direction: column;
  gap: 0.5rem;
}

.card-link {
  color: var(--md-primary-fg-color) !important;
  text-decoration: none !important;
  font-size: 0.85rem;
  display: flex;
  align-items: center;
  gap: 0.5rem;
  padding: 0.25rem 0;
  transition: all 0.2s ease;
}

.card-link:hover {
  color: var(--md-accent-fg-color) !important;
  transform: translateX(4px);
}

.card-link::before {
  content: "→";
  font-weight: bold;
}

/* Quick Links Section */
.quick-links {
  background: var(--md-default-fg-color--lightest);
  border-radius: 12px;
  padding: 1.5rem;
  margin-bottom: 2rem;
}

[data-md-color-scheme="slate"] .quick-links {
  background: rgba(255, 255, 255, 0.03);
}

.quick-links-title {
  font-size: 1rem !important;
  font-weight: 700 !important;
  margin-bottom: 1rem !important;
  color: var(--md-default-fg-color--light) !important;
  text-transform: uppercase;
  letter-spacing: 0.05em;
}

.quick-links-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 0.75rem;
}

.quick-link {
  background: var(--md-default-bg-color);
  color: var(--md-default-fg-color) !important;
  padding: 0.5rem 1rem;
  border-radius: 8px;
  text-decoration: none !important;
  font-size: 0.85rem;
  border: 1px solid var(--md-default-fg-color--lightest);
  transition: all 0.2s ease;
  display: flex;
  align-items: center;
  gap: 0.5rem;
}

.quick-link:hover {
  background: var(--md-primary-fg-color);
  color: white !important;
  border-color: var(--md-primary-fg-color);
}

[data-md-color-scheme="slate"] .quick-link {
  background: rgba(255, 255, 255, 0.05);
  border-color: rgba(255, 255, 255, 0.1);
}

/* Stats Section */
.stats-section {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 1rem;
  margin-bottom: 2rem;
}

.stat-item {
  text-align: center;
  padding: 1.5rem 1rem;
  background: var(--md-default-bg-color);
  border-radius: 12px;
  border: 1px solid var(--md-default-fg-color--lightest);
}

[data-md-color-scheme="slate"] .stat-item {
  background: rgba(255, 255, 255, 0.02);
  border-color: rgba(255, 255, 255, 0.08);
}

.stat-number {
  font-size: 2rem;
  font-weight: 800;
  color: var(--md-primary-fg-color);
  display: block;
  margin-bottom: 0.25rem;
}

.stat-label {
  font-size: 0.85rem;
  color: var(--md-default-fg-color--light);
}
</style>

<!-- Hero Section -->
<div class="hero-section">
  <h1 class="hero-title">СМ ГОЗ Opensource</h1>
  <p class="hero-subtitle">Документация команды OpenSource: гайды, шпаргалки и база знаний</p>
  <div class="hero-badges">
    <span class="hero-badge">OpenSearch</span>
    <span class="hero-badge">Keycloak</span>
    <span class="hero-badge">Vector</span>
    <span class="hero-badge">Kafka</span>
  </div>
</div>

<!-- Stats -->
<div class="stats-section">
  <div class="stat-item">
    <span class="stat-number">8</span>
    <span class="stat-label">Аудит-документов</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">9</span>
    <span class="stat-label">Шпаргалок</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">3</span>
    <span class="stat-label">Технологии</span>
  </div>
  <div class="stat-item">
    <span class="stat-number">2</span>
    <span class="stat-label">Орг. раздела</span>
  </div>
</div>

<!-- Quick Links -->
<div class="quick-links">
  <h3 class="quick-links-title">Быстрые ссылки</h3>
  <div class="quick-links-grid">
    <a href="home/Monitoring/" class="quick-link">:material-chart-line: Мониторинг</a>
    <a href="home/Backlog/" class="quick-link">:material-clipboard-list: Backlog</a>
    <a href="home/ОргРаздел/Дежурства/" class="quick-link">:material-calendar-clock: Дежурства</a>
    <a href="home/ОргРаздел/Группы_и_ТУЗ_Opensource/" class="quick-link">:material-account-group: Группы и ТУЗ</a>
  </div>
</div>

<!-- Main Cards -->
<div class="cards-grid">

  <!-- Аудит -->
  <div class="card">
    <span class="card-icon">:material-shield-check:</span>
    <h3 class="card-title">Аудит</h3>
    <p class="card-description">Документация по аудиту компонентов системы: приложения, провайдеры аутентификации, хранилища и интеграции.</p>
    <div class="card-links">
      <a href="home/Audit/AppExt/" class="card-link">APP EXT</a>
      <a href="home/Audit/AuthProvider/" class="card-link">AUTH PROVIDER</a>
      <a href="home/Audit/Front-Web/" class="card-link">FRONT WEB</a>
      <a href="home/Audit/Kafka-app/" class="card-link">KAFKA APP</a>
      <a href="home/Audit/Opensearch/" class="card-link">OPENSEARCH</a>
      <a href="home/Audit/Storage/" class="card-link">STORAGE</a>
    </div>
  </div>

  <!-- OpenSearch -->
  <div class="card">
    <span class="card-icon">:material-database-search:</span>
    <h3 class="card-title">OpenSearch</h3>
    <p class="card-description">Настройка мониторов, обновление кластера и работа с OpenSearch для логирования и поиска.</p>
    <div class="card-links">
      <a href="home/Opensearch/Monitors/" class="card-link">Мониторы</a>
      <a href="home/Opensearch/Обновление-кластера/" class="card-link">Обновление кластера</a>
    </div>
  </div>

  <!-- Keycloak -->
  <div class="card">
    <span class="card-icon">:material-key-variant:</span>
    <h3 class="card-title">Keycloak</h3>
    <p class="card-description">Аутентификация и авторизация: настройка X509 сертификатов, SSO и управление идентификацией.</p>
    <div class="card-links">
      <a href="home/Keycloak/X509-Authentication/" class="card-link">X509 Authentication</a>
    </div>
  </div>

  <!-- Vector -->
  <div class="card">
    <span class="card-icon">:material-arrow-decision:</span>
    <h3 class="card-title">Vector</h3>
    <p class="card-description">Сбор, обработка и маршрутизация логов с помощью Vector для централизованного логирования.</p>
    <div class="card-links">
      <a href="home/Vector/Logging-v2/" class="card-link">Logging v2</a>
    </div>
  </div>

  <!-- Шпаргалка -->
  <div class="card">
    <span class="card-icon">:material-notebook:</span>
    <h3 class="card-title">Шпаргалка</h3>
    <p class="card-description">Полезные команды и инструкции для повседневной работы: bash, ceph, kafka, consul и другие инструменты.</p>
    <div class="card-links">
      <a href="home/Шпаргалка/bash/" class="card-link">Bash</a>
      <a href="home/Шпаргалка/ceph/" class="card-link">Ceph</a>
      <a href="home/Шпаргалка/kafka/" class="card-link">Kafka</a>
      <a href="home/Шпаргалка/Consul/" class="card-link">Consul</a>
      <a href="home/Шпаргалка/Opensearch/" class="card-link">OpenSearch</a>
    </div>
  </div>

  <!-- Организация -->
  <div class="card">
    <span class="card-icon">:material-account-supervisor:</span>
    <h3 class="card-title">Организация</h3>
    <p class="card-description">Организационная информация команды: графики дежурств, группы доступа и управление ТУЗ.</p>
    <div class="card-links">
      <a href="home/ОргРаздел/Дежурства/" class="card-link">Дежурства</a>
      <a href="home/ОргРаздел/Группы_и_ТУЗ_Opensource/" class="card-link">Группы и ТУЗ</a>
    </div>
  </div>

</div>

---

!!! tip "Нужна помощь?"
    Если вы не нашли нужную информацию, проверьте раздел [Backlog](home/Backlog/) или обратитесь к дежурному инженеру согласно [графику дежурств](home/ОргРаздел/Дежурства/).
