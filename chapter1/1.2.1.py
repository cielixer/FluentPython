from math import hypot
# python의 math 모듈의 hypot
# hypot : Euclidean norm을 반환하는 함수


class Vector:
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y

    # 객체를 문자열로 표현하기 위한 특별 메서드
    # 이 클래스를 구현하지 않으면 <Vector object at 0x01...> 같은 꼴로 출력됨
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'

    # __repr__ vs __str__
    # __repr__는 implicit하게 일어나는 반면
    # __str__는 str 클래스로의 변환(casting)으로 explicit하게 일어남
    # a = Vector(1, 2)
    # a_str = str(a)

    # __str__이 구현되어 있지 않으면 인터프리터는 __repr__을 대신 호출하므로
    # 둘중 하나만 구현한다면 __repr__를 구현하자

    def __abs__(self):
        return hypot(self.x, self.y)

    # for, while loop같은 곳에서 쓰기 위해서 사용됨
    # __bool__이 없다면 __len__을 사용해서 True/False 판별
    # __bool__, __len__이 둘다 없다면 존재하는 객체로 판단해서 항상 True
    def __bool__(self):
        # 고속버전 : return (self.x or self.y) # 고속버전 이지만 가독성 떨어짐
        return bool(abs(self))

    # + 연산자에 대한 오버로딩
    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    # * 연산자에 대한 오버로딩
    # 다만 v * 2는 되지만 2 * v는 안된다.
    # 연잔자의 결합 방향 때문인 것으로 보임
    # __rmul__ 특별메서드도 있음
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)
