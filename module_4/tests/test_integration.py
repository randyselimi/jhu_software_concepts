import pytest
from source.order import Order
from tests.test_order import example_order_empty
from tests.test_pizza import example_pizza_simple_data, example_pizza_simple, example_pizza_complex_data, example_pizza_complex, example_pizza_most_complex_data, example_pizza_most_complex

@pytest.mark.order
def test_order_input_pizza_thrice(example_order_empty, example_pizza_simple_data, example_pizza_complex_data, example_pizza_most_complex_data):
    example_order_empty.input_pizza(example_pizza_simple_data["crust"], example_pizza_simple_data["sauce"], example_pizza_simple_data["cheese"], example_pizza_simple_data["toppings"])
    example_order_empty.input_pizza(example_pizza_complex_data["crust"], example_pizza_complex_data["sauce"], example_pizza_complex_data["cheese"], example_pizza_complex_data["toppings"])
    example_order_empty.input_pizza(example_pizza_most_complex_data["crust"], example_pizza_most_complex_data["sauce"], example_pizza_most_complex_data["cheese"], example_pizza_most_complex_data["toppings"])
    assert example_order_empty.cost == 48