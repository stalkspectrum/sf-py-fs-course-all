'''
class C:
    def __call__(self):
        print('Это объект класса C')
obj = C()
def f():
    print('Это функция f')
obj()
f()

print(obj())
'''
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __str__(self):
        return self.rank + ' ' + self.suit
class Deck:
    def __init__(self):
        self._cards = []
        ranks = ['7', '8', '9', '10', 'Валет', 'Дама', 'Король', 'Туз']
        for suit in ['пик', 'треф', 'бубей', 'черв']:
            for rank in ranks:
                self._cards.append(Card(rank, suit))
    def __len__(self):
        return len(self._cards)
    def __getitem__(self, position):
        return self._cards[position]
deck = Deck()
print(len(deck))
print(str(deck[20]))
print(str(deck[-1]))
import random
print(random.choice(deck))
