import ProductionLine


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


if __name__ == '__main__':
    mes = MES()
    mes.add_production_line("1")
    mes.add_production_line("2")

    mes.get_production_lines()
    mes.get_production_line("1")
