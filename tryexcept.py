sayi1 = input("SAYI1:")
sayi2 = input("SAYI2:")

try:
    sayi1 = int(sayi1)
    sayi2 = int(sayi2)
    print(sayi1/sayi2)

except ValueError:
    print("Lütfen onluk tabanlı bir sayı giriniz")
except ZeroDivisionError:
    print("Bir sayı sıfıra bölünemez")
#except (ValueError,ZeroDivisionError):
    #print("Bir hata oluştu")




