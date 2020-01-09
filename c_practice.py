# author yym
print("玩游戏，从1数到99，末尾是7或者被7整除或者数字中出现了7的数跳一下，统计一共跳了几下：")
count = 0
for i in range(1, 100):
    if i % 10 == 7 or i % 7 == 0 or i // 10 == 7:  # //表示整除
        print("此处跳一下")
        count += 1
        continue
    print(i)
print("一共跳了" + str(count) + "下")
