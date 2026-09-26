#!/usr/bin/env python3
import math

A=(239.9881633256477,68.5117419161366)
POINTS={
 "raw_l2":(235.9,58.1,10.566755706598673),
 "raw_l3":(237.7,62.9,5.689168081519004),
 "inp_l2":(225.5,54.8,15.250342372927966),
 "inp_l3":(249.2,57.7,11.557415977400845),
 "isw_l2":(269.9,40.8,31.96616516173605),
 "isw_l3":(262.8,65.1,9.542028509380712),
}
def sep(p,q):
    l1,b1=map(math.radians,p)
    l2,b2=map(math.radians,q)
    dot=math.sin(b1)*math.sin(b2)+math.cos(b1)*math.cos(b2)*math.cos(l1-l2)
    dot=max(-1,min(1,dot))
    return math.degrees(math.acos(abs(dot)))
for k,(l,b,want) in POINTS.items():
    got=sep(A,(l,b))
    assert abs(got-want)<1e-10,(k,got,want)
raw=sep((235.9,58.1),(237.7,62.9))
assert abs(raw-4.88065785521028)<1e-10
print("PASS: WMAP9 directional crosscheck geometry reproduced.")
