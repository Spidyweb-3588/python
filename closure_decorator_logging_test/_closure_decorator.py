def logged(func):
    def wrapper(*args, **kwargs):
        print('Calling', func.__name__)
        return func(*args, **kwargs)
    return wrapper

@logged
def add(x,y):
    return x + y

print(add(1,3))
########################################
class Car:
    def __init__(self, model):
        self.model = model

    @property
    def get_model(self):
        return self.model


c = Car("GV80")
print(c.get_model)          # c.get_model()이 아님
