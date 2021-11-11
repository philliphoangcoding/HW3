class FoodItem:
    def __init__(self, name="None", fat=0.0, carbs=0.0, protein=0.0):
        self.name = name
        self.fat = fat
        self.carbs = carbs
        self.protein = protein
    def get_calories(self, servings):
        calories = ((self.fat * 9) + (self.carbs * 4) + (self.protein * 4)) * servings;
        return calories
    def print_info(self):
        print('Nutritional information per serving of {}:'.format(self.name))
        print('   Fat: {:.2f} g'.format(self.fat))
        print('   Carbohydrates: {:.2f} g'.format(self.carbs))
        print('   Protein: {:.2f} g'.format(self.protein))
if __name__ == "__main__":
    food_item1 = FoodItem()
    name = input()
    fat = float(input())
    carbs = float(input())
    protein = float(input())
    food_item2 = FoodItem(name, fat, carbs, protein)
    servings = float(input())
    food_item1.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings,food_item1.get_calories(servings)))
    print()
    food_item2.print_info()
    print('Number of calories for {:.2f} serving(s): {:.2f}'.format(servings,food_item2.get_calories(servings)))