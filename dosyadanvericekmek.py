
try:
    dosya = open("yazilim.txt", "r")
    print(dosya.read())
    #print(dosya.readline())
    #print(dosya.readlines())
    dosya.close()

except FileNotFoundError:
    print("Dosya bulunamadı")


