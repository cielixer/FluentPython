import collections # list, tuple, set, dict 같은 built-in container들을 특수화 시킨 패키지

# 이름이 있는 tuple을 클래스처럼 정의(alias?) 파라미터의 이름으로 순서 상관없이 초기화도 가능
# tuple의 특징을 거의 대부분 가지고 있어서 그런지 uppacking도 가능함
Card = collections.namedtuple('Card', ['rank', 'suit'])

# FrenchDeck class 는 암묵적으로(default) object를 상속받음, 그러므로 특별 매서드들을 오버라이딩해서 사용할 수 있게 된다.
class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA') # list(...)를 사용해서 character 하나씩 리스트로 넣을 수 있음
    suits = 'spades diamonds clubs hearts'.split() # ' '(띄어쓰기) 단위로 문자열을 쪼갤 수 있음 (None : ' ' 이고 구분자를 설정 할수 있음)

    def __init__(self):
        # 이런 방식으로 이중 for loop를 돌려서 52종류의 모든 카드를 구현
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]

    def __len__(self): # len 연산자? 오버로딩 가능
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position] # [대괄호] 연산자 오버로딩
    
c = Card(20, 30)
print(c) # Card(rank=20, suit=30)

c2 = Card(suit=30, rank=20)
print(c2) # Card(rank=20, suit=30)

c_suit, c_rank = c
print(c_suit, c_rank) # 20 30

test_deck = FrenchDeck()
print(test_deck.ranks)

print(test_deck.suits)

# FrenchDeck 클래스는 __getitem___ 연산자 오버로딩을 사용해서 시퀸스를 다루는 함수들을 사용할 수 있다.
from random import choice
print(choice(test_deck)) # 동적 타입 언어라서 이런게 가능한것 같다(인터프리터, 스크립트 언어, 유사언어ㄹㅇㅋㅋ)

# 또한 시퀸스(리스트)의 형태를 가지고 있기 때문에 리스트에서 사용하는 거의 모든 기능들을 사용할 수 있다.
print(test_deck[:3])
print(test_deck[3:7])
print(test_deck[12::13]) # skip elemenst, 12부터 13개 다음 것들로 skip 하면서 가져옴
                         # 이렇게 되면 12번 인덱스(13번째인 'A')에서 카드는 13장씩 있으니까 A를 하나씩 다 들고 옴
                         # 이거 이외에도 많은듯
    
# 시퀸스이니까 당연히 for-loop도 가능하다 & 당연히 reversed도 가능
for card in test_deck: #doctest: +ELLIPSIS => 이걸 사용하면 interactive mode 또는 콘솔에서 다양한 기능들 표시? 로그
                                                # 등을 print 할 수 있음... 자세한건 나중에
    pass # print(card) # ... Card(rank='?', suit='???') ... 따위로 출력됨 (doctest:ELLIPSIS 옵션을 사용하면, numpy 생각하면 됨)

# 또한 시퀸스 이기 때문에(__getitem__) in 연산자도 사용할 수 있다
print(Card('Q', 'hearts') in test_deck)
print(Card('Q', 'eee') in test_deck)
# __contains__ 특별 메서드가 없다면 차례대로 하나씩 검사하게 됨(hash-tree나 Red-Black tree같이 검색에서 좋은 성능을 보장하고 싶다면 하자)

suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)

def spade_high(card):
    # card의 rank (2~JQKA)의 인덱스(위치)를 찾아서 
    rank_value = FrenchDeck.ranks.index(card.rank)
    # 인덱스를 곱해서 사용 카드의 높고 낮음을 찾음
    return rank_value * len(suit_values) + suit_values[card.suit]

# spade_high 함수를 key로 사용해서 정렬
for card in sorted(test_deck, key=spade_high):
    print(card) # 숫자가 우선이고, 같으면 suit_values에 따라서 출력이 됨
