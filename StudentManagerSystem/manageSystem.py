from StudentManagerSystem.student import Student
import os


class StudentSystem(object):

    def __init__(self):
        self.student_lists = []

    def run(self):
        while True:
            print('-'*20)
            self.load_student()
            self.show_menu()
            menu_num = int(input('请输入功能序号：'))
            if menu_num == 1:
                self.add_student()
            elif menu_num == 2:
                self.del_student()
            elif menu_num == 3:
                self.modify_student()
            elif menu_num == 4:
                self.search_student()
            elif menu_num == 5:
                self.show_all_student()
            elif menu_num == 6:
                self.save_student()
            elif menu_num == 7:
                break
    @staticmethod
    def show_menu():
        print('请选择如下功能')
        print('1.添加学员')
        print('2.删除学员')
        print('3.修改学员信息')
        print('4.查询学员信息')
        print('5.显示所有学员')
        print('6.保存学员信息')
        print('7.退出系统')

    def add_student(self):
        print('添加学员')
        name = input('请输入学员姓名：')
        gender = input('请输入学员性别：')
        tel = input('请输入学员手机号：')
        stu = Student(name,gender,tel)

        for i in self.student_lists:
            if i.name == name:
                return '学员已存在，请勿重复添加'
        self.student_lists.append(stu)
        print(self.student_lists)

    def del_student(self):
        print('删除学员')
        name = input('请输入学员姓名：')

        for i in self.student_lists:
            if i.name == name:
                self.student_lists.remove(i)
                break
        else:
            print('查无此人')

    def modify_student(self):
        print('修改学员')
        modify_name = input('请输入要修改的学员姓名：')

        for i in self.student_lists:
            if i.name == modify_name:
                i.name = input('请输入学员姓名：')
                i.gender = input('请输入学员性别：')
                i.tel = input('请输入学员手机号：')
                break
        else:
            print('查无此人')
        print(self.student_lists)

    def search_student(self):
        print('查询学员')
        search_name = input('请输入要查询的学员姓名：')

        for i in self.student_lists:
            if i.name == search_name:
                print(f'学员姓名：{i.name}，学员性别：{i.gender}，学员手机号：{i.tel}')
                break
        else:
            print('查无此人')

    def show_all_student(self):
        for i in self.student_lists:
            print(f'学员姓名：{i.name}，学员性别：{i.gender}，学员手机号：{i.tel}')

    def save_student(self):
        f = open('student.txt','w')
        new_lists = [i.__dict__ for i in self.student_lists]
        f.write(str(new_lists))
        f.close()

    def load_student(self):
        try:
            f = open('student.txt','r')
        except:
            f = open('student.txt','w')
        else:
            content = f.read()
            new_list = eval(content)
            self.student_lists = [Student(i['name'],i['gender'],i['tel']) for i in new_list]
        finally:
            f.close()