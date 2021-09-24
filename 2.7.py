import math
import math
r=float(input("Vad är radien på din cirkel i cm?"))
o=r*2*math.pi
a=math.pi*(r*r)
x=round(o,3)
y=round(a,3)
print("Din cirkels omkräts är", x, "\nDin cirkels area är", y)