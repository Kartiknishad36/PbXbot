# PBX Userbot (Self-Contained)

Telethon userbot — **Kartiknishad36** fork, rebuilt without external plugin download.

> Original `Badhacker98/Plugins` is **gone (404)**. This repo now runs **100% local code** under `TelethonPbx/`.

## Features
- `.ping` `.alive` `.help` `.id` `.info`
- Owner: `.eval` `.restart`
- No `GIT_REPO` / no zip download from third party
- Render / Heroku ready

## Setup
1. Get `APP_ID` + `API_HASH` from https://my.telegram.org
2. Generate session: `python3 Pbx_string.py`
3. Set env vars (see `.env.example`)
4. Run: `bash PBX` or `python3 -m TelethonPbx`

## Env
| Var | Required |
|-----|----------|
| APP_ID | yes |
| API_HASH | yes |
| PBXBOT_SESSION | yes |
| OWNER_ID | recommended |
| HANDLER | default `.` |
| LOGGER_ID | optional |
| BOT_TOKEN | optional |

## Deploy
- **Render**: Worker service + env vars + start `bash PBX`
- **Heroku**: use `app.json` / Procfile

## Note
This is a clean minimal core. Old spam/raid plugins from Badhacker98 are **not** included (source unavailable + not recommended).
