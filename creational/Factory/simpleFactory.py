from abc import ABCMeta, abstractmethod

class Animal(metaclass=ABCMeta): # 추상 클래스, 인터페이스
    @abstractmethod
    def do_say(self):
        pass


class Dog(Animal):
    def do_say(self):
        print("멍! 멍!")


class Cat(Animal):
    def do_say(self):
        print("냐옹 냐옹!!")


## forest factory 정의
class ForestFactory:
    def make_sound(self, object_type):
        return eval(object_type)().do_say()


## client 코드
if __name__ == '__main__':
    ff = ForestFactory()
    animal = input("Dog or Cat? ")
    ff.make_sound(animal)