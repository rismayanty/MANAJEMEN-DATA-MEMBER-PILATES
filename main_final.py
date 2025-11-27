# di bagian import
import verifikasi_final as verif_module
from verifikasi_final import validasi_id,login, registrasi,generate_id,validasi_nama
from admin_final import menu_admin
from member_final import menu_member
from operasi_final import menu_utama, enquiry_menu
from final_final import keluar_program
users = {
    "A001": {"nama": "Maya", "usia": 19, "role": "admin"},
    "A002": {"nama": "Adri", "usia": 19, "role": "admin"},
    "A003": {"nama": "Cinta", "usia": 19, "role": "admin"},
    "M001": {"nama": "Riski", "usia": 20, "role": "member"},
    "M002": {"nama": "Dinda", "usia": 25, "role": "member"},
}

pilates_shain = {
    # contoh member sudah terdaftar di pilates_shain (boleh kosong)
    # "M001": {"nama": "Member Satu", "paket": "FULL", "durasi": "3", "jadwal": "Senin - 10:00"}
}

# list jadwal (string format "Hari - Waktu")
jadwal = ["Senin - 08:00 s/d 16:00","Selasa - 08:00 s/d 16:00","Rabu - 08:00 s/d 16:00",
          "Kamis - 08:00 s/d 16:00","Jumat - 08:00 s/d 16:00"]

maks_percobaan = 3

def main():
    program_berjalan = True
    while program_berjalan:
        pilih_menu = menu_utama()

        if pilih_menu == "1":
            try:
                registrasi(users)
            except Exception as e:
                print("Kesalahan registrasi:", e)

        elif pilih_menu == "2":
            try:
                hasil_login = login(users, maks_percobaan)
                if hasil_login:
                    current_user_id, current_user = hasil_login
                    if current_user["role"] == "admin":
                        # pass verif_module agar admin dapat pakai validasi/generate id
                        menu_admin(pilates_shain, jadwal, users, verif_module)
                    elif current_user["role"] == "member":
                        menu_member(pilates_shain, current_user, current_user_id, jadwal)
            except Exception as e:
                print("Kesalahan saat login:", e)

        elif pilih_menu == "3":
            enquiry_menu()
            input("ENTER...")

        elif pilih_menu == "4":
            keluar_program()
            program_berjalan = False

        else:
            print("PILIHAN TIDAK VALID!")

if __name__ == "__main__":
            main()