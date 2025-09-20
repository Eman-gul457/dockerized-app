# 🚀 Dockerized App — Flask + PostgreSQL

A tiny, production-style web app packaged with Docker & Docker Compose.  
It includes healthchecks, a persistent Postgres volume, and a demo endpoint that records visits.

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?logo=python&logoColor=white)](#)
[![Flask](https://img.shields.io/badge/Flask-3.x-000000?logo=flask&logoColor=white)](#)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-16-336791?logo=postgresql&logoColor=white)](#)
[![Docker](https://img.shields.io/badge/Docker-OK-2496ED?logo=docker&logoColor=white)](#)
[![Compose](https://img.shields.io/badge/Compose-v2-1D63ED?logo=docker&logoColor=white)](#)
[![License](https://img.shields.io/badge/License-MIT-green)](#license)


---

## 📌 Project Goals
- Containerize a simple **Flask** app using **Gunicorn** (production WSGI).
- Orchestrate **app + PostgreSQL** with **Docker Compose**.
- Add **healthchecks** (app `/healthz`, DB `pg_isready`).
- Use a **named volume** so DB data **persists** across restarts.
- Provide clear **one-command** run & **troubleshooting** steps.

---

## 🧰 Tech Stack
- **Python 3.12**, **Flask 3.x**, **Gunicorn**
- **PostgreSQL 16 (Alpine)**
- **Docker**, **Docker Compose v2**
- Shell / cURL for quick verification

---

## 📁 Repository Structure

