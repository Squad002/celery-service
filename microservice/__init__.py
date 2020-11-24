import connexion
from connexion.resolver import RestyResolver
from celery import Celery
from flask_mail import Mail
from config import config, Config


mail = Mail()
celery = Celery(
    __name__,
    broker=Config.CELERY_BROKER_URL,
    include=["microservice.api.tasks"],
)
celery.autodiscover_tasks(["microservice.api.tasks"], force=True)


def create_app(config_name):
    connexion_app = connexion.App(__name__, specification_dir="../")

    # Get the underlying Flask app instance and put config in it
    flask_app = connexion_app.app
    flask_app.config.from_object(config[config_name])

    config[config_name].init_app(flask_app)
    context = flask_app.app_context()
    context.push()

    celery.conf.update(flask_app.config)
    mail.init_app(flask_app)

    # Load APIs
    connexion_app.add_api("openapi.yml", resolver=RestyResolver("microservice.api"))
    flask_app.logger.info("Booting up")

    return flask_app, connexion_app
