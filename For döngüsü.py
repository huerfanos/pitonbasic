while True:
    s1=int(input("alt alta yazdırmak istediğin sayı"))
    if s1<=0:
        print("sıfır veya sıfırdan küçük sayı girmeyiniz")
    else:
        for x in range (1,s1):
            print(x)
