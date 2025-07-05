# Trood Backend

A Django REST Framework API for managing projects and their vacancies. This README explains how to run the project locally, which endpoints are available, and how to use the admin interface with a superuser.

---

## Setup and Local Development

1. Clone the repository  
   ```bash
   git clone https://github.com/your-org/trood-backend.git
   cd trood-backend
   ```

2. Copy the example environment file and set your secret key  
   ```bash
   cp .env.example .env
   # Edit .env and add SECRET_KEY and any other variables
   ```

3. Build and start services with Docker Compose  
   ```bash
   docker-compose build
   docker-compose up -d
   ```

4. Run database migrations  
   ```bash
   docker-compose exec web python backend/manage.py migrate
   ```

5. (Optional) Load initial data or fixtures if provided  
   ```bash
   docker-compose exec web python backend/manage.py loaddata initial_data.json
   ```

---

## Available API Endpoints

All endpoints are prefixed with `/api/`.

| Resource             | HTTP Method | URL                                  | Description                                 |
|----------------------|-------------|--------------------------------------|---------------------------------------------|
| Project list         | GET         | `/api/projects/`                     | Retrieve a list of all projects             |
| Project detail       | GET         | `/api/projects/{id}/`                | Retrieve details of a single project        |
| Project create       | POST        | `/api/projects/`                     | Create a new project                        |
| Project update       | PUT/PATCH   | `/api/projects/{id}/`                | Update an existing project                  |
| Project delete       | DELETE      | `/api/projects/{id}/`                | Delete a project                            |
| Vacancy list         | GET         | `/api/vacancies/`                    | Retrieve a list of all vacancies            |
| Vacancy detail       | GET         | `/api/vacancies/{id}/`               | Retrieve details of a single vacancy        |
| Vacancy create       | POST        | `/api/vacancies/`                    | Create a new vacancy                        |
| Vacancy update       | PUT/PATCH   | `/api/vacancies/{id}/`               | Update an existing vacancy                  |
| Vacancy delete       | DELETE      | `/api/vacancies/{id}/`               | Delete a vacancy                            |
| Project vacancies    | GET         | `/api/projects/{id}/vacancies/`      | List all vacancies for a given project      |
| Project vacancies    | POST        | `/api/projects/{id}/vacancies/`      | Create a new vacancy within a given project |

---

## Admin Panel

The admin interface is powered by Django Jazzmin and available at:

```
http://127.0.0.1:8000/admin/
```

### Creating a Superuser

Run the following command to create an admin account:

```bash
docker-compose exec web python backend/manage.py createsuperuser
```

You will be prompted for:
- Username  
- Email address  
- Password (hidden while typing)

Upon success, you will see `Superuser created successfully.`

### Logging In

1. Open your browser and go to `http://127.0.0.1:8000/admin/`
2. Enter the superuser’s credentials
3. Manage Projects, Vacancies, Users, and Groups from the sidebar

---

You now have a fully functional backend with REST API endpoints and a branded Jazzmin admin panel. Happy coding!