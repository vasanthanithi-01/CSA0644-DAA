num1=[2,3,2]
num2=[1,2]
set1=set(num1)
set2=set(num2)
a=0
b=0
for i in num1:
    if i in set2:
        a+=1

for i in num2:
    if i in set1:
        b+=1

print("[",a,",",b, "]")
