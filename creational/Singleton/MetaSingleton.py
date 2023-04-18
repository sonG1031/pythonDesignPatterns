# 메클래스는 클래스 생성과 객체 초기화를 더 세부적으로 할 수 있기 때문에,
# 싱글톤 생성에도 사용될 수 있다.

class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
            print(cls._instances)
        return cls._instances[cls]


class Logger(metaclass=MetaSingleton):
    pass


logger1 = Logger()
logger2 = Logger()
print(logger1, logger2)
