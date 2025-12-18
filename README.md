# Kino Bot (Telegram Mini App + TMDB)

## ✨ Что умеет

- «Tinder для фильмов»: свайпы в мини-приложении, совпадения для пары/компании.
- Импорт вишлистов TMDB/CSV, базовые рекомендации (жанры/популярность) с дальнейшим ML-улучшением.
- Уведомления и напоминания через aiogram-бот, deep-link авторизация в mini app.
- Совместные подборки: общий watchlist и «подбор для двоих».

## 🧠 Технологии

- Bot: Aiogram 3.x (deep-links, уведомления), rate-limit.
- Mini App: React/Vite + Telegram Web Apps SDK (auth via initData).
- Backend: FastAPI + Postgres, TMDB API proxy, кеширование, rate-limit.
- Безопасность: TMDB ключ через ENV, gitleaks/pre-commit, minimal Actions permissions.

## 🖼️ Демо

- TODO: добавить скрин/видео mini app и ссылку на стенд.

## Архитектура

- `bot/` — aiogram хэндлеры (/start, /help, webhook/polling).
- `miniapp/` — фронт WebApp (React/Vite + TWA SDK, свайпы, история лайков).
- `backend/` — FastAPI, TMDB proxy/search, user/watchlist APIs, Postgres.
- `docs/` — overview, ci badge snippet; `assets/` — social preview.

## Конфигурация

- `.env.example`: `BOT_TOKEN`, `TMDB_API_KEY`, `DATABASE_URL`, `REDIS_URL`, `WEBAPP_ORIGIN`, `ALLOWED_ORIGINS`.
- Заполнить `.env`, не коммитить секреты.

### Локальный запуск

Bot:

```bash
pip install -r requirements.txt
python -m bot.main
```

Backend:

```bash
cd backend
pip install -e .[dev]
uvicorn app.main:app --reload
```

Docker Compose (backend+db+redis):

```bash
cd infra
docker compose up --build
```

## Тесты

- План: bot/backend — `ruff check . && black --check . && mypy . && pytest` (после реализации); miniapp — `npm run lint && npm test` (после scaffold).

### Miniapp локально

```bash
cd miniapp
npm install
npm run dev
```

## Roadmap

- Инициализировать miniapp (React/Vite + TWA SDK), бекенд FastAPI с TMDB proxy, schema (users, likes, matches).
- Добавить свайпы/матчи, TMDB поиска/изображений, кеш.
- Deep-link авторизация бота ↔ miniapp, напоминания.
- Рекомендательный базовый слой (жанры/популярность), затем ML улучшения.
- CI: lint/tests для bot/backend/miniapp; e2e playwright smoke.
