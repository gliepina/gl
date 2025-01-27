print("ievadiet naudas daudzumu")
N = int(input())
print("ievadiet kreklu cenu")
pirmacena= int(input())
print("ievadiet apavu cenu")
otracena = int(input())
krekli = 0
apavi = 0

kreklucena = N //pirmacena
apavucena = N //otracena
if(kreklucena>apavucena):
    print(kreklucena, apavucena, "krekli")
if kreklucena<apavucena:
    print(kreklucena, apavucena, "apavi")
if(kreklucena==apavucena):
    print(kreklucena, apavucena, "krekli un apavi")
