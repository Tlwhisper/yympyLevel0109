# author yym
# zip  dict

# word = {'che': '车', 'chen': '沉', 'cheng': '城', 'chi': '吃'}
# print(word)

# 2 用zip和dict把列表转成字典
# key = ['che', 'cheng', 'chi', 'chen']
# value = ['车', '城', '吃', '陈']
# zip1 = zip(key, value)  # 返回一个zip的一个对象
# print(zip1)
# word = dict(zip1)  # 转换成字典对象
# print(word)

# 3 元组可以作为字典的键
# key = ('che', 'cheng', 'chi', 'chen')
# value = ['车', '城', '吃', '陈']
# word1 = {key: value}
# print(word1)
#
# # 4 空
# word2 = {}
# print(word2)
#
# word3 = dict()
# print(word3)

# 5 dict函数
dictory = dict(绮梦='水瓶座', 冷毅毅='射手座', 香凝='双鱼座', 黛蓝='双子座')
print(dictory)

# 6 fromkeys只有键没有值
name = ['绮梦', '冷毅毅', '香凝', '黛蓝']
dictory2 = dict.fromkeys(name)
print(dictory2)

# 删除
# del dictory2

# 只清除字典中的值
dictory2.clear()
print(dictory2)
