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
