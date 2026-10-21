import random
from __future__ import annotations


class ATM:
    def __init__(self, balance: int = 0):
        self.__balance = balance

        min_random_id = 0
        max_random_id = 99999
        self.__id = random.randint(min_random_id, max_random_id)

    def __gt__(self, other: ATM):
        return self.__balance > other.get_balance()

    def __eq__(self, other: ATM):
        return self.__balance == other.get_balance()

    def __str__(self):
        print("Баланс:", self.__balance)
        return str(self.__balance)

    def get_balance(self):
        return self.__balance

    def __add__(self, other_atm):
        other_atm_balance = other_atm.get_balance()
        sum_balance = self.__balance + other_atm_balance

        new_atm = ATM(sum_balance)
        return new_atm
