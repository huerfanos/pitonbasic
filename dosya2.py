with open("yazilim.txt","r") as dosya:
    dosya.seek(10)
    print(dosya.read())
    dosya.seek(5)
    print(dosya.read())
    dosya.seek(10)
    print(dosya.read(3))


