class Funiture:
    def __init__(self,name,area):
        self.name = name
        self.area = area

class Home:
    def __init__(self,address,area):
        self.address = address
        self.area = area
        self.free_area = area
        self.furniture_list = []

    def add_furniture(self,item):
        if self.free_area >= item.area:
            self.furniture_list.append(item.name)
            self.free_area -= item.area
        else:
            print('家具太大，剩余面积不够')

    def __str__(self):
        return f'房屋地址是：{self.address}，面积：{self.area}，剩余面积：{self.free_area}，家具：{self.furniture_list}'

funiture1 = Funiture('bed',6)
funiture2 = Funiture('sofa',4)
home1 = Home('beijing',100)
home1.add_furniture(funiture1)
home1.add_furniture(funiture2)
print(home1)

funiture3 = Funiture('lanqiuchang',99)
home1.add_furniture(funiture3)
print(home1)