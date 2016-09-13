from contact import *


class Supplier(Contact):

    all_orders = {}

    def order(self, order):
        self.all_orders.update({self.email: str(order})
