#!/bin/sh

python manage.py makemigrations --settings=SDN.prodSettings
python manage.py migrate --settings=SDN.prodSettings
python manage.py makesuper --settings=SDN.prodSettings
gunicorn SDN.wsgi --bind=0.0.0.0:80
# docker service logs srv-captain--my-app --since 60m --follow
# python manage.py loaddata mozn.json
# python manage.py collectstatic
# uvicorn ahm4d.asgi:application --reload --port 80 --host 0.0.0.0


