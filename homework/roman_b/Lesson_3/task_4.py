
# Даны катеты прямоугольного треугольника. Найти его гипотенузу и площадь

import math

triangle_leg_1 = 12

triangle_leg_2 = 17

triangle_hypotenuse = math.sqrt(
    triangle_leg_1 ** 2
    + triangle_leg_2 ** 2
)

triangle_area = triangle_leg_1 * triangle_leg_2 / 2

print(f"Your triangle's hypotenuse is: {triangle_hypotenuse}")
print(f"Your triangle's area is: {triangle_area}")
