# author yym

# #1
# word = dict(冷毅毅='射手座', 王明='魔羯座', 度哈哈='双鱼座',天使='双子座')
# print(word)
# print(word['王'] if '王' in word else "不在")

# #2
# # get方法不会抛出异常而，【】会抛出异常
# print(word.get('明', "查无此人"))

# # # 3 两次对应get方法,取出一个人对应星座的性格特点
# word = dict(冷毅毅='射手座', 王明='魔羯座', 度哈哈='双鱼座', 天使='双子座')
# sign_all = ['白羊座', '金牛座', '双子座', '巨蟹座', '狮子座', '处女座', '天秤座', '天蝎座', '射手座', '魔羯座', '水瓶座', '双鱼座']
# nature = ['白羊温暖', '金牛保守', '双子新鲜感', '巨阙敏感', '狮子理想', '处女完美', '天秤公平', '天蝎精力旺盛', '射手崇尚自由', '魔羯聪慧', '水平耐心', '双鱼自由舒服']
# character = dict(zip(sign_all, nature))
# print("度哈哈的星座是：" + word.get('度哈哈'))  # 获取王明星座
# print("\n度哈哈的性格特点是：\n\n" + character.get(word.get('度哈哈')))


# # 4 遍历
word = dict(冷毅毅='射手座', 王明='魔羯座', 度哈哈='双鱼座', 天使='双子座')
print(word.items())

for item in word.items():
    print(item)

for key, value in word.items():
    print(key + "的星座是：" + value)
