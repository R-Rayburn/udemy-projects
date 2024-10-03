import random

class Database:
    _instance = None

    # Can't utilize this, unless you create a guard in here
    def __init__(self):
        # Will get two different ids here
        id = random.randint(1, 101)
        print(f'id={id}')
        print('Loading a database from file.')

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Database, cls)\
            .__new__(cls, *args, **kwargs)
        return cls._instance

if __name__ == '__main__':
    d1 = Database()
    d2 = Database()
    print(d1 == d2)