from tests.fixtures import app, client
from flask import current_app
from microservice.api.tasks import compute_restaurants_rating_average
import requests


def test_send_mail(client):
    res = client.post("/mails", json=mail)

    assert res.status_code == 204
    # TODO verify mail


def test_average_rating(client):
    requests.post(
        f"{current_app.config['URL_API_RESTAURANT']}/restaurants",
        json=restaurant,
        timeout=(3.05, 9.1),
    )

    requests.post(
        f"{current_app.config['URL_API_RESTAURANT']}/reviews",
        json=review,
        timeout=(3.05, 9.1),
    )

    requests.post(
        f"{current_app.config['URL_API_RESTAURANT']}/reviews",
        json=review2,
        timeout=(3.05, 9.1),
    )

    requests.post(
        f"{current_app.config['URL_API_RESTAURANT']}/reviews",
        json=review3,
        timeout=(3.05, 9.1),
    )

    compute_restaurants_rating_average()

    updated = requests.get(
        f"{current_app.config['URL_API_RESTAURANT']}/restaurants/1",
        timeout=(3.05, 9.1),
    ).json()
    
    assert updated["average_rating"] == 4


mail = dict(
    html_body="<h1>Nice</h1>",
    recipients=[
      "gino@mail.com"
    ],
    sender="prova@mail.com",
    subject="Covid info",
    text_body="You are infected! Prepare to die"
)

restaurant = dict(
    name="Trattoria da Fabio",
    phone="555123456",
    lat=40.720586,
    lon=10.10,
    time_of_stay=30,
    cuisine_type="ETHNIC",
    precautions=["Amuchina"],
    opening_hours=12,
    closing_hours=18,
    operator_id=1,
)

review = dict(
    rating=3,
    message="fantastic",
    restaurant_id=1,
    user_id=1,
)

review2 = dict(
    rating=4,
    message="nice",
    restaurant_id=1,
    user_id=2,
)

review3 = dict(
    rating=5,
    message="super",
    restaurant_id=1,
    user_id=3,
)