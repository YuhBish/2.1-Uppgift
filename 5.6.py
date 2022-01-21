datum=input("Skriv ett datum på det amerikanska sättet (mm-dd-åååå)")

usM1=datum[0]
usM2=datum[1]
usM=usM1+usM2

usD1=datum[3]
usD2=datum[4]
usD=usD1+usD2

usY1=datum[-4]
usY2=datum[-3]
usY3=datum[-2]
usY4=datum[-1]
usY=usY1+usY2+usY3+usY4

print("Såhär skrivs det på det svenska viset:")
print(usD,usM,usY)

