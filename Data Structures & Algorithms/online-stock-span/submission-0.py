class StockSpanner:

    def __init__(self):
        self.stocks = []

    def next(self, price: int) -> int:
        self.stocks.append(price)
        return self.span(price)
    def span(self, price):
        p = len(self.stocks) - 1
        count = 0
        while p >= 0 and self.stocks[p] <= price:
            p -= 1
            count += 1
        return count

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)