from turtle import Turtle,Screen
import random

class Food(Turtle):
    def __init__(self,width,height,boundary_offset):
        Turtle.__init__(self)
        self.width = width
        self.height = height
        self.boundary_offset = boundary_offset
        self.shape("circle")
        self.color("red")
        self.penup()
        self.arbitrary = 0
        """This value is changing every repositioning time
         and detecting the food size"""
        self.repositioning()

    def set_size(self):
        self.arbitrary = random.randint(0,5)
        if self.arbitrary == 1:
            self.shapesize(1,1)
        else:
            self.shapesize(.5,.5)

    def get_size(self):
        return self.arbitrary

    def repositioning(self):
        """The food disappears from its place and appears somewhere else"""

        self.set_size()
        width_pos = random.randint(-self.width+self.boundary_offset,
                                   self.width-self.boundary_offset)
        height_pos = random.randint(-self.height+self.boundary_offset+10,
                                    self.height-self.boundary_offset)

        self.goto(width_pos,height_pos)