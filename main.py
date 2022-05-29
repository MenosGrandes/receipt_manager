import dataclasses
import pandas as pd
from datetime import datetime


class Price:
    value: float
    isPromotion: bool = False

    def __init__(self, _v, _isP=False):
        self.value = _v
        self.isPromotion = _isP

    def __repr__(self):
        return f"{self.value}"

    def __str__(self):
        return f"{self.value}"


@dataclasses.dataclass
class Item:
    name: str
    price: Price


@dataclasses.dataclass
class Store:
    name: str

    def __repr__(self):
        return f"{self.name}"

    def __str__(self):
        return f"{self.name}"


class Receipt:
    items: pd.DataFrame
    date: datetime
    store: Store

    def __init__(self, _items, _date, _store):
        self.items = pd.DataFrame(data=_items)
        self.date = _date
        self.store = _store

    def __repr__(self):
        return f"\n {self.date} {self.store} \n {self.items} \n"

    def __str__(self):
        return f"\n {self.date} {self.store} \n {self.items} \n"

    def sum(self):
        return self.items.sum(axis=0).at["price"]


class Receipts:
    receipts: list[Receipt]

    def __init__(self, _r):
        self.receipts = _r

    def __repr__(self):
        return f"{self.receipts}"

    def __str__(self):
        return f"{self.receipts}"

    def getAll(self, item_name : str):
        a = []
        for r in self.receipts:
            print(r.items[r.items["name"] == item_name])


r = Receipt(
    [
        Item("Serek wiejski", Price(41.3)),
        Item("Skyr", Price(33.3)),
        Item("Mleko", Price(34.7)),
        Item("Cebula", Price(34.4)),
        Item("Mielone wolowe", Price(39.4)),
        Item("Szpinak", Price(213123.4)),
    ],
    datetime(2018, 4, 29, 17, 45, 2),
    Store("Lidl"),
)

r2 = Receipt(
    [
        Item("Serek wiejski", Price(41.3)),
        Item("Skyr", Price(2231.3)),
        Item("Mleko", Price(34.7)),
        Item("Cebula", Price(34.4)),
        Item("Mielone wolowe", Price(39.4)),
        Item("Szpinak", Price(213123.4)),
    ],
    datetime(2018, 4, 29, 17, 45, 2),
    Store("Lidl"),
)

a = Receipts([r, r2])
print(f"{a}")
a.getAll("Skyr")
# print(f"{a[0]}")
# sum = a[0].sum()
# print(f"{sum}")
