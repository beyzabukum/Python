name=input("ad: ")
age=int(input("yas: "))
egitim=input("egitim durumu: ")

if age>=18:
    if (egitim=="lise") or (egitim=="üniversite"):
        print("Ehliyet alabilir.")
else:
    print("ehliyet alamaz.")        

# yazili1= int(input("1. yazılı: "))
# yazili2= int(input("2. yazılı: "))
# sozlu= int(input("sözlü: "))

# ortalama = (yazili1 + yazili2 + sozlu) / 3

# if (ortalama >= 0) and (ortalama < 25):
#     print(f"ortalamanız: {ortalama} notunuz: 0")
# elif (ortalama >= 25) and (ortalama < 45):
#     print(f"ortalamanız: {ortalama} notunuz: 1")
# elif (ortalama >= 45) and (ortalama < 55):
#     print(f"ortalamanız: {ortalama} notunuz: 2")
# elif (ortalama >= 55) and (ortalama < 70):
#     print(f"ortalamanız: {ortalama} notunuz: 3")
# elif (ortalama >= 70) and (ortalama < 85):
#     print(f"ortalamanız: {ortalama} notunuz: 4")
# elif (ortalama >= 85) and (ortalama <= 100):
#     print(f"ortalamanız: {ortalama} notunuz: 5")
# else:
#     print("geçersiz not girdiniz.")
