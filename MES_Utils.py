class mes_utils:
    @staticmethod
    def get_order_by_number(production_line, order_number):
        for order in production_line:
            if order.order_number == order_number:
                return order
        return None


    @staticmethod
    def calculate_production_efficiency(order):
        if order.status != 'finished':
            raise ValueError(f"Produktion für Bestellung '{order['order_number']}' ist noch nicht abgeschlossen.")

        efficiency = 0.90
        return efficiency * 100