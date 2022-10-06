release: python manage.py migrate && python manage.py loaddata initial_wishlist_data.json
web: gunicorn project_django.wsgi --log-file -