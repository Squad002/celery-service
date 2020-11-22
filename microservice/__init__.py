from connexion.resolver import RestyResolver
from flask_mail import Mail
from config import config, Config
from celery import Celery

import connexion

mail = Mail()
celery = Celery(
    __name__,
    broker=Config.CELERY_BROKER_URL,
    include=["microservice.api.tasks"],
)
celery.autodiscover_tasks(["microservice.api.tasks"], force=True)


def create_app(config_name, updated_variables=None):
    connexion_app = connexion.App(__name__, specification_dir="../")

    # Get the underlying Flask app instance and put config in it
    flask_app = connexion_app.app
    flask_app.config.from_object(config[config_name])

    if updated_variables:
        flask_app.config.update(updated_variables)

    config[config_name].init_app(flask_app)
    context = flask_app.app_context()
    context.push()

    celery.conf.update(flask_app.config)
    mail.init_app(app)

    # Load APIs
    connexion_app.add_api("openapi.yml", resolver=RestyResolver("microservice.api"))
    flask_app.logger.info("Booting up")

    return flask_app, connexion_app
