#-*- coding: utf-8 -*-
#written by penis-dominator
y0 = .5
h = .1
a=0
b=1

def eiler(a,b,h,y0):
    y=y0
    x=a
    while x<b:
        print x,y
        y=y+h*(x+y**2) #yravnenie tut
        x=x+h

eiler(a,b,h,y0)
