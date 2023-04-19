# https://dojang.io/mod/page/view.php?id=2468

# 메타클래스는 클래스의 클래스이다.
# 즉 클래스는 자신의 메타클래스의 인스턴스다.

# 클래스는 메타클래스가 정의한다.
# 예를 들어 클래스 A의 객체를 초기화하면 파이썬은 내부적으로
# A = type(name:클래스명, bases:기본클래스, dict:클래스속성)을 수행한다.

class MyInt(type):
    def __call__(cls, *args, **kwds): # 클래스로 인스턴스를 만들 때 호출되는 메서드
        print("Here's My int", args, kwds)
        return type.__call__(cls, *args, **kwds)


class int(metaclass=MyInt):
    def __init__(self, x, y):
        self.x = x
        self.y = y


i = int(4,5)
# 위처럼 int(4,5)로 int 클래스를 생성하면 MyInt 메타클래스의 __call__ 메소드가 호출된다.
# 객체 생성을 메타클래스가 제어한다는 의미이다.
print(i.x, i.y)