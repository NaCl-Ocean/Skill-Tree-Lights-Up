

#name  = ['mike','tom']

# def test(name):
#     name.append('tom')
#     print('函数内部：',name)
# name = ['mike']
# test(name)
# print('函数外部:',name

# def new_feature(func):
#     def inner(*args,**kwargs):
#         print('new_feature')
#         func()
#     return inner
#
# @new_feature
# def old_feature(name='mike'):
#     print('old_feature1')
#     print(name)
#
# @new_feature
# def old_feature2():
#     print('old_feature2')
# old_feature()
# old_feature2()
# def test1():
#     print('nihao')
#
# def test2():
#     print('i am not fine')
#     test1()
#
# test2()


class Relation:
    def __init__(self):
        self.couple = list()

    def make_relation(self,obj1,obj2):
        self.couple.extend([obj1,obj2])
        print('{} and {} make relation'.format(self.couple[0].name,self.couple[1].name))

    def get_coule(self,obj_target):
        for obj in self.couple:
            if obj == obj_target:
                pass
            else:
                return obj.name

class Dog:
    def __init__(self,name,age,d_type,master):
        self.name = name
        self.age = age
        self.d_type = d_type
        self.master = master
        self.bite()
    def bite(self):
        print('{} bites its master {}'.format(self.name,self.master.name))

class Brain:
    def __init__(self,IQ):
        self.IQ = IQ
class Person:
    def __init__(self,name,age,sex,IQ):
        self.name = name
        self.age = age
        self.sex = sex
        self.Brain = Brain(IQ)

class Chinese(Person):
    def __init__(self,name,age,sex,IQ,province):
        super().__init__(name,age,sex,IQ)
        super(Chinese,self).__init__(name,age,sex,IQ)
        Person.__init__(self,name,age,sex,IQ)
        self.province = province

# mike = mike = Person('mike',20,'m',120)
# print(mike.Brain.IQ)
# relation = Relation()
# mike = Person('mike',20,'m',relation)
# jissca = Person('jissca',21,'f',relation)
# relation.make_relation(mike,jissca)
# print("mike's couple:{}".format(mike.relation.get_coule(mike)))

# class Brand:
#     def __init__(self,name):
#         self.name=name
#     def __getitem__(self, item):
#         print("获取KEY",item)
#         return self.__dict__[item]
#     def __setitem__(self, key, value):
#         print("设置一个key...",key)
#
#
#
#     def __delitem__(self, key):
#         print('del obj[key]时,我执行')
#         self.__dict__.pop(key)
#     def __delattr__(self, item):
#         print('del obj.key时,我执行')
#         self.__dict__.pop(item)
#
#     def __del__(self):
#         print('del')

class Printer(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance == None:
            obj = object.__new__(cls)
            cls.__instance = obj
        return cls.__instance

    def __init__(self,name):
        self.name = name
        print('create:{}'.format(self.name))


# word = Printer('word')
# excel = Printer('excel')
# print('word:',word.name,'excel:',excel.name)
# print(id(word),id(excel))

def __init__(self,name,age):
    self.name = name
    self.age = age
    print('create test obj')

test_cls = type('test',(object,),{'d_type':'test','__init__':__init__})
test_obj = test_cls('test_obj',1)


print(type(('ste')))