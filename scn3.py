from numpy import *
from manimlib.imports import *
from math import *
import numpy as np

class Polygon1(Scene):
    def construct(self):
        n=[]
        p=[]
        g=math.radians(360)
        x=[25,30,40,50,300,500,700,1000]
        y=[3.1582344611527,3.15312705797029,3.14806827298474,3.14573336268249,3.14170749668916, 3.14163399594489, 3.14161374646496, 3.14160298905616]
        for j in range(2,20):
            j+=1
            n.append(j)
        for i in n:
            f=0.5*(math.tan(g/(2*i)))*2*i
            i+=1
            p.append(round(f,14))
        cir=SmallDot(color=RED)
        tri=RegularPolygon(3)
        sq=RegularPolygon(4)
        pen=RegularPolygon(5)
        hexa = RegularPolygon(6)
        hep = RegularPolygon(7)
        octa = RegularPolygon(8)
        non = RegularPolygon(9)
        dec = RegularPolygon(10)
        undec = RegularPolygon(11)
        dodec = RegularPolygon(12)
        tridec = RegularPolygon(13)
        four= RegularPolygon(14)
        five= RegularPolygon(15)
        six= RegularPolygon(16)
        sev= RegularPolygon(17)
        nine= RegularPolygon(19)
        twen= RegularPolygon(20)
        tfive= RegularPolygon(25)
        thirt= RegularPolygon(30)
        fort= RegularPolygon(40)
        fift= RegularPolygon(50)
        threeh=RegularPolygon(300)
        fiveh=RegularPolygon(500)
        sevh=RegularPolygon(700)
        thou=RegularPolygon(1000)

        a = tri.get_vertices()
        lin=Line(cir, a[0])
        lin2=Line(cir, a[1])

        b = sq.get_vertices()
        lin3=Line(cir, b[0])
        lin4=Line(cir, b[1])

        c = pen.get_vertices()
        lin5=Line(cir, c[0])
        lin6=Line(cir, c[1])

        d = hexa.get_vertices()
        lin7=Line(cir, d[0])
        lin8=Line(cir, d[1])

        e = hep.get_vertices()
        lin9=Line(cir, e[0])
        lin10=Line(cir, e[1])

        h = octa.get_vertices()
        lin11=Line(cir, h[0])
        lin12=Line(cir, h[1])

        k = non.get_vertices()
        lin13=Line(cir, k[0])
        lin14=Line(cir, k[1])

        l = dec.get_vertices()
        lin15=Line(cir, l[0])
        lin16=Line(cir, l[1])

        m = undec.get_vertices()
        lin17=Line(cir, m[0])
        lin18=Line(cir, m[1])

        o = dodec.get_vertices()
        lin19=Line(cir, o[0])
        lin20=Line(cir, o[1])

        q = tridec.get_vertices()
        lin21=Line(cir, q[0])
        lin22=Line(cir, q[1])

        r = four.get_vertices()
        lin23=Line(cir, r[0])
        lin24=Line(cir, r[1])

        s = five.get_vertices()
        lin25=Line(cir, s[0])
        lin26=Line(cir, s[1])

        t = six.get_vertices()
        lin27=Line(cir, t[0])
        lin28=Line(cir, t[1])

        u = sev.get_vertices()
        lin29=Line(cir, u[0])
        lin30=Line(cir, u[1])

        v = nine.get_vertices()
        lin31=Line(cir, v[0])
        lin32=Line(cir, v[1])

        w = twen.get_vertices()
        lin33=Line(cir, w[0])
        lin34=Line(cir, w[1])

        z = tfive.get_vertices()
        lin35=Line(cir, z[0])
        lin36=Line(cir, z[1])

        za = thirt.get_vertices()
        lin37=Line(cir, za[0])
        lin38=Line(cir, za[1])

        zb = fort.get_vertices()
        lin39=Line(cir, zb[0])
        lin40=Line(cir, zb[1])

        zc = fift.get_vertices()
        lin41=Line(cir, zc[0])
        lin42=Line(cir, zc[1])

        zd = threeh.get_vertices()
        lin43=Line(cir, zd[0])
        lin44=Line(cir, zd[1])

        ze = fiveh.get_vertices()
        lin45=Line(cir, ze[0])
        lin46=Line(cir, ze[1])

        zf = sevh.get_vertices()
        lin47=Line(cir, zf[0])
        lin48=Line(cir, zf[1])

        zg= thou.get_vertices()
        lin49=Line(cir, zg[0])
        lin50=Line(cir, zg[1])


        a1=VGroup(lin,lin2)
        a2=VGroup(lin3,lin4)
        a3=VGroup(lin5,lin6)
        a4=VGroup(lin7,lin8)
        a5=VGroup(lin9,lin10)
        a6=VGroup(lin11,lin12)
        a7=VGroup(lin13,lin14)
        a8=VGroup(lin15,lin16)
        a9=VGroup(lin17,lin18)
        a10=VGroup(lin19,lin20)
        a11=VGroup(lin21,lin22)
        a12=VGroup(lin23,lin24)
        a13=VGroup(lin25,lin26)
        a14=VGroup(lin27,lin28)
        a15=VGroup(lin29,lin30)
        a16=VGroup(lin31,lin32)
        a17=VGroup(lin33,lin34)
        a18=VGroup(lin35,lin36)
        a19=VGroup(lin37,lin38)
        a20=VGroup(lin39,lin40)
        a21=VGroup(lin41,lin42)
        a22=VGroup(lin43,lin44)
        a23=VGroup(lin45,lin46)
        a24=VGroup(lin47,lin48)
        a25=VGroup(lin49,lin50)

        sc=VGroup(tri,sq,pen,hexa,hep,octa,non,dec,undec,dodec,tridec,four,five,six,sev,nine,twen,tfive,thirt,fort,fift,threeh,fiveh,sevh,thou)
        every=VGroup(sc,cir,a1,a2,a3,a4,a5,a6,a7,a8,a9,a10,a11,a12,a13,a14,a15,a16,a17,a18,a19,a20,a21,a22,a23,a24,a25)
        every.scale(3)
        self.play(GrowFromCenter(four),ShowCreation(cir),ShowCreation(a12))
        text=TextMobject(r"n =")
        text8=TextMobject(r"$\pi =$")
        text.to_corner(DOWN+1*LEFT)
        text8.to_corner(2*DOWN+1*LEFT)
        self.play(ShowCreation(text),ShowCreation(text8))
        text1 = TextMobject(n[11])
        text2 = TextMobject(p[11])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        self.play(ReplacementTransform(four,five),ReplacementTransform(a12,a13))
        text1 = TextMobject(n[12])
        text2 = TextMobject(p[12])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        self.play(ReplacementTransform(five,six),ReplacementTransform(a13,a14))
        text1 = TextMobject(n[13])
        text2 = TextMobject(p[13])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        self.play(ReplacementTransform(six,sev),ReplacementTransform(a14,a15))
        text1 = TextMobject(n[14])
        text2 = TextMobject(p[14])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        self.play(ReplacementTransform(sev,nine),ReplacementTransform(a15,a16))
        text1 = TextMobject(n[15])
        text2 = TextMobject(p[15])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        self.play(ReplacementTransform(nine,twen),ReplacementTransform(a16,a17))
        text1 = TextMobject(n[16])
        text2 = TextMobject(p[16])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        self.play(ReplacementTransform(twen,tfive),ReplacementTransform(a17,a18))
        text1 = TextMobject(n[17])
        text2 = TextMobject(p[17])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        self.play(ReplacementTransform(tfive,thirt),ReplacementTransform(a18,a19))
        text1 = TextMobject(x[0])
        text2 = TextMobject(y[0])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        self.play(ReplacementTransform(thirt,fort),ReplacementTransform(a19,a20))
        text1 = TextMobject(x[1])
        text2 = TextMobject(y[1])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        self.play(ReplacementTransform(fort,fift),ReplacementTransform(a20,a21))
        text1 = TextMobject(x[2])
        text2 = TextMobject(y[2])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        self.play(ReplacementTransform(fift,threeh),ReplacementTransform(a21,a22))
        text1 = TextMobject(x[3])
        text2 = TextMobject(y[3])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        self.play(ReplacementTransform(threeh,fiveh),ReplacementTransform(a22,a23))
        text1 = TextMobject(x[4])
        text2 = TextMobject(y[4])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        text1 = TextMobject(x[5])
        text2 = TextMobject(y[5])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        self.play(ReplacementTransform(fiveh,sevh),ReplacementTransform(a23,a24))
        text1 = TextMobject(x[6])
        text2 = TextMobject(y[6])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2))
        text1 = TextMobject(x[7])
        text2 = TextMobject(y[7])
        text1.to_corner(DOWN+3*LEFT)
        text2.to_corner(2*DOWN+3*LEFT)
        self.play(ShowCreation(text1),ShowCreation(text2))
        self.wait(0)
        self.play(ReplacementTransform(sevh,thou),ReplacementTransform(a24,a25))
        self.wait(0)
        self.play(FadeOut(text1),FadeOut(text2),FadeOut(text),FadeOut(text8))
        text3 = TextMobject(r"n=",x[7])
        text4 = TextMobject(r"$\pi =$",y[7])
        text3.shift(0.7*DOWN)
        y=VGroup(text3,text4)
        self.play(FadeOut(a25),FadeOut(cir))
        self.play(ReplacementTransform(thou,y))
        self.wait(2)

