class test():
    def __init__(self,age):
        self.age = age
    def __getattr__(self, item):
        print(type(item))
        return 100
    def __getattribute__(self, item):
        return 1000

test_1  = test(10)

breakpoint = 1