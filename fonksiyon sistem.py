def işlem():
    print("(1) Toplama")
    print("(2) Çıkartma")
    print("(3) Çarpma")
    print("(4) Bölme")
    s1=input("İstediğiniz işlemi seçin")
    if s1=="1":
        i1=int(input("1.sayı"))
        i2=int(input("2.sayı"))
        print("sayıların toplamı", i1 + i2)
    elif s1 =="2":
        i1=int(input("1.sayı"))
        i2=int(input("2.sayı"))
        print("sayıların farkı" , i1 - i2)

    elif s1 == "3":
        i1 = int(input("1.sayı"))
        i2 = int(input("2.sayı"))
        print("sayıların çarpımı", i1 * i2)

    elif s1 == "4":
        i1 = int(input("1.sayı"))
        i2 = int(input("2.sayı"))
        print("sayıların bölümü", i1 / i2)

def rehber():
    s1=input("rehberde aramak istediğiniz kişinin ismi")
    if s1 =="a":
        print("kişi X")
    elif s1=="b":
        print("kişi Y")
    elif s1=="c":
        print("kişi Z")



while(True):

    s1=input("kullanıcı adı:")
    s2=input("şifre")
    if s1== "huerfanos":
        if s2=="1234":
            print("işlem")
            print("rehber")
            so=input("hangi işlemi gerçekleştireyim?")
            if so =="rehber":
                rehber()
            elif so == "işlem":
                işlem()
            else:
                print("böyle bişey yok ki , işlem ya da rehber yazman gerekiyor")
        else:
            print("yanlış şifre")
    else:
        print("yanlış kullanıcı adı")

