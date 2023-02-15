from cafe_menu_backend.extensions import db
from cafe_menu_backend.models import Customer, Dish, Order, OrderItem


def insert_test_data():
    # ===============================
    #  Insert customer
    # ===============================

    customer = Customer(first_name="Matt", last_name="Hill")

    db.session.add(customer)
    db.session.commit()

    # ===============================
    #  Insert a selection of dishes
    # ===============================

    pizza = Dish(
        name="Pizza",
        description="Large margarita pizza",
        price=10.99,
        hot_or_cold="hot",
        category="mains",
        ingredients="Dough, cheese, tomato sauce",
    )

    burger = Dish(
        name="Burger",
        description="1/4 lb burger in sesame bun",
        price=8.99,
        hot_or_cold="hot",
        category="mains",
        ingredients="bread, beef, cheese, lettuce",
    )

    chips = Dish(
        name="Chips",
        description="Oven chips served with ketchup",
        price=3.99,
        hot_or_cold="hot",
        category="sides",
        ingredients="Potato",
    )

    ice_cream = Dish(
        name="Ice cream",
        description="Selection of chocolate and vanilla ice cream",
        price=5.99,
        hot_or_cold="cold",
        category="desserts",
        ingredients="Ice cream, wafer, chocolate sauce",
    )

    db.session.add_all([pizza, burger, chips, ice_cream])
    db.session.commit()

    # ===============================
    #  Place a dummy order
    # ===============================

    order = Order(customer=customer, total_price=18.97, payment_complete=True)
    order_item_1 = OrderItem(dish=burger, quantity=1)
    order_item_2 = OrderItem(dish=chips, quantity=2)
    order_item_3 = OrderItem(dish=ice_cream, quantity=1)
    order.order_items.append(order_item_1)
    order.order_items.append(order_item_2)
    order.order_items.append(order_item_3)

    db.session.commit()
