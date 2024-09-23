from source.pizza import Pizza

class Order:
    """
    An order of pizzas. Has a cost and can be paid.
    """
    def __init__(self):
        """
        Initialize an empty order.

        :param self: The order.
        :type self: Order
        """
        self.pizzas = []
        self.cost = 0
        self.paid = False

    def __str__(self):
        """
        Return a string representation of the order.

        :param self: The order.
        :type self: Order
        :return: String representation of the order.
        :rtype: str
        """     
        # header  
        stringOrder = """Customer Requested:"""
        # add a row for every pizza
        for pizza in self.pizzas:
            stringOrder += str(pizza)

        return stringOrder
    
    def input_pizza(self, crust, sauce, cheese, toppings):
        """
        Add a new pizza to the order and update cost.

        :param self: The order.
        :type self: Order
        :param crust: Crust of the pizza.
        :type crust: str
        :param sauce: Sauce for the pizza.
        :type sauce: list of str
        :param cheese: Cheese on the pizza.
        :type cheese: str
        :param toppings: Toppings of pizza.
        :type toppings: list of str
        :return: Cost of order after adding pizza.
        :rtype: int
        """
        # create a new pizza
        inputPizza = Pizza(crust, sauce, cheese, toppings)
        # add to list of pizzas and update cost
        self.pizzas.append(inputPizza)
        self.cost += inputPizza.cost()
    
    def order_paid(self):
        """
        Pay the order and set the order to paid.
        
        :param self: The order.
        :type self: Order
        :return: The status of the order after being paid.
        :rtype: str
        """
        # set the order to paid
        self.paid = True
