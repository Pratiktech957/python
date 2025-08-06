class car:
    def __init__(self,brand):
        self.brand =brand
        
        
    def start(self):
        print(f"{self.brand} car is starting")
        
    def stop(self):
        print(f"{self.brand} car is stopping")
        
car1 = car("Toyota")
car1.start()    
car1.stop()