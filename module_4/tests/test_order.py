import pytest
from source.order import Order
from tests.test_pizza import example_pizza_simple_data, example_pizza_simple, example_pizza_complex_data, example_pizza_complex, example_pizza_most_complex_data, example_pizza_most_complex

@pytest.fixture
def example_order_empty():
    return Order()

@pytest.fixture
def example_order_single(example_pizza_simple):
    pizzas = [example_pizza_simple]
    cost = example_pizza_simple.cost()
    order = Order()
    order.pizzas = pizzas
    order.cost = cost
    return order

@pytest.fixture
def example_order_multiple(example_pizza_simple, example_pizza_complex, example_pizza_most_complex):
    pizzas = [example_pizza_simple, example_pizza_complex, example_pizza_most_complex]
    cost = example_pizza_simple.cost() + example_pizza_complex.cost() + example_pizza_most_complex.cost()
    order = Order()
    order.pizzas = pizzas
    order.cost = cost
    return order

def test_order_init_empty(example_order_empty):
    newOrder = example_order_empty
    assert newOrder.pizzas == []
    assert newOrder.cost == 0
    assert newOrder.paid == False

def test_order_init_single(example_order_single, example_pizza_simple):
    newOrder = example_order_single
    assert newOrder.pizzas == [example_pizza_simple]
    assert newOrder.cost == 9
    assert newOrder.paid == False

def test_order_init_multiple(example_order_multiple, example_pizza_simple, example_pizza_complex, example_pizza_most_complex):
    newOrder = example_order_multiple
    assert newOrder.pizzas == [example_pizza_simple, example_pizza_complex, example_pizza_most_complex]
    assert newOrder.cost == 48
    assert newOrder.paid == False

def test_order_str_empty(example_order_empty):
    assert str(example_order_empty) == """Customer Requested:"""

def test_order_str_single(example_order_single):
    assert str(example_order_single) == """Customer Requested:Crust: thin, Sauce: ['marinara'], Cheese: mozzarella, Toppings: ['pepperoni'], Cost: 9"""

def test_order_str_multiple(example_order_multiple):
    assert str(example_order_multiple) == """Customer Requested:Crust: thin, Sauce: ['marinara'], Cheese: mozzarella, Toppings: ['pepperoni'], Cost: 9Crust: thick, Sauce: ['marinara', 'pesto'], Cheese: mozzarella, Toppings: ['pineapple', 'mushrooms'], Cost: 15Crust: gluten_free, Sauce: ['marinara', 'pesto', 'liv_sauce'], Cheese: mozzarella, Toppings: ['pepperoni', 'pineapple', 'mushrooms'], Cost: 24"""
    
def test_order_input_pizza_once(example_order_empty, example_pizza_simple_data):
    example_order_empty.input_pizza(example_pizza_simple_data["crust"], example_pizza_simple_data["sauce"], example_pizza_simple_data["cheese"], example_pizza_simple_data["toppings"])
    assert example_order_empty.cost == 9

def test_order_input_pizza_twice(example_order_empty, example_pizza_simple_data, example_pizza_complex_data):
    example_order_empty.input_pizza(example_pizza_simple_data["crust"], example_pizza_simple_data["sauce"], example_pizza_simple_data["cheese"], example_pizza_simple_data["toppings"])
    example_order_empty.input_pizza(example_pizza_complex_data["crust"], example_pizza_complex_data["sauce"], example_pizza_complex_data["cheese"], example_pizza_complex_data["toppings"])
    assert example_order_empty.cost == 24

def test_order_input_pizza_thrice(example_order_empty, example_pizza_simple_data, example_pizza_complex_data, example_pizza_most_complex_data):
    example_order_empty.input_pizza(example_pizza_simple_data["crust"], example_pizza_simple_data["sauce"], example_pizza_simple_data["cheese"], example_pizza_simple_data["toppings"])
    example_order_empty.input_pizza(example_pizza_complex_data["crust"], example_pizza_complex_data["sauce"], example_pizza_complex_data["cheese"], example_pizza_complex_data["toppings"])
    example_order_empty.input_pizza(example_pizza_most_complex_data["crust"], example_pizza_most_complex_data["sauce"], example_pizza_most_complex_data["cheese"], example_pizza_most_complex_data["toppings"])
    assert example_order_empty.cost == 48

def test_order_order_paid_empty(example_order_empty):
    example_order_empty.order_paid()
    assert example_order_empty.paid == True

def test_order_order_paid_multiple(example_order_multiple):
    example_order_multiple.order_paid()
    assert example_order_multiple.paid == True