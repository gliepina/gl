print("sāka skriet: ")
h1 = int(input())
m1 = int(input())
s1 = int(input())
print("beidza skriet: ")
h2 = int(input())
m2 = int(input())
s2 = int(input())

if m2<m1:
   h2 -=1
   m2+=60
if s2<s1:
   m2-=1
   s2 +=60

h3= h2-h1
m3= m2-m1
s3= s2-s1

print(h3,m3,s3)