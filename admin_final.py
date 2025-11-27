from prettytable import PrettyTable
from operasi_final import opsi_paket, biaya_pilates, JADWAL_PILATES

def menu_admin(pilates_shain, jadwal, users):
    print("\n🎀 MANAJEMEN DATA MEMBER PILATES 🎀".center(60))
    print("=" * 60)
    print("1. TAMBAH DATA")
    print("2. TAMPILKAN DATA (dengan SEARCH)")
    print("3. UBAH DATA")
    print("4. HAPUS DATA")
    print("5. LOGOUT")
    print("=" * 60)

    pilih = input("PILIH MENU: ")

    if pilih == "1":
        try:
            from operasi_final import tampilkan_jadwal_pretty
            print("\n📆 JADWAL STUDIO YANG TERSEDIA:")
            tampilkan_jadwal_pretty(jadwal)

            id_member = input("\nID MEMBER: ")
            if id_member in pilates_shain:
                print("ID MEMBER SUDAH TERDAFTAR!")
                return menu_admin(pilates_shain, jadwal, users)

            nama = input("NAMA: ")
            paket = input("PAKET PILATES (BASIC/FOAM/LEGS/FULL/RINGAN): ").upper()
            if paket not in opsi_paket:
                print("PAKET TIDAK VALID!")
                return menu_admin(pilates_shain, jadwal, users)

            durasi = input("DURASI MEMBERSHIP (bulan): ")
            if not durasi.isdigit():
                print("DURASI WAJIB ANGKA!")
                return menu_admin(pilates_shain, jadwal, users)

            print("\nContoh format jadwal: Senin - 10:00")
            jadwal_pilih = input("PILIH JADWAL PILATES: ")

            pilates_shain[id_member] = {
                "nama": nama,
                "paket": paket,
                "durasi": durasi,
                "jadwal": jadwal_pilih
            }
            print("๑ ⋆₊⋆─ʚ DATA BERHASIL DITAMBAHKAN ɞ─⋆₊⋆ ๑")

        except Exception as e:
            print("TERJADI KESALAHAN:", e)

    elif pilih == "2":
        if not pilates_shain:
            print("BELUM ADA DATA MEMBER (╥﹏╥)")
            return menu_admin(pilates_shain, jadwal, users)

        print("\n1. TAMPILKAN SEMUA")
        print("2. CARI MEMBER")
        sub = input("PILIHAN: ")

        if sub == "1":
            table = PrettyTable()
            table.field_names = ["ID", "Nama", "Paket", "Durasi", "Biaya", "Jadwal"]
            table.align = "l"
            for id_m, data in pilates_shain.items():
                biaya = biaya_pilates(data["paket"], data["durasi"])
                table.add_row([id_m, data["nama"], data["paket"], data["durasi"], biaya, data["jadwal"]])
            print("\n📊 DATA MEMBER PILATES")
            print(table)

        elif sub == "2":
            keyword = input("MASUKKAN NAMA / ID / JADWAL: ").lower()
            table = PrettyTable()
            table.field_names = ["ID", "NAMA", "PAKET", "DURASI", "BIAYA", "JADWAL"]
            ketemu = False
            for id_m, data in pilates_shain.items():
                if (keyword in id_m.lower() or
                    keyword in data["nama"].lower() or
                    keyword in data["jadwal"].lower()):
                    biaya = biaya_pilates(data["paket"], data["durasi"])
                    table.add_row([id_m, data["nama"], data["paket"], data["durasi"], biaya, data["jadwal"]])
                    ketemu = True
            if ketemu:
                print("\n📌 HASIL PENCARIAN")
                print(table)
            else:
                print("DATA TIDAK DITEMUKAN!")

        else:
            print("PILIHAN TIDAK VALID!")

    elif pilih == "3":
        try:
            id_m = input("MASUKKAN ID MEMBER: ")
            if id_m not in pilates_shain:
                print("DATA TIDAK DITEMUKAN!")
                return menu_admin(pilates_shain, jadwal, users)
            nama_baru = input("NAMA BARU: ")
            paket_baru = input("PAKET BARU: ").upper()
            durasi_baru = input("DURASI BARU: ")
            jadwal_baru = input("JADWAL BARU: ")
            if not durasi_baru.isdigit():
                print("DURASI WAJIB ANGKA!")
                return menu_admin(pilates_shain, jadwal, users)
            pilates_shain[id_m] = {
                "nama": nama_baru,
                "paket": paket_baru,
                "durasi": durasi_baru,
                "jadwal": jadwal_baru
            }
            print("ꔫ DATA BERHASIL DIUBAH ꔫ")

        except Exception as e:
            print("TERJADI KESALAHAN:", e)

    elif pilih == "4":
        try:
            id_m = input("MASUKKAN ID MEMBER YANG INGIN DIHAPUS: ")
            if id_m in pilates_shain:
                del pilates_shain[id_m]
                print("ꔫ DATA BERHASIL DIHAPUS ꔫ")
            else:
                print("DATA TIDAK DITEMUKAN!")
        except Exception as e:
            print("KESALAHAN TERJADI:", e)

    elif pilih == "5":
        print("LOGOUT BERHASIL ⭢ KEMBALI KE MENU UTAMA")
        return

    else:
        print("PILIHAN TIDAK VALID!")

    return menu_admin(pilates_shain, jadwal, users)
