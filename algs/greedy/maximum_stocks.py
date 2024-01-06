# The stock prices are given for `len(prices) days`, where `prices[i]` denotes the price of the stock on the ith day.
# Customer can buy at most i stock on the ith day. If the customer has `money` amount of money
# initially, find out the maximum number of stocks a customer can buy.
import collections


def maximum_stocks(prices: list[int], money: int) -> int:
    stocks_bought = 0
    Stock = collections.namedtuple("Stock", ["quantity", "price"])

    stocks = sorted(
        [Stock(p[0], p[1]) for p in enumerate(prices, start=1)], key=lambda s: s.price
    )

    for s in stocks:
        if money - (s.price * s.quantity) >= 0:
            money -= s.price * s.quantity
            stocks_bought += s.quantity
        else:
            quantity = money // s.price
            money -= s.price * quantity
            stocks_bought += quantity

    return stocks_bought


print(maximum_stocks([10, 7, 19], 45))
print(maximum_stocks([7, 10, 4], 100))
