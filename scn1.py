from numpy import *
from manimlib.imports import *
from math import *

class Polygon1(Scene):
    def construct(self):
        text = TextMobject("\\text{Approximation of}",r"$\pi$")
        
        text2 = TextMobject("\\text{This simple yet beautiful animation shows}")
        text3 = TextMobject("\\text{that how an n-gon shape is transformed}")
        text4 = TextMobject("\\text{into a cirlce and the value of}",r"$\pi$","\\text{is approximated.}")
        text.set_color_by_tex("$\pi$", BLUE)
        text4.set_color_by_tex("$\pi$", BLUE)
        text2.set_color_by_tex("\\text{This simple yet beautiful animation shows}",YELLOW)
        text3.set_color_by_tex("\\text{that how an n-gon shape is transformed}",YELLOW)
        text4.set_color_by_tex("\\text{into a cirlce and the value of}",YELLOW)
        text.set_color_by_tex("\\text{Approximation of}",YELLOW)
        text4.set_color_by_tex("\\text{is approximated.}",YELLOW)
        text6 = TextMobject("\\text{Consider two lines of unit length originating from the centre of}")
        text7 = TextMobject("\\text{each polygon and joining the two collinear vertices.}")
        text8 = TextMobject("\\text{As the centre of the polygons is same, therefore, the distance  }")
        text9 = TextMobject("\\text{between the center and the vertices will be constant.}")
        sent=VGroup(text2,text3,text4)
        lines=VGroup(text6,text7)
        same=VGroup(text8,text9)
        text7.shift(0.6*DOWN)
        text9.shift(0.6*DOWN)
        text3.shift(0.5*DOWN)
        text4.shift(1.0*DOWN)
        sent.shift(0.5*UP)
        self.play(ShowCreation(text))
        self.wait(1.5)
        self.play(ReplacementTransform(text,sent))
        self.wait(3)
        self.play(ReplacementTransform(sent,lines))
        self.wait(3)
        self.play(ReplacementTransform(lines,same))
        self.wait(3)
        new2=SmallDot(color=BLACK)
        self.play(ReplacementTransform(same,new2),run_time=1.5)
        self.wait(1)
 
