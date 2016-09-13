from contact import *


class Supplier(Contact):

    all_orders = {}


    def order(self, order):


        self.__class__.all_orders.setdefault(self.email, [])
        self.__class__.all_orders[self.email].append(order)
