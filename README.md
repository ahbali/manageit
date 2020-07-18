# installation steps:
- install python
- install Sqlite
- install Pipenv : 
```
pip install --user pipenv
git clone https://github.com/ahbali/manageit.git
cd managit
pipenv install
pipenv shell
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```
- go to : http://127.0.0.1:8000/admin/
- login with the superuser account you created.