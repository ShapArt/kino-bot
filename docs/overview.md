# Docs — Kino-bot
Providers, store and bot interactions.
## Architecture
```mermaid
flowchart LR
  User[User] -->|query| Bot[Bot]
  Bot[Bot] -->|TMDB/others| Provider[Provider]
  Bot[Bot] -->|watch/seen| Store[Store]
```
