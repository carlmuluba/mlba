web: gunicorn mlba.wsgi --log-file -
release: python manage.py migrate
python manage.py collectstatic --noinput
manage.py migrate