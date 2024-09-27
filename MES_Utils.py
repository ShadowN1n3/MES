import ProductionOrder


class MES_Utils:
    @staticmethod
    def get_order_by_number(production_line, order_number):
        for order in production_line:
            if order.order_number == order_number:
                return order
        return None

    @staticmethod
    def calculate_production_efficiency(order: ProductionOrder):
        if order.finish():
            return order.__produced_units / order.__quantity * 100
        else:
            raise Exception('Cannot calculate efficiency for this order')
