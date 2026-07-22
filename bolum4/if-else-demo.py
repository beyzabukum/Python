name=input("ad: ")
age=int(input("yas: "))
egitim=input("egitim durumu: ")

if age>=18:
    if (egitim=="lise") or (egitim=="üniversite"):
        print("Ehliyet alabilir.")
else:
    print("ehliyet alamaz.")        
