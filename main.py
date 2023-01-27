name = "Georgiy"
age = 27
age = int(age) - 18
print(age)
print('georgiy starshe na', age, 'moloje georgia na ', age)15



d = input('введите GOD')
c = input('введите BOZ')
d, c = c, d
print('d =', d)
print('c = ', c)

print('reshaem uravnenie ax2+bx+c=0')
a = input('znachenie a')
b = input('znachenie b')
c = input('znachenie c')
a = float(a)
b = float(b)
c = float(c)
discriminant = b**2 - 4*a*c
print('discriminant' + str(discriminant))
if discriminant < 0:
    print('kornei net')
elif discriminant == 0:
    x = -b/(2 * a)
    print('x= ' + str(x))
else:
    x1 = (-b + discriminant ** 0.5) / (2 * a)
    x2 = (-b - discriminant ** 0.5) / (2 * a)
    print('x₁ = ' + str(x1))
    print('x₂ = ' + str(x2))






