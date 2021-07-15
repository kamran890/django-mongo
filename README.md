#  Django-Mongo

Integration of Mongo DB with Django

# Quick Deployment (Ubuntu)

* Open terminal

* Update Software Repositories

`sudo apt-get update`

* In home directory clone django-mongo

`sudo su`

`apt install git`

`git clone https://github.com/kamran890/django-mongo.git`

* Go to django-mongo directory

`cd django-mongo`

* Copy .env.example to new .env file

`cp .env.example .env`

* Open .env file and add env variables.

```
DEBUG=TRUE
DB_USER=DB_USER
DB_PASS=DB_PASS
DB_HOST=DB_HOST
DB_NAME=DB_NAME
SECRET_KEY=SECRET_KEY
```

* Run shell script

`./docker-deploy.sh`

# Update

* Open terminal and go to django-mongo directory and run following script

`./scripts/update.sh`
