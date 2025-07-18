num = [3, 5, 4, 6, 2]
l = len(num)
for i in range(0,l):
    for j in range(i+1,l):
        if num[i] > num[j]:
            temp = num[i]
            num[i] = num[j]
            num[j] = temp
print(num)





# a = [1, 4, 3, 6, 2]
# my_sort = sorted(a)
# print(my_sort)



