# DRF Test for 0+X

## Installation

Once you clone this repository you should move to the project directory and install the project dependencies by running (it's better if you create a virtual environment first):
```sh
pip install -r requirements.txt
```

With all the dependencies successfully installed, create the database and its structure by running:
```sh
python manage.py migrate
```

Now you will need an user to perform some operations on the API (POST, PUT/PATCH, DELETE). It's ok to perform anonymous requests for GET and HEAD. You can create a super user by running:
```sh
python manage.py createsuperuser
```
You'll be prompted for email, username and password.

For running the server and start to use the service you can start the server by running:
```sh
python manage.py runserver
```

## Using the API

Refer to [Wiki](https://github.com/igorbelo/0plusxtest/wiki) of this project to check how to perform operations on the API.

## Report
### Time
I took about 3 hours to finish the task considering all enhancements (except #5 and this documentation).

### Enhancements for going production
- better authentication and permission system
- write tests
- serve uploaded images in cdn services such as s3, cloudfare...
- wouldn’t go with sqlite and choose a more consistent database
- for querying images would use a full-text search solution (elasticsearch or solr) depending on the complexity and scability needed...
- `django-filters` library is a good way to provide a generic mechanism to filter resources as well (multiple fields, type cast etc.)
- put database credentials and secrets in environment variables
