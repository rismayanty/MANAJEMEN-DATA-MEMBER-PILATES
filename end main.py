from verif import login, registrasi
from admin import menu_admin
from member import menu_member
from operasi import welcome, menu_utama
from final import keluar_program

# ==========================
# DATA AWAL
# ==========================

users = {
    "0001": {"nama": "Admin Satu", "usia": 30, "role": "admin"},
    "0002": {"nama": "Admin Dua", "usia": 28, "role": "admin"},
    "0003": {"nama": "Admin Tiga", "usia": 35, "role": "admin"},

    "1001": {"nama": "Member Satu", "usia": 20, "role": "member"},
    "1002": {"nama": "Member Dua", "usia": 25, "role": "member"},
}

pilates_shain = {}
maks_percobaan = 3


# ==========================
# PROGRAM UTAMA
# ==========================

def main():
    program_berjalan = True
    while program_berjalan:
        pilih_menu = menu_utama()

        # --- REGISTRASI ---
        if pilih_menu == "1":
            try:
                registrasi(users)
            except Exception as e:
                print(f"Terjadi kesalahan saat registrasi: {e}")

        # --- LOGIN ---
        elif pilih_menu == "2":
            try:
                hasil_login = login(users, maks_percobaan)
                if hasil_login:
                    current_user_id, current_user = hasil_login

                    if current_user["role"] == "admin":
                        menu_admin(pilates_shain)

                    elif current_user["role"] == "member":
                        menu_member(pilates_shain, current_user, current_user_id)

            except Exception as e:
                print(f"Terjadi kesalahan saat login: {e}")

        # --- KELUAR ---
        elif pilih_menu == "3":
            keluar_program()
            program_berjalan = False

        else:
            print("PILIHAN TIDAK VALID!")


# ==========================
# MAIN EXECUTE
# ==========================

welcome()
main()