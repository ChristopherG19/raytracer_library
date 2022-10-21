# Universidad del Valle de Guatemala
# Christopher García 20541 
# Gráficas por computadora (10)
# #Raytracing environment
from intersect import *
from Lib import *

class Plane(object):
    def __init__(self, center, w, l, material):
        self.center = center
        self.w = w
        self.l = l
        self.material = material
        
    def ray_intersect(self, origin, direction):
        d = (origin.y + self.center.y) / direction.y
        impact = origin + (direction * d)
        normal = V3(0, 1, 0)
        
        if (d <= 0) or \
            impact.x > (self.center.x + self.w/2) or impact.x < (self.center.x - self.w/2) or \
            impact.z > (self.center.z + self.l/2) or impact.z < (self.center.z - self.l/2): 
            return None
        
        return Intersect(
            distance=d,
            point=impact,
            normal=normal
        )
    
