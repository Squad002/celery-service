#!/bin/bash
source venv/bin/activate
export FLASK_APP="app"

while true; do
    flask deploy
    if [[ "$?" == "0" ]]; then
        break
    fi
    echo Deploy command failed, retrying in 5 secs...
    sleep 5
done

python -m smtpd -n -c DebuggingServer localhost:8025 &
celery -A app.celery worker -l DEBUG -E -B &
exec gunicorn -b 0.0.0.0:5000 --access-logfile - --error-logfile - app:app 