sers = {}
pilates_shain = {}
maks_percobaan = 3

def main():
    program_berjalan = True
    while program_berjalan:
        pilih_menu = menu_utama()

        if pilih_menu == "1":
            registrasi(users)
        elif pilih_menu == "2":
            hasil_login = login(users, maks_percobaan)
            if hasil_login:
                current_user_id, current_user = hasil_login
                if current_user["role"] == "admin":
                    menu_admin(pilates_shain)
                elif current_user["role"] == "member":
                    menu_member(pilates_shain, current_user, current_user_id)
        elif pilih_menu == "3":
            keluar_program()
            program_berjalan = False
        else:
            print("PILIHAN TIDAK VALID!")

if __name__ == "__main__":
    welcome()
    main()