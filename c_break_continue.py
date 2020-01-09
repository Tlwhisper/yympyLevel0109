# author yym
# for i in range(1, 101):
#     print(i)
#     if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
#         print(str(i) + "满足条件")
#         break

# continue
for i in range(1, 31):

    if i % 3 == 2 and i % 5 == 3 and i % 7 == 2:
        continue
    print(i)