from verifikasi_final import validasi_nama
import os

JADWAL_PILATES = [{"hari":"Senin", "waktu":  "08:00 s/d 16:00",  "paket":"RINGAN", "harga":100000},
                   {"hari":"Selasa", "waktu":  "08:00 s/d 16:00", "paket":"BASIC", "harga":150000},
                   {"hari":"Rabu", "waktu":  "08:00 s/d 16:00",  "paket":"FOAM", "harga":200000},
                   {"hari":"Kamis", "waktu":  "08:00 s/d 16:00", "paket":"LEGS", "harga":250000},
                   {"hari":"Jum'at", "waktu":  "08:00 s/d 16:00", "paket":"FULL", "harga":500000},
                   {"hari":"Sabtu", "waktu":  "08:00 s/d 16:00", "paket":"BASIC", "harga":150000},
                   {"hari":"Minggu", "waktu":  "08:00 s/d 16:00", "paket":"Ringan", "harga":100000}

]
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# ===============================================================
#                  MENU ADMIN (5 PILIHAN)
# ===============================================================
def menu_admin(users, pilates_shain, jadwal_kelas,verif_module):
    while True:
        print("\n╔══════ MENU ADMIN ══════╗")
        print("1. Lihat Data Pengguna & Jadwal Member")
        print("2. Tambah Pengguna")
        print("3. Ubah Data Pengguna")
        print("4. Hapus Data Pengguna")
        print("5. Logout")
        print("╚════════════════════════╝")

        pilih = input("Pilih menu: ").strip()

        if pilih == "1":
            submenu_data_admin(users, pilates_shain, jadwal_kelas)

        elif pilih == "2":
            tambah_pengguna_admin(users)

        elif pilih == "3":
            update_pengguna(users)

        elif pilih == "4":
            hapus_pengguna(users)

        elif pilih == "5":
            print("Logout berhasil...")
            return

        else:
            print("Pilihan tidak valid!")


# ===============================================================
#                  SUBMENU DATA (PILIHAN 1)
# ===============================================================
def submenu_data_admin(users, pilates_shain, jadwal_kelas):
    while True:
        print("\n=== SUBMENU DATA ADMIN ===")
        print("1. Lihat Semua Data Pengguna")
        print("2. Cari Member & Lihat Jadwalnya")
        print("3. Kembali")

        p = input("Pilih: ").strip()

        if p == "1":
            tampilkan_semua_pengguna(users)

        elif p == "2":
            cari_lihat_jadwal_member(users, pilates_shain, jadwal_kelas)

        elif p == "3":
            return

        else:
            print("Pilihan tidak valid!")


# ===============================================================
#            LIHAT SEMUA PENGGUNA (ADMIN & MEMBER)
# ===============================================================
def tampilkan_semua_pengguna(users):
    if not users:
        print("Belum ada data pengguna.")
        return

    table = PrettyTable()
    table.field_names = ["ID", "Nama", "Usia", "Role","Paket","Durasi","Jadwal"]

    for uid, data in users.items():
        table.add_row([uid, data["nama"], data["usia"], data["role"],data.get("paket","-"),data.get("durasi","-"),data.get("jadwal","-")])

    print("\n=== DATA PENGGUNA ===")
    print(table)


