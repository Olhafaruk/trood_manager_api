# 🧠 Trood Manager API

A scalable Django REST Framework backend for managing **projects** and **vacancies**, featuring token authentication, a sleek Jazzmin admin, auto-generated Swagger docs, and Dockerized deployment.

Built with clarity and structure for production use.

---

## 🚀 Live Access

| Interface     | URL                                                           |
|---------------|---------------------------------------------------------------|
| Swagger UI    | [trood-api.onrender.com/swagger](https://trood-api.onrender.com/swagger/) |
| Redoc Docs    | [trood-api.onrender.com/redoc](https://trood-api.onrender.com/redoc/)     |
| Admin Panel   | [trood-api.onrender.com/admin](https://trood-api.onrender.com/admin/)     |
| Projects API  | [trood-api.onrender.com/api/projects](https://trood-api.onrender.com/api/projects/) |
| Vacancies API | [trood-api.onrender.com/api/vacancies](https://trood-api.onrender.com/api/vacancies/) |

---

## 🧱 Stack & Architecture

- 🐍 Django 4.2 + Django REST Framework
- 🗄 PostgreSQL (via Render)
- 🍱 Token-based auth (DRF Tokens)
- 🎩 Jazzmin for admin customization
- 🎯 drf-spectacular for schema generation
- 🐳 Docker & docker-compose for dev setup
- 🔥 Waitress + WhiteNoise for static file serving

---

## 🔐 Authentication Endpoints

| Method | Endpoint                       | Description                 |
|--------|--------------------------------|-----------------------------|
| POST   | `/auth/register/`              | Register a new user        |
| GET    | `/auth/profile/`               | Get user profile info      |
| PUT    | `/auth/profile/`               | Update profile fields      |
| POST   | `/auth/change-password/`       | Change current password    |

👉 Protected routes require header:

```
Authorization: Token your_token_here
```

---

## 📦 Main API Structure

### Projects

| Endpoint                              | Method(s)            |
|---------------------------------------|----------------------|
| `/api/projects/`                      | GET, POST            |
| `/api/projects/{id}/`                 | GET, PUT, PATCH, DELETE |
| `/api/projects/{id}/vacancies/`       | GET, POST            |

### Vacancies

| Endpoint                              | Method(s)            |
|---------------------------------------|----------------------|
| `/api/vacancies/`                     | GET, POST            |
| `/api/vacancies/{id}/`                | GET, PUT, PATCH, DELETE |

Supports query filtering such as `employment_type`, `project_id`, etc.

---

## 🧪 Example Requests (via `curl`)

### 🔐 Register

```bash
curl -X POST https://trood-api.onrender.com/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "Olga", "email": "user@example.com", "password": "olgatrood"}'
```

### 👤 Get Profile

```bash
curl -X GET https://trood-api.onrender.com/auth/profile/ \
  -H "Authorization: Token YOUR_TOKEN"
```

### 🔒 Change Password

```bash
curl -X POST https://trood-api.onrender.com/auth/change-password/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"old_password": "oldpass", "new_password": "newpass123"}'
```

### 📁 Create Project

```bash
curl -X POST https://trood-api.onrender.com/api/projects/ \
  -H "Authorization: Token YOUR_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Trood Platform",
    "description": "SaaS for project-based hiring",
    "budget": 50000,
    "deadline": "2025-12-31"
  }'
```

---

## 🐳 Local Setup

```bash
git clone https://github.com/Olhafaruk/trood_manager_api.git
cd trood_manager_api
cp .env.example .env  # Fill in your environment variables
docker-compose up --build
docker-compose exec web python backend/manage.py migrate
docker-compose exec web python backend/manage.py createsuperuser
```

---

## ⚙️ Environment Variables (`.env.example`)

```env
DJANGO_SECRET_KEY=your-secret-key
DJANGO_ALLOWED_HOSTS=trood-api.onrender.com
DJANGO_SETTINGS_MODULE=config.settings.production
DJANGO_DEBUG=False
DATABASE_URL=postgres://user:password@host/dbname
```

---

## 🚀 Deploying to Render

1. Create PostgreSQL database
2. Add Web Service pointing to your repo
3. Build & Start commands:

```bash
# Build
pip install -r requirements.txt

# Start
waitress-serve --listen=0.0.0.0:8000 config.wsgi:application
```

4. Add same `.env` variables into Render dashboard

---

## 👩‍💻 Author

Built and maintained by [Olhafaruk](https://github.com/Olhafaruk/trood_manager_api.git)  







