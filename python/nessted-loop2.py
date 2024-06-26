n = 5
0-5

for i in range(n):
    for j in range(n):
        print(i,j)

n = 5

print('*'*1)
print('*'*2)
print('*'*3)
print('*'*4)
print('*'*5)


for b in range(1,6):
    for c in range(1,b+1):
        print(c,end='')
    print()

n = 5

for i in range(0,n):
    for k in range(i,n):
        if i == k:
            continue
        else:
            print(i,k)
print()

'''
for i in  1 to n 
    for j  in 1 to j
       print j without new line
     print new line
'''

''' 
    1
   222
  33333
 4444444
555555555
 4444444
  33333
   222
    1'''
'''
สำหรับ ตัวเลข ใน ขอบเขต
    บรรทัด 1 ช่องว่าง * 4 เลข 1*1 ลงท้ายด้วย ช่องว่าง * 4
    บรรทัด 2 ช่องว่าง * 3 เลข 2*3 ลงท้ายด้วย ช่องว่าง * 3
    บรรทัด 3 ช่องว่าง * 2 เลข 3*5 ลงท้ายด้วย ช่องว่าง * 2
    บรรทัด 4 ช่องว่าง * 1 เลข 4*7 ลงท้ายด้วย ช่องว่าง * 1
    บรรทัด 5 ช่องว่าง * 0 เลข 5*9 ลงท้ายด้วย ช่องว่าง * 0
    บรรทัด 6 ช่องว่าง * 1 เลข 4*7 ลงท้ายด้วย ช่องว่าง * 1
    บรรทัด 7 ช่องว่าง * 2 เลข 3*5 ลงท้ายด้วย ช่องว่าง * 2
    บรรทัด 8 ช่องว่าง * 3 เลข 2*3 ลงท้ายด้วย ช่องว่าง * 3
    บรรทัด 9 ช่องว่าง * 2 เลข 3*5 ลงท้ายด้วย ช่องว่าง * 2
    บรรทัด 10 ช่องว่าง * 4 เลข 1*1 ลงท้ายด้วย ช่องว่าง * 4'''

# print line 1-5 
for b in range(1,6):
    # for loop print space multiply by time n-b 
    for c in range(n-b):
        print('_',end='')
    # for loop print line number multiply by x*2-1
    for c in range((b*2)-1):
        print(b,end='')
    # print new line
    print()
# print line 4-1 
for b in range(4,0,-1):
    # print space multiply by time n-b 
    print(' '*(n-b),end='')
    # print line number multiply by x*2-1
    print(str(b)* (b*2-1),end='')
    # print new line
    print()

l = 5

for d in range(1, l):
    for e in range(1,d):
        print(''*l,str(e)*e, end='')
        e +=1
    print()

'''
    1
   222
  33333
 4444444
555555555'''

'''
_1
__22
___333
____4444
_____55555'''


'''
guniversez
*
**
***
****
*****'''

'''1
12
123
1234
12345'''

'''
1
22
333
4444
55555'''