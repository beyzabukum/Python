"""
sayilar=[1,3,5,7,9,12,19,21]
i=0
while (i<len(sayilar)):
    print(sayilar[i])
    i+=1
"""
"""
start=int(input("baslangic giriniz: "))
end=int(input("bitis giriniz: "))
i=start
while(i<end):
    i+=1
    if(i%2==1):
     print(i)

"""
"""
i=100
while (i>0):
    print(i)
    i-=1

"""
numbers=[]
"""
i=0
while(i<5):
    sayi=int(input("sayi: "))
    numbers.append(sayi)
    i+=1

numbers.sort()
print(numbers)

"""
urunler=[]
adet=int(input("adet giriniz: "))
i=0
while(i<adet):
    name=input("ürün adı: ")
    price=int(input("ürün fiyat: "))
    urunler.append({
        "name":name,
        "price":price
    })
    i+=1
for urun in urunler:
    print(f"urun adı: {urun["name"]}  urun fiyatı: {urun["price"]}")