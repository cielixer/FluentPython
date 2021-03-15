from collections import namedtuple

# namedtuple : 튜플에 이름을 추가한 형태

# 각 필드 들은 띄어쓰기로 문자열 이름(당연히 변수 이름 생성 규칙)
City = namedtuple('City', 'name country population coordinates')

# 각 필드가 들어감
#             name   country pop      coordinates
tokyo = City("Tokyo", 'JP', 36.933, (35.68, 139.69))

# 구조체 마냥 tokyo라는 객체에 멤버변수로 값들이 존재함
# 인터프리터(동적언어)의 성질을 이용한듯, string->token
print(tokyo.name)
print(tokyo.country)
print(tokyo.population)
print(tokyo.coordinates)

# 뿐만 아니라 일반 tuple 처럼 인덱싱도 가능함
print(tokyo[1])

# 특별 변수?로 클래스 속성을 나타내는
print(City._fields)  # ('name', 'country', 'population', 'coordinates')

LatLong = namedtuple('LatLong', 'lat long')
delhi_data = ('Delhi', 'IN', 21.935, LatLong(28.6, 77.2))

# iterable한 객체를 통해 make(create) 패턴도 사용 가능
delhi = City._make(delhi_data)

# 또한 collection.OrderedDict의 형태로(순서 있는 dict?) 출력 가능
print(delhi._asdict())

# OrderedDict의 형태를 사용하면 일반 dict처럼 항목들을 iterate할수 있다.
for key, value in delhi._asdict().items():
    print(key + ':', value)  # 하나에 한줄씩 출력

# 일반적인 리스트의 특별 메서드 중 불변성에 위반하는 것들을 제외하고 다 동작한다.
