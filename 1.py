import random
def generate_password(len1, element):
    password = ""
    for i in range(len1-len(element)):
        if i == (len1-len(element)) * 0.5:
            password = password + element
        j = random.randint(1, 10)
        password = password + str(j)
    return password
print(generate_password(10, "asdasd"))


def if_in_where(lst1, a):
    a = int(a)
    if a in lst1:
        for i in range(len(lst1)):
            if lst1[i] == a:
                if len(lst1) % 2 == 0:
                    if i+1 <= len(lst1) * 0.5:
                        flag = "left"
                    else:
                        flag = "right"
                else:
                    if i+1 < int(len(lst1) * 0.5 + 1):
                        flag = "left"
                    elif i+1 == int(len(lst1) * 0.5 + 1 ):
                        flag = "center"
                    else:
                        flag = "right"
        if flag == "left":
            print(a, "位于列表的左半边")
        elif flag == "right":
            print(a, "位于列表的右半边")
        elif flag == "center":
            print(a, "位于列表的中间")
    else:
        print(a, "不在列表当中")
if_in_where([1, 2, 3, 4, 5, 6, 7, 8, 9],4)


def function1(a):
    for i in range(2, a):
        if a % i == 0:
            return False
    return True
print(list(filter(function1, range(1,101))))


import Mymodule
print("add:", Mymodule.add(2, 2))
print("sub:", Mymodule.sub(4, 2))
print("mul:", Mymodule.mul(3, 3))
print("div:", Mymodule.div(9, 3))
print()


def function2(lst1):
    return min(lst1)
print("列表中最小的整数是", function2([7,2,3,4,1,5,6]))