# ===============================================================
#          CARI MEMBER & LIHAT JADWALNYA
# ===============================================================
def cari_lihat_jadwal_member(users, pilates_shain, jadwal_kelas):
    keyword = input("Masukkan ID / Nama Member: ").strip().lower()
    ditemukan = None

    for uid, data in users.items():
        if keyword in uid.lower() or keyword in data["nama"].lower():
            if data["role"] == "member":
                ditemukan = uid
                break

    if not ditemukan:
        print("Member tidak ditemukan.")
        return

    print(f"\n=== DATA MEMBER {ditemukan} ===")
    print(f"Nama  : {users[ditemukan]['nama']}")
    print(f"Usia  : {users[ditemukan]['usia']} tahun")

    # tampilkan status member
    if ditemukan in pilates_shain:
        paket = pilates_shain[ditemukan]["paket"]
        durasi = pilates_shain[ditemukan]["durasi"]
        print(f"Paket : {paket}")
        print(f"Durasi: {durasi} bulan")
        print(f"Jadwal: {pilates_shain[ditemukan]['jadwal']}")
        print(f"Tagihan: Rp {JADWAL_PILATES(paket, durasi)}")
    else:
        print("Belum terdaftar sebagai member.")

    # tampilkan jadwalnya
    print("\n=== JADWAL MEMBER ===")
    if ditemukan in jadwal_kelas:
        print(f"Kelas: {jadwal_kelas[ditemukan]}")
    else:
        print("Belum memilih jadwal kelas.")


# ===============================================================
#                TAMBAH PENGGUNA DARI ADMIN
# ===============================================================
def tambah_pengguna_admin(users):
    print("\n=== TAMBAH PENGGUNA ===")

    try:
        nama = input("Nama: ").strip()
        if not validasi_nama(nama):
            print("Nama tidak valid!")
            return

        usia = input("Usia (12–40): ").strip()
        if not usia.isdigit() or not (12 <= int(usia) <= 40):
            print("Usia tidak valid!")
            return

        role = input("Role (admin/member): ").strip().lower()
        if role not in ["admin", "member"]:
            print("Role tidak valid!")
            return
        
        paket = input("Paket (BASIC/FOAM/LEGS/FULL/RINGAN): ").upper().strip()
        if not paket in paket:
            print("Paket tidak valid!")
            return
        durasi = input("Durasi (bulan): ").strip()
        if not durasi.isdigit():
            print("Durasi harus angka!")
            return
        jadwal_paket = [j for j in JADWAL_PILATES if j["paket"]==paket]
        if not jadwal_paket:
            print(f"Paket dan jadwal tidak tersedia!{paket}.")
            return menu_admin
        
        print(f"\n jadwal tersedia untuk paket {paket}:")
        for i, j in enumerate(jadwal_paket, start=1):
            print(f"{i}. {j['hari']} - {j['waktu']})")

            pilih_jadwal =  input(f"pilih nomor jadwal (1-{len(jadwal_paket)}): ")
            if not pilih_jadwal.isdigit() or not (1 <= int(pilih_jadwal) <= len(jadwal_paket)):
                print("Nomor jadwal tidak valid!")
                return menu_admin
            
            j_terpilih = jadwal_paket[int(pilih_jadwal)-1]
            jadwal_str = f"{j_terpilih['hari']}, {j_terpilih['waktu']}({j_terpilih['paket']})"
        
        
        # generate ID otomatis
        prefix = "A" if role == "admin" else "M"
        nomor = 1
        while True:
            uid = f"{prefix}{nomor:03d}"
            if uid not in users:
                break
            nomor += 1
        
        users[uid] = {
            "nama": nama,
            "usia": int(usia),
            "role": role,
            "paket" : paket,
            "durasi" : durasi,
            "jadwal" : jadwal_str
            
        }


        print(f"Pengguna berhasil ditambahkan!= {uid}")

    except:
        print("Terjadi kesalahan saat menambah pengguna.")


# ===============================================================
#                UPDATE / UBAH DATA PENGGUNA
# ===============================================================
def update_pengguna(users):
    tampilkan_semua_pengguna(users)
    uid = input("Masukkan ID yang akan diubah: ").strip().upper()

    if uid not in users:
        print("ID tidak ditemukan.")
        return

    print("\n=== Ubah Data ===")
    new_name = input("Nama baru: ").strip()
    if not validasi_nama(new_name):
        print("Nama tidak valid.")
        return

    new_age = input("Usia baru (12–40): ").strip()
    if not new_age.isdigit() or not (12 <= int(new_age) <= 40):
        print("Usia tidak valid.")
        return

    users[uid]["nama"] = new_name
    users[uid]["usia"] = int(new_age)
    print("Data berhasil diubah!")


# ===============================================================
#                HAPUS PENGGUNA
# ===============================================================
def hapus_pengguna(users):
    tampilkan_semua_pengguna(users)

    uid = input("Masukkan ID yang akan dihapus: ").strip().upper()

    if uid not in users:
        print("ID tidak ditemukan.")
        return

    del users[uid]
    print("Pengguna berhasil dihapus!")
