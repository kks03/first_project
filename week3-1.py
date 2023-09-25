#week3-1

class Customer:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance
    def __str__(self):
        return f"{self.name}({self.balance}원)"
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        return self.balance
    def deposit(self, amount):
        self.balance += amount
        return self.balance
if __name__ == '__main__':
    c1 = Customer('Bill')
    c2 = Customer('Steve', 50000)
    c3 = Customer('Tim', 100000)
    print(c1, c2, c3)
    c1.deposit(50000)
    c2.deposit(30000)
    c3.withdraw(100000)
    print(c1, c2, c3)
    c2.withdraw(1000000)
    print(c1, c2, c3)

#week3-2

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Name: {self.name}, Age: {self.age}"
class Dog(Animal):
    def bark(self, n):
        for _ in range(n):
            print("bark!")
    def human_age(self):
        return self.age * 4
class Cat(Animal):
    def meow(self, n):
        for _ in range(n):
            print("meow~")
    def human_age(self):
        return self.age * 4
if __name__ == '__main__':
    popo = Dog('popo', 10)
    popo.bark(3)
    print(popo)
    print('사람 나이로 환산 :', popo.human_age())
    pipi = Cat('pipi', 5)
    pipi.meow(4)
    print(pipi)
    print('사람 나이로 환산 :', pipi.human_age())

#week3-3

class Item:
    count = 0
    def __init__(self, t, p):
        self.t = t
        self.p = p
        Item.count += 1
    def __str__(self):
        return f'제목: {self.t}, 가격: {self.p}'
    def getprice(self):
        print(f'* {self.t} 의 가격은 {self.p} 원 입니다.')
class Book(Item):
    def __init__(self, t, p, pages, au):
        super().__init__(t, p)
        self.pages = pages
        self.au = au
    def __str__(self):
        return super().__str__() + f', 페이지 수: {self.pages}, 저자: {self.au}'
class Magazine(Item):
    def __init__(self, t, p, m):
        super().__init__(t, p)
        self.m = m
    def __str__(self):
        return super().__str__() + f', 출간 월: {self.m}'
if __name__ == '__main__':
    b1 = Book('소나기', 10000, 124, '황순원')
    b2 = Book('메밀꽃 필 무렵', 15000, 142, '이효석')
    b3 = Book('난쏘공', 12000, 112, '조세희')
    magazine1 = Magazine('보그', 11000, 9)
    magazine2 = Magazine('싱글즈', 13000, 8)
    print('', b1, '\n', b2, '\n', b3, '\n', magazine1, '\n', magazine2)
    print('총', Item.count, '권')
    b2.getprice()
    magazine1.getprice()
    b1.getprice()
