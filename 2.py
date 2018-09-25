
def prt_usr():
    name = input("请输入你的名字:")
    age = int(input("请输入你的年龄:"))
    print(name, "在", 2018+100-age, "年为100岁")
prt_usr()
print()


def function1():
    element1 = int(input("请输入一个整数:"))
    if element1 %2 == 0:
        print("你输入的是偶数")
    else:
        print("你输入的是基数")
function1()


def function2_1(list):
    if None in list:
        print("list中有空对象")
        return True
    print("list中没有空对象")

def function2_2(list):
    for i in list:
        if i == None:
            print("list中有空对象")
            return True
    print("list中没有空对象")
def function2_3(list):
    if None not in list:
        print("list中没有空对象")
        return True
    print("list中有空对象")
function2_1([1, 2, None])
function2_2([1, 2, None])
function2_3([1, 2, None])



def function3_1(lst1):
    lst1 = list( map(lambda x: x ** 2, lst1))
    print(lst1)
def function3_2(lst1):
    lst1 = [x ** 2 for x in lst1]
    print(lst1)
function3_1([1, 2, 3])
function3_2([1, 2, 3])



from functools import reduce
def function4(lst1):
    print(reduce(lambda x, y: x+y, lst1))
function4([1, 2, 3, 4, 5])


def function5(lst1):
    print(lst1, "开平方后为：", end="")
    lst1 = [int(x ** 0.5) for x in lst1]
    print(lst1)
function5([1, 4, 9])
print()


def function6(lst1, lst2):
    return list(set(lst1) & set(lst2))
print(function6([1,2,3,4],[1,2,3,5,6]))



def function7_1(a, b, c):
    return max(a, b , c)
def function7_2(a, b, c):
    if a>b:
        if a>c:
            return a
        else:
            return b
    else:
        if b>c:
            return b
        else:
            return c
print("最大的数字是：", function7_1(1, 4, 3))
print("最大的数字是：", function7_2(1, 4, 3))