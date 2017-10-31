def factoriel(numara):
    faktöriyel =1
    for i in range (1,numara+1):
        faktöriyel *=i
    print("Faktöriyel:",faktöriyel)
sayi= int(input("Sayıyı giriniz"))

factoriel(sayi)

