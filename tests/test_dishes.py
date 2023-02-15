def test_get_dish_list(client, all_dishes):
    response = client.get("api/v1.0/dishes")
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json["success"] == True
    assert response_json["dishes"] == all_dishes
    assert response_json["dish_count"] == len(all_dishes)


def test_get_dish_list_by_category(client, mains_dishes):
    response = client.get("api/v1.0/dishes/category/mains")
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json["success"] == True
    assert response_json["dishes"] == mains_dishes
    assert response_json["dish_count"] == len(mains_dishes)


def test_get_dish_list_by_category_raises_not_found(client):
    response = client.get("api/v1.0/dishes/category/cocktails")
    response_json = response.get_json()

    assert response.status_code == 404
    assert response_json["success"] == False
    assert response_json["message"] == "Not found"


def test_get_dish_by_id(client, pizza):
    response = client.get("api/v1.0/dishes/1")
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json["success"] == True
    assert response_json["dish"] == pizza


def test_get_dish_by_id_raises_not_found(client):
    response = client.get("api/v1.0/dishes/100")
    response_json = response.get_json()

    assert response.status_code == 404
    assert response_json["success"] == False
    assert response_json["message"] == "Not found"


def test_add_dish_to_menu(client, new_dish, new_dish_response):
    response = client.post("api/v1.0/dishes", json=new_dish)
    response_json = response.get_json()

    assert response.status_code == 201
    assert response_json["success"] == True
    assert response_json["new_dish"] == new_dish_response


def test_delete_dish_from_menu(client, all_dishes):
    response = client.delete("api/v1.0/dishes/1")
    response_json = response.get_json()

    assert response.status_code == 200
    assert response_json["success"] == True
    assert response_json["deleted"] == 1

    # Check the dish has actually been removed
    response = client.get("api/v1.0/dishes")
    response_json = response.get_json()
    all_dishes.pop(0)

    assert response.status_code == 200
    assert response_json["success"] == True
    assert response_json["dishes"] == all_dishes
    assert response_json["dish_count"] == len(all_dishes)


def test_delete_dish_from_menu_raises_not_found(client):
    response = client.delete("api/v1.0/dishes/100")
    response_json = response.get_json()

    assert response.status_code == 404
    assert response_json["success"] == False
    assert response_json["message"] == "Not found"
