from numpy import *
from manimlib.imports import *
from math import *
import numpy as np

class ColoringEquations(Scene):

    def construct(self):
        text1=TextMobject("\\text{The value of}", r"$\pi$", "\\text{is calculated using the limit}")
        text1.set_color_by_tex("$\pi$", BLUE)
        text2=TextMobject(r"${\lim_{n\to \infty } \mathrm{n}\ \mathrm{tan}\mathrm{(\frac{360}{2n}})\ }$}")
        text2.set_color_by_tex(r"${\lim_{n\to \infty } \mathrm{n}\ \mathrm{tan}\mathrm{(\frac{360}{2n}})\ }$}",YELLOW_E)
        text3=TextMobject("\\text{where}","\\text{n}", "\\text{is the number of sides in a polygon.}")
        text3.set_color_by_tex("\\text{n}", RED)
        text2.shift(.6*DOWN)
        text3.shift(1.2*DOWN)
        
        text4=TextMobject("\\text{Thank You!!!}")
        group=VGroup(text1,text2,text3)
        text4.scale(3)
        self.play(ShowCreation(text1),ShowCreation(text2),ShowCreation(text3))
        self.wait(2)
        self.play(ReplacementTransform(group,text4))
        self.wait(1)
