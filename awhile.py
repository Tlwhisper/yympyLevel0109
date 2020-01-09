# author yym
flag = True
num1 = 0
while (flag):
    num1 += 1
    if (num1 % 3 == 2 and num1 % 5 == 3 and num1 % 7 == 2):
        print(num1, "是一个符合条件的数！！")
        flag = False
    else:
        print(num1, "此时还不满足条件")
