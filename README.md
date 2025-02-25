
## Introduction
This is a simple project for a To-Do List application. It has 2 core components:
1. Database Layer: PostgreSQL
2. API Layer: Django

## Database Layer
### Run database instance in container
Create the PostgreSQL database image
```bash
docker build -t postgres-alpine:17.2 db/
```

Run the database container
```bash
docker run -d --name postgres-db -p 5432:5432 postgres-alpine:17.2
```

Access and use the PostgreSQL shell in the database container 
```bash
docker exec -it postgresql-db psql -U django -d django_db
```

### Query Data
List tables available in the database container
```
django_db=# \dt 
```

Query the database table
```
django_db=# SELECT * FROM to_do_list;
```

## API Layer
### Configuration
Update Django app to use the database container in the DATABASES variable in the `settings.py` file:

```py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'django',
        'PASSWORD': 'django_password',
        'HOST': '0.0.0.0',
        'PORT': '5432',
    }
}
```

### Run Django application in Python virtual environment
Activate Python virtual environment
```bash
python -m venv .venv
```

Activate the virtual environment
```bash
source .venv/bin/activate
```

Install Python packages including Django and more
```bash
pip install -r requirements.txt
```

Run the Python application
```bash
python manage.py runserver
```

### Run Django application in container
Create the Django image
```bash
docker build -t django-api:1.0 api/
```

Run the Django container
```bash
docker run -d -p 8000:8000 --name django-api django-api:1.0
```

## Notes
- Use the snippet below to map the Django model to link it to the actual name of the database table 
```Python
    class Meta:
        db_table = 'to_do_list' 
```

## To Do
- Create separate server instance for hosting app on Production
- Turn off DEBUG=TRUE setting