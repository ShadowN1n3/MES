class ProductionOrder:

    def __init__(self, order_number, product_name, quantity):
        self.__order_number = order_number
        self.__product_name = product_name
        self.__quantity = quantity
        self.__produced_units = 0
        self.__started = False
        self.__finished = False

    def get_order_number(self):
        return self.__order_number

    def start(self):
        if not self.__started:
            self.__started = True
        else:
            raise Exception('Order number already started')

    def finish(self):
        if not self.__finished:
            self.__finished = True
        else:
            raise Exception('Order number already finished')

    def produce(self, units):
        if self.__started and not self.__finished:
            self.__produced_units += units

        else:
            raise Exception('Order is not in a state to produce units')

    def get_production_efficiency(self):
        if self.__finished:
            return self.__produced_units / self.__quantity * 100
        else:
            raise Exception('Cannot calculate efficiency for this order')

    def get_name(self):
        return self.__product_name
