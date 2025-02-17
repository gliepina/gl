teikums = input()
vardi=teikums.split(" ") 
m=0
for vards in vardi:
    lielosk=0
    m+=1
    for i in range(len(vards)):
        if vards[i]>='A' and vards[i]<='Z':
            lielosk+=1
    if lielosk == len(vards):
        print(m)

