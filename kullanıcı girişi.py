defkullanıcı = "huerfanos"
defparola = "1234"

while True:
    kullanıcı = input("Kullanıcı adı:")
    parola = input("Parola")
    if (kullanıcı != defkullanıcı) or (parola != defparola):
        print("Hatalı girişi!")
    else:
        print("Hoşgeldiniz!")
        break




