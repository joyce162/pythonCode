class Component:
    def __init__(self,name,lifetime):
        self.name = name
        self.life_time = lifetime
        self.free_time = lifetime

    def __str__(self):
        return f'name: {self.name}, usetime: {self.life_time}, freetime: {self.free_time}'

class Computer:
    def __init__(self,cpu,disk,memory,name='Dell'):
        self.cpu = cpu
        self.disk = disk
        self.memory = memory

    def __str__(self):
        return f'cpu: {self.cpu}, disk: {self.disk}, memory: {self.memory}'

    def run(self,time):
        if self.cpu.free_time < time:
            print('cpu 不能使用')
        elif self.disk.free_time < time:
            print('disk 不能使用')
        elif self.memory.free_time < time:
            print('memory 不能使用')
        else:
            self.cpu.free_time -= time
            self.disk.free_time -= time
            self.memory.free_time -= time

