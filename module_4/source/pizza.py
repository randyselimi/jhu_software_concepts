class Pizza:
    """
    A pizza which can has a configurable crust, sauce, cheese, and toppings. Belong to an order and has a variable cost.
    """    
    def __init__(self, crust, sauce, cheese, toppings):
        """
        Initialize a pizza with the given options

        :param self: The pizza.
        :type self: Pizza
        :param crust: Crust of the pizza.
        :type crust: str
        :param sauce: Sauce for the pizza.
        :type sauce: list of str
        :param cheese: Cheese on the pizza.
        :type cheese: str
        :param toppings: Toppings of pizza.
        :type toppings: list of str
        """    
        # create price mappings. no price for cheese
        self.crustCosts = {
            "thin": 5,
            "thick": 6,
            "gluten_free": 8,
        }
        self.sauceCosts = {
            "marinara": 2,
            "pesto": 3,
            "liv_sauce": 5,
        }
        self.cheeseCosts = {
            "mozzarella": 0,
        }
        self.toppingsCosts = {
            "pineapple": 1,
            "pepperoni": 2,
            "mushrooms": 3, 
        }
        # assign options
        self.crust = crust
        self.sauce = sauce
        self.cheese = cheese
        self.toppings = toppings
     
    def __str__(self):
        """
        Return a string representation of the pizza containing its crust, sauce, cheese, toppings, and cost.

        :param self: The pizza.
        :type self: Pizza
        :return: String representation of the pizza.
        :rtype: str
        """   
        return """Crust: {crust}, Sauce: {sauce}, Cheese: {cheese}, Toppings: {toppings}, Cost: {cost}""".format(crust = self.crust, sauce = self.sauce, cheese = self.cheese, toppings = self.toppings, cost = self.cost())

    def cost(self):
        """
        Return the cost of the pizza.

        :param self: The pizza.
        :type self: Pizza
        :return: Cost of pizza calculated from its options.
        :rtype: int
        """    
        crustCost = self.crustCosts[self.crust]
        sauceCost = sum([self.sauceCosts[s] for s in self.sauce])  # Sum for multiple sauces        
        cheeseCost = self.cheeseCosts[self.cheese] # 0
        toppingsCost = sum([self.toppingsCosts[t] for t in self.toppings])  # Sum for multiple toppings        
        return crustCost + sauceCost + cheeseCost + toppingsCost

