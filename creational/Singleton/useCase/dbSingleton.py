# 상황 : 클라우드 서비스에서 여러 모듈이 한개의 DB를 공유하는 구조
# 안정된 클라우드 서비스를 설계하려면
# 1. 데이터베이스 작업 간에 일관성 유지, 즉 작업 간의 충돌이 발생하면 안됨
# 2. 다수의 DB 연산을 처리하려면 메모리와 CPU를 효율적으로 사용해야함

import sqlite3
class MetaSingleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class Database(metaclass=MetaSingleton):
    connection = None
    @classmethod
    def connect(cls):
        if cls.connection is None:
            cls.connection = sqlite3.connect("db.sqlite3")
            cls.cursorobj = cls.connection.cursor()
        return cls.cursorobj

db1 = Database.connect()
db2 = Database.connect()

print("Database Objects DB1", db1)
print("Database Objects DB2", db2)