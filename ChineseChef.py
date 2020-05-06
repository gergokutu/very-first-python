from Chef import Chef

# inherit it
class ChineseChef(Chef):
    # it can do everything that the generic Chef can do
    # instead of copy
    # inherit it
    # def make_chicken(self):
    #     print("The chef makes a chicken")

    # def make_salad(self):
    #     print("The chef makes a salad")
    
    def make_special_dish(self):
        print("The chef makes orange chicken")

    def make_fried_rice(self):
        print("The chef makes fride rice")

chinese1 = ChineseChef()
chinese1.make_special_dish()