class Student2:
    def __init__(self, name, major, points):
        self.name = name
        self.major = major
        self.points = points
    
    # provides a service to the owner class
    # class function >>  method
    # putting functions inside of classes are youseful
    # check object_functions.py 
    def on_honor_roll(self):
        if self.points >= 3.5:
            return True
        else:
            return False
