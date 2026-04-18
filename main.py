class CustomException(Exception):
    pass

class ValueErrorException(CustomException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

class TypeErrorException(CustomException):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

def divide(a, b):
    try:
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeErrorException("Sonlar tipi xato")
        if b == 0:
            raise ValueErrorException("Nolga bo'lib bo'lmaydi")
        return a / b
    except ValueErrorException as e:
        print(f"ValueError: {e}")
    except TypeErrorException as e:
        print(f"TypeError: {e}")

print(divide(10, 2))
print(divide(10, 0))
print(divide("10", 2))
print(divide(10, "2"))