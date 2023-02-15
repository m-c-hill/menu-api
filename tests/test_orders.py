def test_get_order_details(client, order_one):
    response = client.patch("api/v1.0/orders/1")
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json["success"] == True
    assert response_json["order"] == order_one


def test_get_order_details_raises_not_found(client):
    response = client.patch("api/v1.0/orders/100")
    response_json = response.get_json()

    assert response.status_code == 404
    assert response_json["success"] == False
    assert response_json["message"] == "Not found"


def test_place_order(client, new_order, new_order_response):
    response = client.post("api/v1.0/orders/1", new_order)
    response_json = response.get_json()

    assert response.status_code == 201
    assert response_json["success"] == True
    assert response_json["new_order"] == new_order_response

    # Also, need to check that new order exists in the database (id: 2?)


def test_cancel_order(client, cancelled_order_response):
    response = client.patch("api/v1.0/orders/1")
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json["success"] == True
    assert response_json["cancelled_order"] == cancelled_order_response
