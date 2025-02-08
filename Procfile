web: gunicorn sk_interior.wsgi --log-file -
#or works good with external database
web: python manage.py migrate && gunicorn sk_interior.wsgi
