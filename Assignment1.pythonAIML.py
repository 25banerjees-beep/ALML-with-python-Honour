import sys 
from abc import ABC, abstractmethod
from dataclasses import dataclasses
from typing import List, Dict
class Item:
    name: str
    price: float
    quantity: int
class Order:
    @abstractmethod
    def get_details(self) -> int:
        return sum(item.quantity for item in self.items)
    @abstractmethod
    def pay(self , amount: float) -> None:
        pass
class CardPayment(PaymentMethod)
     def get_payment_details(self):
         print("Getting card payment details.")
         self.card_number = input("Enter card number:")
         self.card_holder = input("Enter card holder namw:")
         self.expiry_date = input("Enter expiry date (MM/YY):")
         def pay(self, amount: float) -> bool:
             print(f"Paying {amount} using card.")
             return True
class CardPayment(PaymentMethod)
        def get_payment_details(self):
         print("Getting UPI payment details.")
         self.UPI_id = input("Enter UPI id:")
         def pay(self, amount: float) -> bool:
             print(f"Paying {amount} using UPI.")
             return Trued
         
#paymentmethod - parent - abstract class
#-get_details
#-pay
#rajorupipayment - child
#rajorpayemnt-child
#stripeupipayment - child
#stripecardpayment - child
# AggregateFactoryPaymentMethod - factory class abstract
# -factory -dict
#-get_payment_object method
# rajorpayfactory - factory class
#stripefactory - factory class
class PaymentmethodFactory:
    factory = {
        "1": CardPayment
        "2".UpiPayment
    }
    def get_payment_object(cls, choice:str) -> PaymentMethod
        if choice in cls.factory:
            return cls.factory[choice]()
        raise ValueError(f"Unsupported payment metho: {choice}")
class PaymentAggregator:
    def_int_(self):
    self.name ="Stripe Payment Aggregator"
def select_payment_method()
    print("Select a payment method")
    print("1.Credit Card")
    print("1.UPI")
    choice = input("Enter your choice(1, 2 or 3) ")
    payment_method = PaymentMethodFactory.get_payment_object(choice) payment_method.get_payment_details 
    return payment_method
    def main():
    print("Welcome to the Order Processing System!")
    order_id = input("Enter order ID: ")
    items = process_order()
    if not items:
        print("No items were added to the order. Exiting.")
        sys.exit(1)
    order = Order(order_id, items)
    print(f"Total items: {order.total_items}")
    print(f"Grand total: {order.grand_total}")

    payment_method = select_payment_method()
    aggregator = PaymentAggregator()
    aggregator.process_payment(order.grand_total, payment_method)


if _name_ == "_main_":
    main()
                                                        