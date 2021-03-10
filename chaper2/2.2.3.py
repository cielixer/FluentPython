# 데카르트 곱 : 두 리스트에서 모든 항목 쌍을 만드는 연산

# 옷을 종류를 만드는 데카르트 곱을 만들어 보자
# 색상은 black, white, 사이즈는 S, M, L이라고 하면

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

tshirts = [(color, size) for color in colors for size in sizes]

# 모든 조합 쌍들이 튜플로 나온다.
# [('black', 'S'), ('black', 'M'), ('black', 'L'), ('white', 'S'), ('white', 'M'), ('white', 'L')]
print(tshirts)

# 앞서 FrenchDeck의 경우에 데카르트 곱을 이용해서 52장의 카드들을 만들었다.
# 1.1.py를 살펴보자
