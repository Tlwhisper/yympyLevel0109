# author yym
for i in range(1, 10):
    for j in range(1, i+1):
        print(j, "*", i, "=", i * j, end="  ")
    print("")  # 这样也可以换行
