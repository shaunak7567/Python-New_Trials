
import os
print(os.getcwd())
mins=[1,2,3,4,5]
secs=[m * 60 for m in mins]
print(secs)

feet=[10,20,30]
inches=[m *12 for m in feet]
print(inches)

feet=[22,24,30]
meters=[m*381/1250 for m in feet]
print(meters)

names=['shaunak','preeti']
upp=[names.upper() for names in names]
print(upp)

names=['SHAUNAK','PREETI']
low=[names.lower() for names in names]
print(low)




def sanit(l1):
    if '-' in l1:
        spl='-'
            
    elif ':' in l1:
        spl=':'
    else:
        return (l1)
    (mins1,secs1)=l1.split(spl)
    
    return(mins1 + '.' +secs1)

l1=['2.12','2-32','4-56']
x1=sanit(l1)
print(x1)







fo = open('d1.txt', 'r')
str1 = fo.read();
print ("Read String is : ", str1)
# Close opend file
fo.close()
     
