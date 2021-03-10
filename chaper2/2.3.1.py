# 레코드로서의 튜플을 보자면
# 항목의 수가 고정되어 있으며 항목의 순서가 중요하다.

import os
lax_coord = (33.9, -118.4)  # LA 공항 위도와 경도

# 도쿄에 대한 데이터
city, year, pop, chg, area = ('Tokyo', 2003, 32450, 0.66, 8014)

# 국가코드,여권번호
traveler_ids = [('USA', '31195855'), ('BRA', 'CE342567'), ('ESP', 'XDA205856')]

# 뭐 어떤 기준으로 대충 정렬해주는거 같다.
for passport in sorted(traveler_ids):
    print('%s/%s' % passport)

# 위에서 도쿄의 데이터와 passport로 for-loop를 돌릴 때
# tuple unpacking이라는 방식을 사용해서 값을 가져왔다.

# 튜플 언패킹은 반복 가능한 객체라면 다 사용할 수 있다.
# 왜 튜플이냐면 튜플의 형태로 가져오기 때문이다.
# 왜냐면 튜플의 소괄호()는 생략 가능하기 때문이라고 알고 있다.

latitude, longitude = lax_coord  # 병렬 할당
print(latitude, longitude)

# 병렬 할당을 사용하면 임시변수를 사용하지 않고 swap을 할 수 있다.
a, b = 10, 20

a, b = b, a  # swap

# 또한 개쩌는 기능중 하나로 튜플 앞에 *을 붙여 언패킹 할수 있다.
t = (20, 8)
quotient, remainder = divmod(*t)
print(quotient, remainder)

# 이게 진짜 개쩌는게 함수의 파라미터로 값을 넘길 때
# *하나만 붙여도 튜플에서 소괄호()가 사라지는 것같은 효과가 나타난다.

# 또한 언패킹에서 무시할 내용으로 _를 사용하는 것으로
# 조건부로 빼오는 것도 가능하다.

_, filename = os.path.split('/home/luciano/.ssh/idrsa.pub')

# 파이썬의 개쩌는 *을 사용해서 초과항목을 잡을 수 있다.

a, b, *rest = range(5)
print(a, b, rest)  # 0 1 [2, 3, 4]

# 만약 rest에 넣을게 없다면 빈 배열로 들어가게 된다.

# 또한 중간에도 들어갈 수 있다.

a, *body, b = range(5)  # 0 [1, 2, 3] 4
print(a, body, b)
a, *body, b, c = range(5)
print(a, body, b, c)  # 0 [1, 2] 3 4

# 당연하게도 *이 들어간게 여러개 있으면 안되(겠지?)
