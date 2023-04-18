# https://weeklyit.code.blog/2019/12/24/2019-12%EC%9B%94-3%EC%A3%BC-python%EC%9D%98-__init__%EA%B3%BC-__new__/

# 싱글톤 패턴 (Singleton Pattern)
# 글로벌하게 접근 가능한 하나의 객체를 제공하는 패턴
# 목적 : 단일 객체 생성, 전역 객체 제공, 공유된 리소스에 대한 타동시 접근 제어

class Singleton:
    #  __init__메소드는 클래스 오브젝트에 메모리를 할당하지 않는다.
    #  따라서 __init__은 클래스 인스턴스틀 생성하지 않는다.
    # 즉, 생성자 메서드가 아니라 초기화 시키는 메서드로 생각할 수 있다.

    # 객체에 메모리를 할당하는 것은 바로 __new__ 메서드이다.
    # 파이썬 객체를 생성할때 __init__이 실행되기 전에 항상 __new__가 먼저 실행된다.
    # 이때 객체에 메모리가 할당되는 것이다.

    # __new__ 메서드는 클래스 자기 자신(cls)을 숨겨진 파라미터로 받으며
    # 반드시 object를 반환한다.
    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls) # super(Singleton, cls).__new__(cls)
        return cls.instance

s = Singleton()
print("Object created", s)
s1 = Singleton()
print("Object created", s1)