sayi=int(input("sayı giriniz: "))
asalMi=True
if sayi==1:
    print("asal degildir")
for i in range(2,sayi):
    if (sayi % i==0):
        asalMi=False
        break
if asalMi:
    print("sayı asal")
else:
    print("asal degil")