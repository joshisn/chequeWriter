befDec = "12345"
#prn = befDec[-len(befDec)+3*n:-len(befDec)+3*(n-1)]
prn = befDec[-len(befDec)+3:]
#print(befDec[-6:-3])
#print(befDec[len(befDec)-8:len(befDec)-6])
#print(int(len(befDec)/3))
#print(len(befDec)-(3*1))
#for n in range(0, int(len(befDec)/3)+1):
#    print(n)
powers = ["Hundred", "Thousand", "Hundred Thousand", "Million", "Million+", "Millions more"]
i = 0
for n in range(0, int(len(befDec)/3)):
    prn1 = befDec[len(befDec)-((3*n)+3):len(befDec)-(3*n)]
    print(prn1)
    i += 1

subPow = len(befDec)%3
if subPow != 0:
    prn2 = befDec[0:subPow]
    print(prn2)
    i += 1
else:
    print("No subPow")
#print(len(befDec))
print("i is equal to:", i)
print(powers[i-1])