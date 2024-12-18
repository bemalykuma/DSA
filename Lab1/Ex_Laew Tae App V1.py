class LaewTaeApp():
    def __init__(self, menu):
        self.menu = menu
        self.count = 0

    def random_foods(self):
        self.count += 1
    
    def list_foods(self):
        print(self.menu)

use_app = LaewTaeApp(sorted(["Pizza", "Fried Chicken", "Hamburger", "Steak"]))
use_app.list_foods()
