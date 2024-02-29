import math
def calculate_distance(x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
def calculate_triangle_area(x1, y1, x2, y2, x3, y3):
    side1 = calculate_distance(x1, y1, x2, y2)
    side2 = calculate_distance(x2, y2, x3, y3)
    side3 = calculate_distance(x3, y3, x1, y1)
    s = (side1 + side2 + side3) / 2
    area = math.sqrt(s * (s - side1) * (s - side2) * (s - side3))
    if area <= 0:
        print("Трикутник не існує, оскільки площа менше або дорівнює нулю.")
        return 0
    return area
x1 = float(input("Введіть x-координату першої вершини: "))
y1 = float(input("Введіть y-координату першої вершини: "))
x2 = float(input("Введіть x-координату другої вершини: "))
y2 = float(input("Введіть y-координату другої вершини: "))
x3 = float(input("Введіть x-координату третьої вершини: "))
y3 = float(input("Введіть y-координату третьої вершини: "))
triangle_area = calculate_triangle_area(x1, y1, x2, y2, x3, y3)
if triangle_area > 0:
    print("Площа трикутника з заданими координатами вершин: ", triangle_area)

