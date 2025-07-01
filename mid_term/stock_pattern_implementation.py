from abc import ABC, abstractmethod

class Observer(ABC):
    @abstractmethod
    def update(self, symbol, price):
        pass
class Subject(ABC):
    @abstractmethod
    def attach(self,observer):
        pass
    @abstractmethod
    def detach(self, observer):
        pass
    @abstractmethod
    def notify(self):
        pass

class Stock(Subject):
    def __init__(self, symbol, price):
        self._observers = set()
        self.symbol = symbol
        self._price = price
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.add(observer)
    
    def detach(self, observer):
        if observer in self._observers:
            self._observers.remove(observer)
    
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        if self._price != value:
            self._price = value
            self.notify()
    
    def notify(self):
        for observer in self._observers:
            observer.update(self.symbol, self._price)

        

# Test Input
class PriceAlert(Observer):
    def update(self, symbol, price):
        print(f"ALERT: {symbol} now at {price}")

apple = Stock("AAPL", 150)
alert = PriceAlert()
apple.attach(alert)
apple.price = 155  # Should trigger alert