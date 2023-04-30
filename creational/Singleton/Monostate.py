# 모노스테이트 싱글톤 패턴 (The Monostate Singleton Pattern)
# 상태를 공유하여 싱글톤 패턴의 목적을 만족시킨다.
# 객체 생성 여부보다는 객체의 상태, 행위가 더 중요하다는 의견이다.

class Borg:
    __shared_state = {"1":"2"} # private static 느낌임
    def __init__(self):
        self.x = 1
        # 파이썬은 __dict__ 속성에 클래스 내 모든 객체의 상태를 저장한다.
        self.__dict__ = self.__shared_state


class BorgNew: # __new__ 메서드를 사용해 구현하는 법
    _shared_state = {}
    def __new__(cls, *args, **kwargs):
        obj = super(BorgNew, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls._shared_state
        return obj


b = Borg()
b1 = Borg()
b.x = 4

print("Borg Object 'b':", b) # b와 b1은 다른 객체임(상태는 같음).
print("Borg object 'b1':", b1)

print("Object State 'b':", b.__dict__)
print("Object State 'b1':", b1.__dict__)

print(dir(Borg))
print("Borg :", id(Borg._Borg__shared_state))
print("Object State 'b':", id(b.__dict__))
print("Object State 'b1':", id(b1.__dict__))