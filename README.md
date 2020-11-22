[![Build Status](https://travis-ci.org/Squad002/celery-service.svg?branch=main)](https://travis-ci.org/Squad002/celery-service)
[![Coverage Status](https://coveralls.io/repos/github/Squad002/celery-service/badge.svg?branch=main)](https://coveralls.io/github/Squad002/celery-service?branch=main)

# GoOutSafe - Celery microservice

### Local
    # Install Dependencies
    pip install -r requirements/dev.txt

    # Deploy
    flask deploy

    # Run 
    export FLASK_APP="app.py"
    export FLASK_ENV=development
    flask run

### Docker Image
    docker build -t celery-service:latest . 
    docker run -p 5000:5000 celery-service 

## Tests with coverage
Inside user-service run (it will automatically use the configuration in pyproject.toml):

    pytest