# installation steps:
- install Git
- install Python
- install Sqlite
```Shell
$ pip install --user pipenv
$ git clone https://github.com/ahbali/manageit.git
$ cd manageit
$ pipenv install
$ pipenv shell
$ python manage.py migrate
$ python manage.py createsuperuser
$ python manage.py runserver
```
- admin page : http://127.0.0.1:8000/admin/
- login with the superuser account you created.
- main site : http://127.0.0.1:8000/

# updating steps:
```Shell
$ cd manageit
$ git pull
$ pipenv install
$ pipenv shell
$ python manage.py migrate
$ python manage.py runserver
```
- admin page : http://127.0.0.1:8000/admin/
- login with the superuser account you created.
- main site : http://127.0.0.1:8000/