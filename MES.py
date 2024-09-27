import ProductionLine
import ProductionOrder
import MES_Utils


class MES:

    def __init__(self):
        self.__productionLines = []

    def add_production_line(self, name):
        self.__productionLines.append(ProductionLine.ProductionLine(name))

    def get_production_lines(self):
        for line in self.__productionLines:
            print(f"Produktionslinie: {line.get_production_line_name()}")

    def get_production_line(self, name):
        try:
            index = next(i for i, line in enumerate(self.__productionLines) if line.get_production_line_name() == name)
            return self.__productionLines[index]
        except StopIteration:
            return None

    def create_production_order(self, production_line_name, order_number, product_name, quantity):
        self.get_production_line(production_line_name).add_order(order_number, product_name, quantity)
        return None

    def produce_units(self, production_line_name):
        production_line = self.get_production_line(production_line_name)
        all_orders = production_line.get_orders()
        for order in all_orders:
            order_quantity = order.get_quantity()
            for i in range(1, order_quantity + 1):
                print("Start order with the number: ", order.get_order_number(), " | production line: ",
                      production_line_name)
                print("Object with the name: ", order.get_name(), " | number: ", i, " created")
                print()
        return


if __name__ == '__main__':
    mes = MES()
    mes.add_production_line("1")
    mes.add_production_line("2")

    # mes.get_production_lines()
    # mes.get_production_line("1")
    mes.create_production_order("1", 1, "test1", 1)
    mes.create_production_order("1", 2, "test2", 3)

    mes.produce_units("1")
