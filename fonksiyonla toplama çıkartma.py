def toplama():
    print("toplama için 2 sayı yazınız")
    s1=int(input("1.sayı"))
    s2=int(input("2.sayı"))
    if s1+s2:
        print("sayıların toplamı =" , s1+s2)
    else:
        print("karakter ya da negatif sayı girmiş olabilir misin yavrum?")

def çıkartma():
    print("çıkartma için 2 sayı yazınız")
    s1=int(input("1.sayı"))
    s2=int(input("2.sayı"))
    if s1+s2:
        print("sayıların farkı=" , s1-s2)
    else:
        print("karakter ya da negatif sayı girmiş olabilir misin yavrum?")

while (True):
    print("toplama(1)")
    print("çıkartma(2)")
    il=int(input("işlem numarasını yazıp entera basın"))
    if il==1:
        toplama()
        break
    elif il==2:
        çıkartma()
        break
    else:
        print("1 ya da 2 yazarak yapmak istediğiniz işlemi seçmelisiniz. Tekrar deneyin")
