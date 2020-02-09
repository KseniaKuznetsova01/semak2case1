import turtle
from turtle import *
print('''Select a fractal:
1. The Koch Curve
2. Koch's Snowflake.
3. Ice fractal (example 1)
4. Ice fractal (example 2)
5. Snowflake to an ice fractal (example 1) with the construction of external and internal fractals.
6. A snowflake to an ice fractal (example 2) with the construction of the outer and inner fractals.
7. Minkowski Curve
8. Levi's Curve
9. Building a binary tree.''')

f = int(input())
if f == 1:
    def koch(order, size):
        if order == 0:
            forward(size)
        else:
            koch(order-1, size/3)
            left(60)
            koch(order-1, size/3)
            right(120)
            koch(order-1, size/3)
            left(60)
            koch(order-1, size/3)

    def main():
        up()
        goto(-100,0)
        down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch(n, a)

    main()

elif f == 2:
    def koch(order, size):
        if order == 0:
            forward(size)
        else:
            koch(order - 1, size / 3)
            left(60)
            koch(order - 1, size / 3)
            right(120)
            koch(order - 1, size / 3)
            left(60)
            koch(order - 1, size / 3)

    def main():
        up()
        goto(-100, 0)
        down()

    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    koch(n, a)
    right(120)
    koch(n, a)
    right(120)
    koch(n, a)

    main()
elif f == 7:
    def mink(order, size):
        if order == 1:
            forward(size)

        else:
            mink(order - 1, size / 2)
            right(90)
            mink(order - 1, size / 2)
            left(90)


    # нужно сделать нормальный угол
    order = int(input('Глубина рекурсии:'))
    size = int(input('Глубина рекурсии:'))

    mink(order, size)

elif f == 9:

    def tree(order, size):
        if order >= 1:
            forward(order * 10)
            right(30)
            tree(order * 0.75, size / 4)
            left(60)
            tree(order * 0.75, size / 4)
            right(30)
            bk(order * 10)
        else:
            forward(size)


    def main():
        left(90)
        speed(10)
        up()
        goto(0, -100)
        down()
        tree(order, size)


    order = int(input('Глубина рекурсии:'))
    size = int(input('Глубина рекурсии:'))

    main()