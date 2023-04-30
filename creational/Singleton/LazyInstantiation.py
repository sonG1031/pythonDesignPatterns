# 게으른 초기화 (Lazy instantiation)
# 싱글톤 패턴을 기반으로 하는 초기화 방식
# 목적 : 인스턴스가 꼭 필요할 때 생성

class Singleton:
    __instance = None # 은닉 (외부 접근 거부), 클래스 변수 (self.~ 이 아니므로 독립적인 변수가 아님)
    def __init__(self):
        if not Singleton.__instance: # 인스턴스가 필요없는 경우라서 만들지 않음
            print("__init__ method called..")
        else:
            print("Instance already created:", self.getInstance())

    @classmethod
    def getInstance(cls): # 인스턴스가 꼭 필요할 때 호출함
        if not cls.__instance: # __instance가 없으면
            cls.__instance = Singleton() # 인스턴스를 만들어 할당
        return cls.__instance


s = Singleton() # 클래스를 초기화했지만 객체는 생성하지 않음
print("Object created", Singleton.getInstance()) # 객체 생성
s1 = Singleton() # 이미 객체가 생성됨
# print(s1.getInstance())