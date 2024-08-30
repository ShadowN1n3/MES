import ProductionOrder


class ProductionLine:

    def __init__(self, name: int):
        self.__name = name
        self.__productionLineOrders = []

    def add_order(self, orderNumber, productionName, quantity):
        self.__productionLineOrders.append(ProductionOrder.ProductionOrder(orderNumber, productionName, quantity))

    def get_production_line_name(self):
        return self.__name

    def get_orders(self):
        return self.__productionLineOrders

