# # author yym
# 集合没有重复元素
# set1 = {"射手座", "天蝎座", "天秤座", "白羊座"}
# print(set1)

# # 2
# python = {"王一伊", "李静", "李明", "李白"}
# c = {"李静", "李明", "d杜甫", "杨过"}
# print("选修Python的同学是：", python)
# print("选秀C语言的同学是： ", c)

# 3
set2 = set()  # 定义空集合
print(type(set2))

# 4把列表装换成集合
name = ["李静", "李明", "d杜甫", "杨过", "李静", "李静"]
print("列表是：", name)
set3 = set(name)
print("集合是： ", set3)
