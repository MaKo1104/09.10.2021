class TriangleChecker:

    def __init__(self, sides):
        self.sides = sides
        

    def is_triangle(self):
        if all(isinstance(side, (int, float)) for side in self.sides):
            if all(side > 0 for side in self.sides):
                sorted_sides = sorted(self.sides)
                if sorted.sides[0] + sorted_sides[1] > sorted_sides[2]:
                    return 'Ураа, треугольник может быть построен!'
                return 'К сожелению, соотношение сторон не верное'
            return 'Используя отрицательные числа треугольник не построишь!'
        return 'Ты что, эксперементатор? используй только числа!'            