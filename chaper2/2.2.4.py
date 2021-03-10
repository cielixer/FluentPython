# 시퀸스를 생성하고 초기화 할 때 listcomp를 사용할 수 있지만,
# 시퀸스를 통째로 만들기 싫으면 iterator protocol을 이용할 수 있다.
# 이 방법은 하나씩 만드는 방법으로 메모리를 더 적게 사용한다.

symbols = 'a$2%?ⅧⅨ♞♟😀😉'

# generator comprehension은 listcomp와 같은 구문을 사용하지만 [대괄호] 대신 (괄호)를 사용
print(tuple(ord(s) for s in symbols))

# 솔직히 뭔차이노 했는데 다음 예제를 보면 약간 이해할 수 있었다.
# 편한 이해를 위해 '코루틴과 비슷한 형태'라고 생각하기로 했다.
# 만들고 주고 만들고 주고를 사용하는 것 같다

colors = ['black', 'white']
sizes = ['S', 'M', 'L']

for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
    print(tshirt)

# 이렇게 하면 단순히 for문에 전달할 목적으로
# ㅈㄴ 큰 리스트를 만드는 것을 피할 수 있다.

# generator comprehension은 generator를 만드는 표현식이라고 할 수 있다.
# 자세한건 14장에서

# 정리하자면 데이터를 들고 있어야 하면 listcomp
# 들고 있을 이유가 없다면 gencomp 를 사용하자.
