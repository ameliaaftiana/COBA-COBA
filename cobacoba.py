#Soal laporan 1
bil1=int(input("Masukkan bilangan 1: "))
bil2=int(input("Masukkan bilangan 2: "))
bil3=int(input("Masukkan bilangan 3: "))
bil4=int(input("Masukkan bilangan 4: "))
bil5=int(input("Masukkan bilangan 5: "))

urut=[bil1,bil2,bil3,bil4,bil5]
urut.sort()
print("maka bilangan keduanya adalah", urut[3])

#Soal laporan 2
bill1=input("bil 1 = ")
bill2=input("bill 2 = ")

if bill1[0]==bill2[0] or bill1[0]==bill2[1] or bill1[1]==bill2[0] or bill1[1]==bill2[1]:
    print ("sama")
else:
    print("tidak sama")


#Soal laporan 3
bilangan1=input("Bil 1 = ")
bilangan2=input("Bil 2 = ")
bilangan3=input("Bil 3 = ")

bb=bilangan1[-1]
bc=bilangan2[-1]

if int(bb)<5:
    bil1baru=int(bilangan1)-int(bb)
    print(bil1baru)
elif int(bc)<5:
    bil2baru = int(bilangan2)-int(bc)
    print(bil2baru)
