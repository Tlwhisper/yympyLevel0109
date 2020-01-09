# author yym
# 字典推导式

# #1
# import random
# randomdict = {i: random.randint(10, 100) for i in range(1, 5)}
# print(randomdict)

# #2推荐使用字典推导式构造字典
name = ['王明', '小玲', '谢翱龙', '天使']
xingzuo = ['魔羯座', '双鱼座', '射手座', '天秤座']
dict1 = {i: j for i, j in zip(name, xingzuo)}
print(dict1)


