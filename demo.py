import functools


def print_line():
    print("-"*20)

# print_line()

def print_line2(num):
    for i in range(num):
        print_line()

# print_line2(3)

def sum(a,b,c):
    return a+b+c

print(sum(1,2,3))

def average(a,b,c):
    res = sum(a,b,c)
    return res/3

print(average(1,2,3))


def test01(a,b,c):
    if len(a)>6 or len(b)>6 or len(c)>6:
        return "参数不能超6位"
    else:
        return a+b+c

print(test01('sgh','123','hjhwwwwwwww'))


def sum_test(n):
    i = 1
    sum = 0
    for i in range(n):
        sum += i
    return sum

print(sum_test(10))


li = 'helloworldhellopythonhelloc++hellojava'
def find_all(li):
    ret_li = []
    start_index = 0

    while True:
        ret = li.find("hello",start_index)
        if ret != -1:
            ret_li.append(ret)
            start_index = ret + 5
        else:
            break
    return ret_li
print(find_all(li))

def min_max(*args):
    return max(args),min(args)
print(min_max(1,2,3,4,5))

def sum_nums(num):
    if num==1:
        return 1
    return num+sum_nums(num-1)

print(sum_nums(5))

fn = lambda a,b:a+b
print(fn(1,2))

fn2 = lambda :100
print(fn2())

fn3 = lambda a,b:a if a>b else b
print(fn3(1,2))

def sum_num(a,b,f):
    return f(a)+f(b)
print(sum_num(-1,-4,abs))


list1=[1,2,3,4,5,6,7,8,9]
def func(x):
    return x%2==0
result = filter(func,list1)
print(list(result))

li1 = [1,2,3,4,5,6]
def func4(x):
    return x%2 != 0
li4 = list(filter(func4,li1))
def func1(a,b):
    return a+b
result1 = functools.reduce(func1, li4)
print(result1)

li2 = [1,2,None,3,None,5]
def func2(x):
    return x != None
result2 = filter(func2,li2)
print(list(result2))

li3 = [1,2,3,4,5,6]
def func3(x):
    if x % 2 == 0:
        return x*2
    else:
        return x
result3 = map(func3,li3)
print(list(result3))


