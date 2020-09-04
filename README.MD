
# A Django project for a RESTful Application using Docker


Description
=======

The application is a simple RESTful app that allows users to create list of recipies, ingredients , tags recipes, tag ingredients and upload image of recipies. The api end points allow user to filter their recipies based on tags and ingredients seperately.It is a simple [Django](https://www.djangoproject.com/) project that uses [Django REST framework](http://www.django-rest-framework.org/). The template makes use of Docker to create containers for developmet.

It uses python3, Django 3, Docker and travis CI for automated tests

## Usage

Download the repository:
```
$ git clone https://github.com/ashok-kavungal/python-recipieAPI.git
```

Init project:
```
$ cd python-recipieAPI
$ docker-compose build
```
Launch:
```
$ docker-compose up
```

*Now your django app is available on port 8000 of any ip address of your machine, but it's optional for development*

### Create a super user
```
$ docker-compose exec <container-id> python manage.py createsuperuser
```

## Awesome resources

Useful awesome list to learn more about all the different components used in this repository.

* [Docker](https://github.com/veggiemonk/awesome-docker)
* [Django](https://gitlab.com/rosarior/awesome-django)
* [Python](https://github.com/vinta/awesome-python)

## Useful links

* [Docker Hub Python](https://hub.docker.com/_/python/)
* [Docker Hub Postgres](https://hub.docker.com/_/postgres/)
* [Docker compose Postgres environment variables](http://stackoverflow.com/questions/29580798/docker-compose-environment-variables)
* [Quickstart: Docker Compose and Django](https://docs.docker.com/compose/django/)
* [Best practices for writing Dockerfiles](https://docs.docker.com/engine/userguide/eng-image/dockerfile_best-practices/)

## Screenshots 

![Screen shots of build](./screenshots/1.png?raw=true "Result")
![Screen shots of build](./screenshots/2.png?raw=true "Result")
![Screen shots of build](./screenshots/3.png?raw=true "Result")

![Screen shots of build](./screenshots/4.png?raw=true "Result")
![Screen shots of build](./screenshots/5.png?raw=true "Result")
![Screen shots of build](./screenshots/6.png?raw=true "Result")

![Screen shots of build](./screenshots/7.png?raw=true "Result")
![Screen shots of build](./screenshots/8.png?raw=true "Result")
![Screen shots of build](./screenshots/9.png?raw=true "Result")

![Screen shots of build](./screenshots/10.png?raw=true "Result")
![Screen shots of build](./screenshots/11.png?raw=true "Result")
![Screen shots of build](./screenshots/12.png?raw=true "Result")

![Screen shots of build](./screenshots/13.png?raw=true "Result")
![Screen shots of build](./screenshots/14.png?raw=true "Result")
![Screen shots of build](./screenshots/15.png?raw=true "Result")
