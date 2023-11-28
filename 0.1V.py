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

    # ha sikeres a belépés
        print(
            f"Sikeres Bejelentkezés, {log_felhasznaló}")
        # jatek valasztó
        while True:
            menu_pont2 = int(input("Dobókocka: 1, Kő-Papír-Olló 2 |(1:2): "))
            if menu_pont2 == 1:
                # kocka dobás
                dobasod = input("nyomj Enter-t a dobáshoz")
                Kocka_Szamok = [1, 2, 3, 4, 5, 6]
                Eredmeny = random.choice(Kocka_Szamok)
                print(f"Dobókocka dobása: {Eredmeny}")

            else:
                print("")

            if menu_pont2 == 2:
                # kő papíír ollós játék
                valasztasod = str(input("Kő , Papír , Olló: "))
                print("")
                print(f"Választásod: {valasztasod}")
                print
                Elleneg_lehetosegei = ['Kő', 'Papír', 'Olló']
                Ellenseg_valasztasa = random.choice(Elleneg_lehetosegei)
                print(f"Ellenség választása: {Ellenseg_valasztasa}")
                print("")

            else:
                print("")

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
