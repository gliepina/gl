import math
ax=int(input())
ay=int(input())
bx=int(input())
by=int(input())
cx=int(input())
cy=int(input())
ab=math.sqrt((ax-bx)**2+(ay-by)**2)
ac=math.sqrt((ax-cx)**2+(ay-cy)**2)
bc=math.sqrt((bx-cx)**2+(by-cy)**2)

if ab>ac and ab>bc:
    garakais=ab
    isais1=ac
    isais2=bc

elif bc>ac and bc>ab:
    garakais=bc
    isais1=ac
    isais2=ab

if garakais**2==isais1**2+isais2:
    print("ir taisnleņķis")
else:
    print("nav taisnleņķis")

