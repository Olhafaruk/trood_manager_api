# 🧠 Trood Manager API – Backend for Projects & Vacancies

A scalable Django REST Framework backend for managing **projects** and **vacancies**, featuring token authentication, 
customized admin (Jazzmin), auto-generated Swagger docs, and Dockerized deployment. Built for clarity, maintainability,
and production use.

---

## 🚀 Live Access

| Interface       | Full URL                                                                 |
|-----------------|--------------------------------------------------------------------------|
| Swagger UI      | [https://trood-api.onrender.com/swagger](https://trood-api.onrender.com/swagger)         |
| Redoc Docs      | [https://trood-api.onrender.com/redoc](https://trood-api.onrender.com/redoc)             |
| Admin Panel     | [https://trood-api.onrender.com/admin](https://trood-api.onrender.com/admin)             |
| Projects API    | [https://trood-api.onrender.com/api/projects/](https://trood-api.onrender.com/api/projects/)     |
| Vacancies API   | [https://trood-api.onrender.com/api/vacancies/](https://trood-api.onrender.com/api/vacancies/)   |
| Register User   | [https://trood-api.onrender.com/auth/register/](https://trood-api.onrender.com/auth/register/)   |
| Profile Info    | [https://trood-api.onrender.com/auth/profile/](https://trood-api.onrender.com/auth/profile/)     |

---

## 🧱 Tech Stack

- 🐍 Django 4.2 + Django REST Framework  
- 🛢 PostgreSQL (Render hosted)  
- 🔐 DRF Token Authentication  
- 🎩 Jazzmin for customized admin  
- 🧠 drf-spectacular for OpenAPI schema  
- 🐳 Docker & docker-compose setup  
- 🔥 WhiteNoise + Waitress for deployment

---

## 🔐 Authentication Endpoints

| Method | Endpoint                            | Description               |
|--------|-------------------------------------|---------------------------|
| POST   | `/auth/register/`                   | Register new user         |
| GET    | `/auth/profile/`                    | Get user profile          |
| PUT    | `/auth/profile/`                    | Update user profile       |
| POST   | `/auth/change-password/`            | Change user password      |

👉 Requires header for protected routes:

```http
Authorization: Token YOUR_TOKEN_HERE
```

---

## 📦 API Endpoints

### Projects

| Endpoint                                 | Method(s)                 |
|------------------------------------------|---------------------------|
| `/api/projects/`                         | GET, POST                 |
| `/api/projects/{id}/`                    | GET, PUT, PATCH, DELETE   |
| `/api/projects/{id}/vacancies/`          | GET, POST                 |

### Vacancies

| Endpoint                                 | Method(s)                 |
|------------------------------------------|---------------------------|
| `/api/vacancies/`                        | GET, POST                 |
| `/api/vacancies/{id}/`                   | GET, PUT, PATCH, DELETE   |

🔎 Supports query filtering by fields like `project_id`, `employment_type`, etc.

---

## 🧪 Sample Requests (`curl`)

### 🔐 Register
```bash
curl -X POST https://trood-api.onrender.com/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "olha", "email": "user@example.com", "password": "testpass123"}'
```

### 👤 Get Profile
```bash
curl -X GET https://trood-api.onrender.com/auth/profile/ \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### 🛠 Create Project
```bash
curl -X POST https://trood-api.onrender.com/api/projects/ \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
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

## ⚙️ Environment Variables (.env)

```env
DJANGO_DEBUG=True
SECRET_KEY=your-dev-key
DB_NAME=trood_db
DB_USER=trood_user
DB_PASSWORD=trood_pass
DB_HOST=db
DB_PORT=5432
```

---

## 🚀 Deploying to Render

1. Create PostgreSQL database  
2. Deploy repo as Web Service  
3. Build & start commands:

```bash
# Build
pip install -r requirements.txt

# Run
waitress-serve --listen=0.0.0.0:8000 config.wsgi:application
```

4. Add `.env` variables in Render dashboard settings

---
## 📎 Useful Info

🧪 Admin Credentials
Use these demo credentials to test the admin dashboard:
Username: admin
Password: Admin12345
⚠️ For demo purposes only. Do not use these credentials in production.

---

## 👩‍💻 Author

Built and maintained by [Olhafaruk](https://github.com/Olhafaruk)

---

