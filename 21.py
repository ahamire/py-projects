# 1) 21 Напишіть програму для друку дробових чисел у форматі до 2 десяткових знаків.
print(round(float(input('enter num: ')), 2))
# 2) 46 Напишіть програму, яка зчитує три цілих числа і виводить найбільше значення з них. Не можна користуватися розгалуженнями і циклами.
a=min(12,-2,54)
b=max(12,-2,54)
print(b,a)
# 3) 71 Напишіть програму для обчислення координат середини відрізка.
a=float(input('x1: '))
b=float(input('y1: '))
c=float(input('x2: '))
d=float(input('y2: '))
print("The midpoint's x value is: ",a+c/2)
print("The midpoint's y value is: ",b+d/2)
# 4) 96 З початку доби годинникова стрілка повернулася на кут a градусів. Визначте на який кут повернулась хвилинна стрілка з початку останньої години.
# Вхідні і вихідні дані - дійсні числа. При розв’язуванні цього завдання не можна користуватися умовними конструкціями і циклами.
a = int(input())
print(a*12%360)
