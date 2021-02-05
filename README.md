# Create API with Django

### Check python environment
```sh
python -v
```

```sh
pip -v
```

### Install virtualenv

```sh
pip install virtualenv
```

### Create virtualenv

```sh
virtualenv <name>

source <name>/bin/activate
```

### Create django project

```sh
django-admin startproject <Project_name>

cd <Project_name>
```

### Install Django

```sh
pip install django
```

### Move to project folder

```sh
cd <Project_name>
```

### Create django application

```sh
django-admin startapp <App_name>
```


### 1. Check django admin

```sh
python manage.py migrate

python manage.py createsuperuser
```


### 2. setup django

https://bit.ly/2LVGcPZ

### 3. setup PostgreSQL
>Install postgreSQL

```sh
brew install postgresql
```
>Install check

```sh
psql -V
```
>Start PostgreSQL

```sh
brew services start postgresql
```
>Check

```sh
brew services list
```
>check default database

```sh
psql -l
```
>check default database

```sh
psql -l
```
>create user

```sh
createuser -P postgres
```
>Create database

```sh
createdb demo_api -O postgres;
```


```sh
pip install dj_database_url
pip install python-dotenv
pip install psycopg2-binary

```
In setting.py.

```sh
(TOP line)
---
from dotenv import (find_dotenv, load_dotenv)
import dj_database_url
---


(Override database setting line)
---
load_dotenv(find_dotenv())
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600)
}
---

```
Create *.env* in top directory.


'''sh
DATABASE_URL=postgres://postgres:postgres@localhost/demo_api
'''

*DATABASE_URL=postgres://{username}:{password}@localhost/{DBName}

>Connect from django and check admin site

```sh
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser
python manage.py runserver
```

### 4. setup cors
>Install cors library

```sh
pip install django-cors-headers
```

>Add *corsheaders* to setting.py

```sh
INSTALLED_APPS = [
    ...
    'corsheaders',
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
     ...
]

---Last line---

CORS_ORIGIN_ALLOW_ALL = True

---

```
<https://pypi.org/project/django-cors-headers/>


### 5. Prepare for Deploying to Heroku
>Install libraries
```sh
pip install whitenoise
pip install gunicorn
```
>Modify *setting.py*
```sh
---Near Top---
import os

DEBUG = False

ALLOWED_HOSTS = ['*']
---



MIDDLEWARE = [
    ...
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

---Near STATIC_URL---

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

---

```
<http://whitenoise.evans.io/en/stable/>

>Create a *Procfile* file in top directory.

```sh
web: gunicorn {project_folder name}.wsgi
```

>Execute the command in top directory.

```sh
pip freeze > requirements.txt
```

### 6. Deploy to Heroku
>Connect github to heroku by using GUI