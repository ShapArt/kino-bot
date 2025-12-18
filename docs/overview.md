# Kino Bot — overview

```mermaid
sequenceDiagram
  participant User
  participant Bot
  participant MiniApp
  participant Backend
  participant TMDB
  participant DB

  User->>Bot: /start (deep-link)
  Bot-->>User: Link to MiniApp (initData)
  MiniApp->>Backend: Auth via initData, fetch recommendations
  Backend->>TMDB: Search/details
  Backend->>DB: Store likes/swipes
  Backend-->>MiniApp: Next card, match info
  Backend-->>Bot: Notify matches
```

Components:

- Aiogram bot: onboarding, reminders, notifications.
- Mini App: swipe UI, history, match view.
- Backend (FastAPI): TMDB proxy, auth, persistence (Postgres), rate limits, cache.
