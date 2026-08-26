class Student(object):
    def __init__(self,name,gender,tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'姓名：{self.name}，性别： {self.gender}，电话：{self.tel}'