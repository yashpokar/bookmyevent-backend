# bookmyevent-backend
Bookmyevent backend

# installation
1. Create database name it anything you want

2. Hit in your console
```
git clone https://github.com/yashpokar/bookmyevent-backend.git
cd bookmyevent-backend/
pip install -e .
```

3. change your databse connection string config inside bookmyevent-backend/bookmyevent-backend/config.py
4. again in your console
5. install redis [https://redis.io/topics/quickstart] and run redis

```
python manage.py db migrate
python manage.py db upgrade
celery -A event.tasks.cekery worker --loglevel=info
```

in another console

```
python manage.py runserver
```
