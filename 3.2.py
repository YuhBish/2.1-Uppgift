ggrV=float(input("Hur många gånger per vecka planerar du att komma?"))
yrPass=2000
dayPass=10
ggrTot=ggrV*51
if ggrTot>200:
    print("Köp årskortet [2000kr]")
else:
    print("Köp ett dagskort varje gång [10kr]")

