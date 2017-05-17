# mysite
personal blog powered by Django


# Demo
https://ooooo.io

# How to use

```
git clone https://github.com/crasker/mysite.git

cd mysite

pip install -r requirements.txt  (should execute within your python virtualenv)

python manage.py makemigration

python manage.py migrate

python manage.py createsuperuser

python manage.py runserver

```
 > if you want to deploy your blog with nginx and uwsgi
 > you can use uwsgi --ini mysite.ini to start uwsgi and update nginx config which in conf dir.
