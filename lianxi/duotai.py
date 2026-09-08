class Dog(object):
    __tooth = 100
    def work(self):
        print("追击")

    @classmethod
    def get_tooth(cls):
        return cls.__tooth

class ArmDog(Dog):
    def work(self):
        print('追击敌人')

class DrugDog(Dog):
    def work(self):
        print('追击毒品')

class Person(object):
    def work_with_dog(self,dog):
        dog.work()


ad = ArmDog()
dd = DrugDog()

pp = Person()
pp.work_with_dog(ad)
pp.work_with_dog(dd)

print(ad.get_tooth())


try:
    print(1/0)
except Exception as result:
    print(result)

try:
    print(1/1)
except Exception as result:
    print(result)
else:
    print("未报错，打印")