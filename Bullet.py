


class Bullet:
            
        def __init__(self, x, y):    
            self.x = x    
            self.y = y
            self.speed = 8

            self.direction="UP"
    
        
        def move(self):

            if self.direction=="UP":
                self.y -= self.speed
            elif self.direction=="DOWN":
                self.y +=self.speed
            
           