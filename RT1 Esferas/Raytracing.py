# Universidad del Valle de Guatemala
# Christopher García 20541 
# Gráficas por computadora (10)
# #Raytracing environment

from math import pi, tan
from Lib import *
import math
from sphere import *

class RayTracer(object):
    def __init__(self, width, height):
        self.width = width 
        self.height = height
        self.background_color = color(0, 0, 0)
        self.current_color = color(255, 255, 255)
        self.ray_prob = 1
        self.scene = []
        self.clear()

    def clear(self):
        self.framebuffer = [
            [self.background_color for x in range(self.width)]
            for y in range(self.height)
        ]
        
    def point(self, x, y, color=None):
        if y >= 0 and y <= self.height and x >= 0 and x <= self.width:
            self.framebuffer[y][x] = color or self.current_color
        
    def write(self, filename):
        writebmp(filename, self.width, self.height, self.framebuffer)
        
    def change_rayProb(self, newRayProb):
        self.ray_prob = newRayProb
        
    def render(self):
        fov = int(pi/2)
        ar = self.width/self.height
        tana = tan(fov/2)
        
        for y in range (self.height):
            for x in range (self.width):
                i = ((2 * (x + 0.5) / self.width) - 1) * (ar * tana)
                j = (1 - (2 * (y + 0.5) / self.height)) * tana
                
                direction = V3(i, j, -1).norm()
                origin = V3(0, 0, 0)
                c = self.cast_ray(origin, direction)
                self.point(x, y, c)
                
    def cast_ray(self, origin, direction):
        for s,c in self.scene:
            if s.ray_intersect(origin, direction):
                return c
        return self.background_color
            
WHITE = color(255,255,255)
BLACK = color(0,0,0)
ORANGE = color(255,140,0)

r = RayTracer(600, 600)
r.scene = [
    (Sphere(V3(2.9, 0, -16), 0.25), ORANGE),
    (Sphere(V3(3.5, 0.6, -16), 0.285), BLACK),
    (Sphere(V3(3.5, -0.6, -16), 0.285), BLACK),
    (Sphere(V3(2.6, 0.85, -16), 0.2), BLACK),
    (Sphere(V3(2.6, -0.85, -16), 0.195), BLACK),
    (Sphere(V3(2.35, 0.5, -16), 0.195), BLACK),
    (Sphere(V3(2.35, -0.5, -16), 0.195), BLACK),
    (Sphere(V3(2.15, 0, -16), 0.195), BLACK),
    (Sphere(V3(-0.8, 0, -16), 0.27), BLACK),
    (Sphere(V3(0.1, 0, -16), 0.27), BLACK),
    (Sphere(V3(1, 0, -16), 0.27), BLACK),
    (Sphere(V3(-3.5, 0, -16), 2.8), WHITE),
    (Sphere(V3(0, 0, -16), 2.1), WHITE),
    (Sphere(V3(2.8, 0, -16), 1.47), WHITE),
]
r.render()
r.write('snowman.bmp')
