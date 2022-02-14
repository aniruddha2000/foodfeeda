# foodfeeda

Django back-end for Google Solution Challenge 2022

---

## How to use the application

Make sure you have [pipenv](https://docs.python-guide.org/dev/virtualenvs/#installing-pipenv) or [docker](https://docs.docker.com/engine/install/) install in your system.

### With docker container -

To build the images and run the container

```bash
$ docker-compose up
```

To initialize the tables in the databse(Note: Run below command with running container)

```bash
$ docker-compose exec backend python manage.py makemigrations
$ docker-compose exec backend python manage.py migrate
```

To create superuser

```bash
$ docker-compose exec backend python manage.py createsuperuser
```

To drop the database

```bash
$ docker-compose down
$ docker-compose up db
$ docker-compose exec db psql -U postgres -d postgres -c 'DROP DATABASE "FOODFEEDADATABASE";'
```

To create the database

```bash
$ docker-compose exec db psql -U postgres -d postgres -c 'CREATE DATABASE "FOODFEEDADATABASE";'
$ docker-compose exec backend python manage.py migrate
```

### With Pipenv -

To install all the dependencies -

```bash
$ pipenv install
$ pipenc install --dev
```

To launch the environment -

```bash
$ pipenv shell
```

## How to format the code after writting

Formatting with pep8 style

```bash
$ docker-compose exec backend autopep8 ./ -r -i --pep8-passes 2000 --verbose --exclude="*/migrations"
```

Remove unused imports

```bash
$ docker-compose exec backend autoflake ./ -r -i --verbose --remove-unused-variables --exclude="*/migrations"
```
