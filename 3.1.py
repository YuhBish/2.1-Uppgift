tid=float(input("Hur många minuter per dag pratar du i telefonen?"))
totTid=tid*30
pris=totTid*10
if pris > 300:
    print("Det blir:", pris*0.9, "kr")
else:
    print("Det blir", pris)