teikums = input()
vardi=teikums.split(" ") 
alfabets=0
m=0
for vards in vardi:
    m+=1
    for i in range(len(vards)-1):
         if vards[i] < vards[i+1]:
            alfabets+=1
    if alfabets == len(vards):
        print("IR")
        print(m)
    else:
       print("NAV")
