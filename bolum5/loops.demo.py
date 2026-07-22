import random
sayi=random.randint(1,100)
puan=0
hak=int(input("tahmin sayısı: "))
while(hak>0):
    hak-=1
    tahmin=int(input("tahmininizi yazınız: "))

    if(sayi==tahmin):
        print("tebrikler")
        break
    elif sayi>tahmin:
        print("yukarı")
    else:
        print("aşağı")

    if hak==0:
        print(f"hakkınız bitti.Tutulan sayı :{sayi}")
