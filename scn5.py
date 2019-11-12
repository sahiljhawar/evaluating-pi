from numpy import *
from manimlib.imports import *
from math import *
import numpy as np

class Polygon1(Scene):

    def construct(self):

        newcircle=SmallDot(color=BLACK)
        text1=TextMobject("\\text{The value of}", r"$\pi$", "\\text{is approximated using the limit}")
        text1.set_color_by_tex("$\pi$", BLUE)
        text2=TextMobject(r"${\lim_{n\to \infty } \mathrm{n}\ \mathrm{tan}\mathrm{(\frac{180}{n}})\ }$}")
        text2.set_color_by_tex(r"${\lim_{n\to \infty } \mathrm{n}\ \mathrm{tan}\mathrm{(\frac{180}{n}})\ }$}",YELLOW_E)
        text3=TextMobject("\\text{where}","\\text{n}", "\\text{is the number of sides in a polygon.}")
        text3.set_color_by_tex("\\text{n}", RED)
        text2.shift(.6*DOWN)
        text3.shift(1.2*DOWN)
        
        
        group=VGroup(text1,text2,text3)
        self.play(ReplacementTransform(newcircle,group),run_time=1.7)
        self.wait(3)
        new2=SmallDot(color=BLACK)
        self.play(ReplacementTransform(group,new2),run_time=1.5)
        self.wait(1)
