import pytest
from source.pizza import Pizza

@pytest.fixture
def example_pizza_simple_data():
    return {"crust": "thin", "sauce": ["marinara"], "cheese": "mozzarella", "toppings": ["pepperoni"]}
    
@pytest.fixture
def example_pizza_simple(example_pizza_simple_data):
    return Pizza(example_pizza_simple_data["crust"], example_pizza_simple_data["sauce"], example_pizza_simple_data["cheese"], example_pizza_simple_data["toppings"])

@pytest.fixture
def example_pizza_complex_data():
    return {"crust": "thick", "sauce": ["marinara", "pesto"], "cheese": "mozzarella", "toppings": ["pineapple", "mushrooms"]}
    
@pytest.fixture
def example_pizza_complex(example_pizza_complex_data):
    return Pizza(example_pizza_complex_data["crust"], example_pizza_complex_data["sauce"], example_pizza_complex_data["cheese"], example_pizza_complex_data["toppings"])

@pytest.fixture
def example_pizza_most_complex_data():
    return {"crust": "gluten_free", "sauce": ["marinara", "pesto", "liv_sauce"], "cheese": "mozzarella", "toppings": ["pepperoni", "pineapple", "mushrooms"]}
    
@pytest.fixture
def example_pizza_most_complex(example_pizza_most_complex_data):
    return Pizza(example_pizza_most_complex_data["crust"], example_pizza_most_complex_data["sauce"], example_pizza_most_complex_data["cheese"], example_pizza_most_complex_data["toppings"])

def test_pizza_init_simple(example_pizza_simple):
    newPizza = example_pizza_simple
    assert newPizza.crust == "thin"
    assert newPizza.sauce == ["marinara"]
    assert newPizza.cheese == "mozzarella"
    assert newPizza.toppings == ["pepperoni"]
    assert newPizza.cost() != 0

def test_pizza_init_complex(example_pizza_complex):
    newPizza = example_pizza_complex
    assert newPizza.crust == "thick"
    assert newPizza.sauce == ["marinara", "pesto"]
    assert newPizza.cheese == "mozzarella"
    assert newPizza.toppings == ["pineapple", "mushrooms"]
    assert newPizza.cost() != 0

def test_pizza_str_simple(example_pizza_simple):
    assert str(example_pizza_simple) == """Crust: thin, Sauce: ['marinara'], Cheese: mozzarella, Toppings: ['pepperoni'], Cost: 9"""
    
def test_pizza_str_complex(example_pizza_most_complex):
    assert str(example_pizza_most_complex) == """Crust: gluten_free, Sauce: ['marinara', 'pesto', 'liv_sauce'], Cheese: mozzarella, Toppings: ['pepperoni', 'pineapple', 'mushrooms'], Cost: 24"""

def test_pizza_cost_simple(example_pizza_simple):
    assert example_pizza_simple.cost() == 9

def test_pizza_cost_complex(example_pizza_most_complex):
    assert example_pizza_most_complex.cost() == 24

