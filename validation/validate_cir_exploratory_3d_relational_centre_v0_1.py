#!/usr/bin/env python3
import math
import numpy as np

def vec(l,b):
    l=math.radians(l); b=math.radians(b)
    return np.array([
        math.cos(b)*math.cos(l),
        math.cos(b)*math.sin(l),
        math.sin(b)
    ],dtype=float)

def lb(v):
    v=v/np.linalg.norm(v)
    return (
        math.degrees(math.atan2(v[1],v[0]))%360.0,
        math.degrees(math.asin(v[2]))
    )

def cross_axis(p2,p3):
    a=vec(*p2); b=vec(*p3)
    gamma=math.acos(float(np.clip(abs(a@b),-1,1)))
    s=np.cross(a,b); s/=np.linalg.norm(s)
    return gamma,1/math.sin(gamma),lb(s)

cases={
 "raw":((235.9,58.1),(237.7,62.9),(4.88065785521028,11.753565170812795,(137.65831979352447,5.098818745494779))),
 "inpainted":((225.5,54.8),(249.2,57.7),(13.408392762564134,4.312382158230489,(71.97733752793756,32.26959225029267))),
 "isw":((269.9,40.8),(262.8,65.1),(24.638072141101908,2.398743787340636,(184.59977342776244,-5.422389616947123))),
}
for name,(p2,p3,want) in cases.items():
    g,c,a=cross_axis(p2,p3)
    wg,wc,wa=want
    assert abs(math.degrees(g)-wg)<1e-12
    assert abs(c-wc)<1e-12
    assert abs(a[0]-wa[0])<1e-12
    assert abs(a[1]-wa[1])<1e-12

d=2350.770443410027
s=vec(137.65831979352447,5.098818745494779)
xyz=d*s
want=np.array([-1730.67588034,1577.09681099,208.92181217])
assert np.max(np.abs(xyz-want))<1e-8
assert abs(np.linalg.norm(xyz)-d)<1e-10

print("PASS: exploratory 3D packet and WMAP processing-sensitivity geometry reproduced.")
