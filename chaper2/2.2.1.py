# List comprehension을 이해하기 위해 유니코드->ascii걸러내기->숫자의 변환을 보자
symbols = 'a$2%?ⅧⅨ♞♟😀😉'

codes = []
for symbol in symbols:
    char_val = ord(symbol)
    if char_val > 127:
        codes.append(char_val)

print(codes)  # [8551, 8552, 9822, 9823, 128512, 128521]

# 여기서 List comprehension을 이용해서 간다명료하게 표현을 한다면

codes = [ord(s) for s in symbols if ord(s) > 127]
print(codes)  # [8551, 8552, 9822, 9823, 128512, 128521]

# 하지만 남용해서는 안된다... 두줄이 넘어가거나 너무 길면 가독성 측면에서 좋지 않음
# 지능형 리스트를 사용해서 if를 넣는다던지 해서 filter와 map의 기능을 수행할수 있다.
# 위와 같은 코드를 filter와 map을 이용한다면
codes = list(filter(lambda c: c > 127, map(ord, symbols)))
print(codes)  # [8551, 8552, 9822, 9823, 128512, 128521]

# map은 ord라는 함수를 통해 symbols 리스트를 mapping을 하고
# filter는 lambda를 통해 list의 요소들을 filtering을 하게 된다.
# 이해할 순 있지만... 가독성이 너무 떨어진다.
