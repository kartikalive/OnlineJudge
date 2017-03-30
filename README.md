# Online Judge
An Online Judge based on Django, Django-Rest-Framework and Docker.

## Install
```bash
$ git clone git@github.com:Lodour/OnlineJudge.git
$ cd OnlineJudge
$ virtualenv env --python=python3.5
$ source ./env/bin/activate

$ pip install -r requirements.txt
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
$ # Set your info here
$ python manage.py runserver
```

## Reference && Thanks
* [Django 1.10 Documents](http://docs.djangoproject.com/en/1.10/)
* [Django Rest Framework 3 Documents](http://www.django-rest-framework.org/)
* [QingdaoU-OnlineJudge](https://github.com/QingdaoU/OnlineJudge)
