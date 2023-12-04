import random
import time

while True:
    # menu pont valasztó
    menu_pont = str(input("Bejelentkezés: 1 , Regisztárció: 2  |(1:2): "))
    print("")
    # bejelentkezés
    if menu_pont == "1":
        log_felhasznaló = input("Felhasználónév: ")
        log_jelszó = input("Jelszó: ")
        print("")
    # hibas jelszó estén
        while log_felhasznaló != reg_felhasznaló or log_jelszó != reg_jelszó:
            print("Helytelen Felhasznélónév vagy Jelszó")
            log_felhasznaló = input("Felhasználónév: ")
            log_jelszó = input("jelszó: ")
            print("")
    # ha sikeres a belépés ez történik:
        print(
            f"Sikeres Bejelentkezés, {log_felhasznaló} \n")
        # jatek valasztó
        while True:
            # 2.menu pont
            menu_pont2 = None
            # ha valamit elgépelnek
            while menu_pont2 != "1" or menu_pont2 != "2" or menu_pont2 != "3":
                menu_pont2 = str(
                    input("Dobókocka: 1, Kő-Papír-Olló 2, Szerencse Dobás 3 |(1-3): "))

                # menu pont lehetoseg 1

                if menu_pont2 == "1":
                    # kocka dobás
                    dobasod = input("nyomj Enter-t a dobáshoz")
                    Kocka_Szamok = [1, 2, 3, 4, 5, 6]
                    Eredmeny = random.choice(Kocka_Szamok)
                    print(f"Dobókocka dobása: {Eredmeny}")

                # menu pont lehetoseg 2

                elif menu_pont2 == "2":
                    # kő papíír ollós játék
                    valasztasod = str(input("Kő , Papír , Olló: "))
                    print("")
                    print(f"Választásod: {valasztasod}")
                    print
                    Elleneg_lehetosegei = ['Kő', 'Papír', 'Olló']
                    Ellenseg_valasztasa = random.choice(Elleneg_lehetosegei)
                    print(f"Ellenség választása: {Ellenseg_valasztasa}")
                    print("")

                # menu pont lehetesoeg 3

                elif menu_pont2 == "3":
                    kassza = 10000
                    jatott_korok = 0
                    # akar a felhasználó még játszani
                    jatek = input("Akarsz játszani?(igen-nem): ")
                    # a jelenlegi vagyonod
                    print(f"vagyonod: {kassza}HUF")
                    # ha a while igen akkor lefut a kod
                    while jatek == "igen":
                        # jatszott körök képlet
                        jatott_korok = jatott_korok+1
                        # randomizáció
                        tortenhet = [-700, 700]
                        tortenhet_tovabb = random.choice(tortenhet)
                        # pénzes dolgok
                        kassza = tortenhet_tovabb+kassza
                        # ki íratás
                        print(f"{kassza} HUF")
                        # jatszott korok
                        print(f"{jatott_korok}x játszott")
                        # jatek folytatása
                        jatek = input("Akarsz játszani?: ")

                else:
                    print("Valamit elgépelt")

    # regisztáció
    elif menu_pont == "2":
        reg_felhasznaló = input("Felhasználónév: ")
        reg_jelszó = input("jelszó: ")
        print("")
    # regisztációs adatok
        while reg_felhasznaló == "" or reg_jelszó == "":
            reg_felhasznaló = input("Felhasználónév: ")
            reg_jelszó = input("jelszó: ")
            print("")

    # sikeres regisztáció

        print(
            f"Sikeres Regisztáció, A felhasznéló neved: {reg_felhasznaló},A Jelszód pedig: {reg_jelszó}")

    # ha valami nem elront a felhasználó

    else:
        print("Valamit elronott kérem inditsa úrja a programot")

# Váradi Zsolt 10.A
