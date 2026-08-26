print("执行的是我")

# 显示主界面
def homePage():
    print("请输入功能序号：----------------")
    print(" 1:添加学生")
    print(" 2:删除学生")
    print(" 3:修改学生")
    print(" 4:查询学生")
    print(" 5:显示所有学生")
    print(" 6:退出系统")
    print("---------------------------")

student_info = []
def add_student():
    stu_id = input("请输入学生id")
    stu_name = input("请输入学生姓名")
    stu_tel = input("请输入学生手机号")

    global student_info
    for i in student_info:
        if i['name'] == stu_name:
            print(stu_name + " 该生已存在")
            return

    stu_dic = {}
    stu_dic['id'] = stu_id
    stu_dic['name'] = stu_name
    stu_dic['tel'] = stu_tel
    student_info.append(stu_dic)
    show_all_student()
def del_student():
    stu_name = input("请输入学生姓名")
    global student_info
    for i in range(len(student_info)):
        if student_info[i]['name'] == stu_name:
            del student_info[i]
            break
    else:
        print("该生不存在")
    show_all_student()
def update_student():
    stu_name = input("请输入要修改的学生姓名")
    stu_tel = input("请输入学生新的手机号")

    global student_info
    for i in student_info:
        if i['name'] == stu_name:
            stu_dict = {}
            stu_dict['id'] = i['id']
            stu_dict['name'] = i['name']
            stu_dict['tel'] = stu_tel

            student_info.remove(i)
            student_info.append(stu_dict)
            break
    else:
        print("该生不存在")

def find_student():
    stu_name = input("请输入要查询的学生姓名")
    for i in student_info:
        if i['name'] == stu_name:
            print(i['id']+" -- "+i['name']+' -- '+i['tel'])
            break
    else:
        print("该生不存在")
def show_all_student():
    for i in student_info:
        id = i['id']
        name = i['name']
        tel = i['tel']
        print(f'学生学号{id}，姓名{name}，手机号{tel}')

while True:
    homePage()
    input_num = int(input("请输入功能序号："))
    if input_num == 1:
        add_student()
    elif input_num == 2:
        del_student()
    elif input_num == 3:
        update_student()
    elif input_num == 4:
        find_student()
    elif input_num == 5:
        show_all_student()
    elif input_num == 6:
        print("退出系统")
        break
    else:
        print("输入有误")
        break

