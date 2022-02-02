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

To initialize the tables in the databse

```bash
$ docker-compose exec backend python manage.py makemigrations
$ docker-compose exec backend python manage.py migrate
```

To create superuser

```bash
$ docker-compose exec backend python manage.py createsuperuser
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
