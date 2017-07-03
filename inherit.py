class Animal(object):
    pass

 # 哺乳类:
class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

#鹦鹉
class Parrot(Bird):
    pass

#功能
class RunnableMixIn(object):
    def run(self):
        print('Running...')

class FlyableMixIn(object):
    def fly(self):
        print('Flying...')

#使用多继承
class Dog(Mammal, RunnableMixIn):
    pass
    
class Parrot(Bird, FlyableMixIn):
    pass
