class NutritionInfo:
    def __init__(self, proteins, carbs, fats):
        self.proteins = proteins
        self.carbs = carbs
        self.fats = fats
    def __add__(self, other):
        return NutritionInfo(self.proteins + other.proteins, self.carbs + other.carbs,  self.fats + other.fats)
    def __mul__(self, other):
        return NutritionInfo(self.proteins * other, self.carbs * other, self.fats * other)
    def energy(self):
        return int(self.fats * 9 + (self.carbs + self.proteins) * 4.2)

tvorog_9 = NutritionInfo(18, 3, 9)
apple = NutritionInfo(0, 25, 0)

breakfast = apple * 2 + tvorog_9
print(breakfast.energy())
