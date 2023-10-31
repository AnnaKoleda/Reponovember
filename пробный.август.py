num = int(input())
a = num
a1 = 0
while num!=0:
    last_num = num%10
    a1+=last_num
    num = num//10
 print (a1)

с2 = 0
while num!=0:
    last_num = num%10
    с2+=1
    num = num//10
print (c2)

с3 = 1
while num!=0:
    last_num = num%10
    с3=c3*last_num
    num = num//10
print (c3)

num = int(input())
с4 = 0
while num!=0:
    last_num = num%10
    с4+=last_num
    num = num//10
print (c4/c3)

c5 = a//10**(c2-1)
print (c5)

c6 = a%10
c7 = c5+c6
print (c7)
