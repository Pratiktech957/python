#  Encapsulation (Data Hiding + Bundling Data & Methods)
# Bundling data (self.brand) and methods (start()) inside a class.

# Keeps data safe from outside interference.

class car:
    def __init__(self):
        self._brand = brand
        
    def start(self):
        print(f"{self._brand} car is starting") 
        
    def stop(self):
        print(f"{self._brand} car is stopping")
car1 = car("Toyota")
car1.start()       



# __brand is a private variable (name mangled). It cannot be accessed directly from outside.