#!/bin/sh
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

exec celery -A gooutsafe.celery worker -l DEBUG -E -B