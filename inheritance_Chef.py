# inherit another class attributes, methods
from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_chicken()
myChef.make_special_dish()

myCineseChef = ChineseChef()
myCineseChef.make_chicken()
myCineseChef.make_special_dish()