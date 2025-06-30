bs = 0
toplam = 0
while 1 == 1:
    sayi = input("1-ikilik tabani onluk tabana cevirme\n"
                 "2-onluk tabani ikilik tabana cevirme\n"
                 "3-CIKIS")
    sayi = int(sayi)
    if sayi == 1:
        while 1 == 1:
            ikilik = input("onluk tabana cevrilecek ikilik tabanli sayi giriniz")
            ikilik = int(ikilik)

            Dogruluk = True
            ikilik_copy = ikilik
            while ikilik_copy != 0:
                mod = ikilik_copy % 10
                ikilik_copy = ikilik_copy - mod
                ikilik_copy = ikilik_copy / 10
                if mod != 0 and mod != 1:
                    print("ikilik tabanli sayi girmediniz.")
                    Dogruluk = False
                    break

            if Dogruluk == True:
                while ikilik != 0:
                    bas = ikilik % 10
                    toplam = toplam + (2 ** bs) * bas
                    bs += 1
                    ikilik = ikilik - bas
                    ikilik = ikilik / 10
                print(toplam)
                toplam = 0
                bs = 0
                break
    if sayi==2:
        onluk = input("ikilik tabana cevrilecek onluk tabanli bir sayi giriniz")
        onluk = int(onluk)
        kalan = " "
        while onluk != 0:
            kalan = str(onluk % 2) + kalan
            onluk = onluk // 2
        print(kalan)

    if sayi==3:
        break
