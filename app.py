from microservice import create_app, celery
from dotenv import load_dotenv

import os

dotenv_path = os.path.join(os.path.dirname(__file__), ".env")
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)


app, connexion_app = create_app(os.getenv("FLASK_CONFIG") or "default")
app.logger.info("Booting finished")


@app.cli.command()
def deploy():
    """Run deployment tasks."""
    pass