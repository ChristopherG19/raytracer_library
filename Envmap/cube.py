# Universidad del Valle de Guatemala
# Christopher García 20541 
# Gráficas por computadora (10)
# #Raytracing environment

from Lib import *

class Cube(object):
    def __init__(self, vmin, vmax):
        self.min = vmin
        self.max = vmax   
             
    def ray_intersect(self, origin, direction):
        
        invdir = 1 / direction
        
        txmin = (self.min.x - origin.x) / direction.x 
        txmax = (self.max.x - origin.x) / direction.x 
        
        if txmin > txmax:
            txmin, txmax = txmax, txmin
        
        tymin = (self.min.y - origin.y) / direction.y 
        tymax = (self.max.y - origin.y) / direction.y 
        
        if tymin > tymax:
            tymin, tymax = tymax, tymin

        if (txmin > tymax | tymin > txmax):
            return None
        
        if (tymin > txmin): txmin = tymin
        if (tymax < txmax): txmax = tymax
        
        tzmin = (self.min.x - origin.z) / direction.z 
        tzmax = (self.max.y - origin.z) / direction.z 
    
        if tzmin > tzmax:
            tzmin, tzmax = tzmax, tzmin
        
        if (txmin > tzmax | tzmin > txmax):
            return None
        
        if (tzmin > txmin): txmin = tzmin
        if (tzmax < txmax): txmax = tzmax
        
        
        
        
        



    
        
        
        