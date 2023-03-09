

# Задание-1:
# Дан список, заполненный произвольными целыми числами.
# Получить новый список, элементы которого будут
# квадратами элементов исходного списка
# [1, 2, 4, 0] --> [1, 4, 16, 0]


bin = [ 3, 2, 64, 5, -22]
bina = [i ** 2 for i in bin]
print(bina)







# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.


frukt_list = ['яблоко',',banan','apelsin','vishn9']
frukt_list2 = ['kivi','mandarinka','grusha']

frukt_list3 = [i for i in frukt_list if i in frukt_list2]
print(frukt_list3)


fruits_list_1 = ['дыня', 'яблоко', 'мандарин', 'манго', 'груша', 'апельсин', 'нектарин']
fruits_list_2 = ['банан', 'киви', 'яблоко', 'лимон', 'груша', 'ананас', 'мандарин', 'дыня']
for i in fruits_list_1:
    if not i in fruits_list_2:
        fruits_list_2.append(i)
fruits_list3 = fruits_list_2
print(fruits_list3)

l = [1, 2, 3, 4, 5, 6, 7, 8, -4, -5, -3, 12, 27]
l2 = [i for i in l if i % 3 == 0 and i > 0 and i % 4 != 0]
print(l2)

