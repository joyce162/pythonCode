import os

# x = 'runoob'
# for i in x:
#     print(i)

# list=[i for i in range(10)]
# print(list)
#
# list1=[i for i in range(0,10,2)]
# print(list1)
#
# list2=[i for i in range(10) if i%2==0]
# print(list2)

#现有一个列表，li = [1,2,4,None,5,None] 使用推导式 仅保留数字
# li = [1,2,4,None,5,None]
# new_li = [i for i in li if i is not None]
# print(li)
#
# f = open('test.txt','r')
# # content = f.read()
# content = f.read(5)
# # content = f.readlines()
# f.close()
# print(content)

# os.mkdir('aa')
# os.rmdir('aa')
# print(os.getcwd())

# os.mkdir('aa')
# os.mkdir('bb')

# os.chdir('aa')
# os.mkdir('bb')
# f = open('1.txt','w')
# f.write('hello world')
# f.close()

# f = open('12txt','w')
# f.write('hello world')
# f.close()
# os.rmdir('bb')
# os.chdir('aa')
# print(os.getcwd())
# listDir = os.listdir('aa')
# print(listDir)
# os.chdir('aa')
# print(os.getcwd())
# for i in listDir:
#     print(i)
#     new_name = 'Python_'+i
#     os.rename(i,new_name)


# os.chdir('aa')
# print(os.getcwd())
# # os.rmdir('Python_bb')
# os.chdir('..')
# print(os.getcwd())
# li = os.listdir('aa')
# os.chdir('aa')
# for i in li:
#     os.remove(i)
os.rmdir('aa')

