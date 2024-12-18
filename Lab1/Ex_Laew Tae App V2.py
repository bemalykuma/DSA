class LaewTaeApp():
    def __init__(self, menu):
        self.menu = menu
        self.count = 0

    def random_foods(self):
        self.count += 1
    
    def list_foods(self):
        print(sorted(self.menu))

    def add_food_item(self, name):
        self.menu.append(name)
use_app = LaewTaeApp(["Pizza", "Fried Chicken", "Hamburger", "Steak"])
for i in range(int(input())):
    use_app.add_food_item(input())
use_app.list_foods()
