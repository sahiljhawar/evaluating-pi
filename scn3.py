from numpy import *
from manimlib.imports import *
class Polygon1(Scene):
    def construct(self):
        hexa=RegularPolygon(n=6,color=RED)
        tri=RegularPolygon(n=3,color=WHITE)
        tri.scale(3)
        a = hexa.get_vertices()
        cir=SmallDot(color=BLUE)
        lin1=Line(cir, a[5])
        lin2=Line(cir, a[4])
        lin =Line()
        lin.rotate(np.pi/2)
        lin.shift(1.23*DOWN)
        lin.scale(1.35)
        a = TextMobject("\\text{A}")
        b = TextMobject("\\text{B}")
        c = TextMobject("\\text{C}")
        a.next_to(cir,UP)
        b.next_to(hexa,7*DOWN+3*LEFT)
        c.next_to(hexa,7*DOWN+3*RIGHT)
        s=VGroup(hexa,cir,lin1,lin2)
        s.scale(3)
        cir1=SmallDot(color=BLUE)
        cir1.scale(3)
        new=VGroup(a,b,c,s,lin,cir1)
        self.play(ShowCreation(a),ShowCreation(b),ShowCreation(c),ShowCreation(s),ShowCreation(lin),ShowCreation(cir1),run_time=3)
        self.wait(1)
        a1 = TextMobject("\\text{A}")
        b1 = TextMobject("\\text{B}")
        c1 = TextMobject("\\text{C}")
        
        cir2=SmallDot(color=BLUE)
        cir2.scale(2.05)
        cir2.shift(2.51*UP)
        a1.next_to(cir2,UP)
        b1.next_to(tri,DOWN+LEFT)
        c1.next_to(tri,DOWN+RIGHT)
        linnew=Line()
        linnew.rotate(np.pi/2)
        linnew.scale(2.23)
        linnew.shift(0.21*UP)
        ngroup=VGroup(tri,linnew)
        self.play(ShowCreation(ngroup),ReplacementTransform(new,cir2),run_time=1.5)
        arc=Arc(angle=np.pi/5.55)
        arc.rotate(-np.pi/2)
        arc.shift(1.22*UP,0.63*LEFT)
        self.play(ShowCreation(a1),ShowCreation(b1),ShowCreation(c1),ShowCreation(arc),run_time=3)
        text=TextMobject("\\text{a}")
        text.set_color_by_tex("\\text{a}", BLUE)
        text.scale(1.75)
        text.shift(0.4*RIGHT+DOWN)
        text1=TextMobject(r"$\theta$")
        text1.set_color_by_tex(r"$\theta$", BLUE)
        text1.next_to(arc,0.6*DOWN)
        text2=TextMobject("\\text{s}")
        text2.set_color_by_tex("\\text{s}", BLUE)
        
        braces=Brace(tri,DOWN)
        text2.next_to(braces,DOWN)
        text2.scale(1.4)
        abc=TextMobject(r"$\triangle$","\\text{ABC is an equilateral triangle having}")
        side=TextMobject("\\text{side length}", "\\text{s}","\\text{and apothem}","\\text{a}")
        side.set_color_by_tex("\\text{s}", RED)
        side.set_color_by_tex("\\text{a}", RED)
        abc.shift(2.5*UP+3.7*LEFT)
        abc.scale(0.7)
        side.shift(2.15*UP+4.64*LEFT)
        side.scale(0.7)
        verynew=VGroup(text,text1,tri,braces,a1,b1,c1,text2,linnew,cir2,arc)
        
        self.play(ShowCreation(text),ShowCreation(text1),ShowCreation(text2),GrowFromCenter(braces),ShowCreation(abc),ShowCreation(side),run_time=3)
        angle=TextMobject(r"$\angle$","\\text{BAC is given by}",r"$\frac{360}{n}$","\\text{where n is the}")
        inpoly=TextMobject("\\text{number of sides of inscribed polygon}")
        angle.shift(UP+3.9*LEFT)
        angle.scale(0.7)
        inpoly.shift(0.55*UP+4*LEFT)
        inpoly.scale(0.7)
        self.play(ShowCreation(angle),ShowCreation(inpoly),ApplyMethod(verynew.shift,3*RIGHT),run_time=3)
        hexa1=RegularPolygon(n=6,color=RED)
        hexa1.shift(DOWN+6*LEFT)
        here=TextMobject("\\text{n=6}")
        here.move_to(hexa1)
        self.play(Write(hexa1),Write(here),run_time=3)
        erase=VGroup(abc,side,inpoly,angle)
        self.play(ApplyMethod(hexa1.shift,3*UP),ApplyMethod(here.shift,3*UP),FadeOut(erase),run_time=3)
        bac=TextMobject(r"$\angle$","\\text{BAC=60}","\\text{and}",r"$\theta$","\\text{= 30}")
        half=TextMobject("\\text{because}",r"$\theta$","\\text{=}",r"$\frac{180}{n}$")
        bac.shift(2*LEFT+2*UP)
        half.shift(1.3*UP+2*LEFT)
        x=VGroup(here,hexa1,bac,half)
        self.play(Write(bac),Write(half))
        tan=TextMobject("\\text{tan}"r"$\frac{180}{n}$","\\text{=}",r"$\frac{S}{2a}$")
        s1=TextMobject("\\text{s =}","\\text{2a}"r"$\cdot$""\\text{tan}"r"$\frac{180}{n}$")
        tan.shift(5*LEFT+2*UP)
        s1.shift(4.85*LEFT+1.1*UP)
        self.play(ReplacementTransform(x,tan),run_time=1.5)
        self.play(FadeIn(s1))
        area=TextMobject("\\text{area of triangle =}",r"$\frac{1}{2}$"r"$\cdot$""\\text{2a}"r"$\cdot$""\\text{tan}"r"$\frac{180}{n}$"r"$\cdot$""\\text{a}")
        area.shift(2.85*LEFT+0.2*UP)
        self.play(FadeIn(area))
        area1=TextMobject("\\text{=}","\\text{a}"r"$\cdot$""\\text{a}"r"$\cdot$""\\text{tan}"r"$\frac{180}{n}$")
        area2=TextMobject("\\text{As described earlier a=1 and n=6}")
        area3=TextMobject("\\text{area of triangle = tan30}")
        area4=TextMobject("\\text{area of polygon = n}"r"$\cdot$""\\text{tan}"r"$\frac{180}{n}$") 
        area5=TextMobject("\\text{area of hexagon = 6}"r"$\cdot$""\\text{tan30}")  
        area1.shift(1.5*LEFT+(-0.7*UP))
        self.play(Write(area1),run_time=1.5)
        self.play(FadeOut(area1),FadeOut(area),FadeOut(tan),FadeOut(s1),run_time=3)
        area2.shift(2*UP+3*LEFT)
        area3.shift(1.1*UP+3.28*LEFT)
        area4.shift(0.2*UP+2.98*LEFT)
        area5.shift(-0.7*UP+3*LEFT)
        
        self.play(FadeIn(area2))
        self.play(FadeIn(area3))
        self.play(FadeIn(area4))
        self.play(FadeIn(area5))
        self.wait(1)
        self.play(FadeOut(area2))
        self.play(FadeOut(area3))
        self.play(FadeOut(area4))
        self.play(FadeOut(area5))
        hexa2=RegularPolygon(n=6,color=RED)
        hexa2.scale(3)
        area6=TextMobject("\\text{Area = 3.46410161513775}") 
        area6.move_to(hexa2)
        self.play(ReplacementTransform(verynew,hexa2),run_time=1.5)
        self.play(ShowCreation(area6),run_time=3)
        self.wait(2)
        newgroup=VGroup(area6,hexa2)
        new2=SmallDot(color=BLACK)
        self.play(ReplacementTransform(newgroup,new2),run_time=1.5)
        self.wait(1)
        
