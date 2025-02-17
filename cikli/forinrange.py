teikums = input()
vardi=teikums.split(" ") 
visulielosk=0
     #2uzd
for vards in vardi:
    lielosk=0
    for i in range(len(vards)):
        if vards[i]>='A' and vards[i]<='Z':
            lielosk+=1
    print(lielosk)

    #1uzd
for i in range (len(teikums)):
    if teikums[i]>='A' and teikums[i]<='Z':
        visulielosk+=1

if visulielosk>0:
    print ("IR DRUKATS")
if visulielosk==0:
    print ("NAV DRUKATS")
