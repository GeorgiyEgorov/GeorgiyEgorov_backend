##Задача-2: Напишите программу, которая спрашивает "Четные или нечетные?", в зависимости от ответа,
# используя цикл с предусловием while или for in
# вывести в одну строку через пробел соотвествующие числа от 0 до 20
a = 1
b = 2
print('nechet')
while a <= 20:
     print(a)
     a = a + 2
print("chet")
while b <= 19:
     print(b)
     b = b + 2
# Задача-1: Запросите у пользователя его возраст.
# Если ему есть 18 лет, выведите: "Доступ разрешен",
# иначе "Извините, пользоваться данным ресурсом можно только с 18 лет"
age = int(input('vvedite vozrast'))
if age >= 18:
    print("dostup razreshen")
else: print('dostup zapreshen')

#Дано произвольное целое число, вывести самую большую цифру этого числа.
# Например, дается x = 58375.
# Нужно вывести максимальную цифру в данном числе, т.е. 8.
# Подразумевается, что мы не знаем это число заранее.
# Число приходит в виде целого беззнакового.
# Подсказки:
# * постарайтесь решить задачу с применением арифметики и цикла while;
# * при желании и понимании решите задачу с применением цикла for.

a = int(input('chislo-'))
n = a%10
a = a//10
while a > 0:
    if a%10 > n:
        n =  a%10
    a = a//10
print(n)
