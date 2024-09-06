import ProductionLine
import ProductionOrder


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
        for production_line in self.__productionLines:
            all_orders = production_line.get_orders()
            for order in all_orders:
                print(order.get_name())
                print(order.quantity)
        return


if __name__ == '__main__':
    mes = MES()
    mes.add_production_line("1")
    # mes.add_production_line("2")

    mes.get_production_lines()
    # mes.get_production_line("1")
    mes.create_production_order("1", 1, "test", 100)

    mes.produce_units("1")


