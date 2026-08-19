class SweetPotato:
    def __init__(self):
        self.cook_time = 0
        self.cook_state = '生的'
        self.condiments=[]

    def cook(self,time,condiments):
        self.cook_time += time
        if 0<= self.cook_time <3:
            self.cook_state = '生的'
            print('熟的才能添加调料')
        elif 3<= self.cook_time <5:
            self.cook_state = '半生不熟'
            print('熟的才能添加调料')
        elif 5<= self.cook_time <8:
            self.cook_state = '熟了'
            self.condiments.append(condiments)
        elif self.cook_time >= 8:
            self.cook_state = '糊了'
            print('熟的才能添加调料')

    def addCondiments(self,condiments):
        self.condiments.append(condiments)

    def __str__(self):
        return f'这个地瓜被烤过的时间是{self.cook_time},状态是{self.cook_state},调料是{self.condiments}'

digua1 = SweetPotato()
print(digua1)
print('-'*20)

digua1.cook(1,'酱油')
print(digua1)
print('-'*20)

digua1.cook(5,'蜂蜜')
print(digua1)
print('-'*20)

digua1.cook(3,'麻油')
print(digua1)