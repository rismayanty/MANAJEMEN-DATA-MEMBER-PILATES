from prettytable import PrettyTable
from operasi import data_member, opsi_paket, biaya_pilates

JADWAL_PILATES = [
    {"hari": "Senin",    "waktu": "17.00-18.00", "paket": "RINGAN", "harga": 100000},
    {"hari": "Selasa",   "waktu": "17.00-18.00", "paket": "BASIC", "harga": 150000},
    {"hari": "Rabu",     "waktu": "17.00-18.00", "paket": "FOAM", "harga": 200000},
    {"hari": "Kamis",    "waktu": "19.00-20.00", "paket": "LEGS", "harga": 250000},
    {"hari": "Jumat",    "waktu": "17.00-18.00", "paket": "FULL", "harga": 500000},
    {"hari": "Sabtu",    "waktu": "08.00-09.00", "paket": "BASIC", "harga": 150000},
    {"hari": "Minggu",   "waktu": "08.00-09.00", "paket": "RINGAN", "harga": 100000}
]
  
def menu_admin(pilates_shain):
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
            id_member = input("ID MEMBER: ")
            if id_member in pilates_shain:
                print("ID MEMBER SUDAH TERDAFTAR!")
                return menu_admin(pilates_shain)

            nama = input("NAMA: ")

            paket = input("PAKET PILATES (BASIC/FOAM/LEGS/FULL/RINGAN): ").upper()
            if paket not in opsi_paket:
                print("PAKET TIDAK VALID!")
                return menu_admin(pilates_shain)

            durasi = input("DURASI MEMBERSHIP (bulan): ")
            if not durasi.isdigit():
                print("DURASI WAJIB ANGKA!")
                return menu_admin(pilates_shain)

            jadwal_paket = [j for j in JADWAL_PILATES if j["paket"] == paket]
            if not jadwal_paket:
                print(f"Tidak ada jadwal tersedia untuk paket {paket}.")
                return menu_admin(pilates_shain)

            print(f"\nJadwal tersedia untuk paket {paket}:")
            for i, j in enumerate(jadwal_paket, 1):
                print(f"{i}. {j['hari']}, {j['waktu']}")

            pilih_jadwal = input(f"Pilih nomor jadwal (1-{len(jadwal_paket)}): ")
            if not (pilih_jadwal.isdigit() and 1 <= int(pilih_jadwal) <= len(jadwal_paket)):
                print("Pilihan jadwal tidak valid!")
                return menu_admin(pilates_shain)

            j_terpilih = jadwal_paket[int(pilih_jadwal) - 1]
            jadwal_str = f"{j_terpilih['hari']}, {j_terpilih['waktu']} ({j_terpilih['paket']})"

            pilates_shain[id_member] = {
                "nama": nama,
                "paket": paket,
                "durasi": durasi,
                "jadwal": jadwal_str
            }

            print("๑ ⋆₊⋆─ʚ DATA BERHASIL DITAMBAHKAN ɞ─⋆₊⋆ ๑")

        except Exception as e:
            print("TERJADI KESALAHAN:", e)

    elif pilih == "2":
        if not pilates_shain:
            print("BELUM ADA DATA MEMBER (╥﹏╥)")
        else:
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
                table.field_names = ["ID", "Nama", "Paket", "Durasi", "Biaya", "Jadwal"]
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
        id_m = input("MASUKKAN ID MEMBER: ")
        if id_m not in pilates_shain:
            print("DATA TIDAK DITEMUKAN!")
        else:
            nama_baru = input("NAMA BARU: ")
            paket_baru = input("PAKET BARU (BASIC/FOAM/LEGS/FULL/RINGAN): ").upper()
            if paket_baru not in opsi_paket:
                print("PAKET TIDAK VALID!")
                return menu_admin(pilates_shain)
            durasi_baru = input("DURASI BARU (bulan): ")
            if not durasi_baru.isdigit():
                print("DURASI WAJIB ANGKA!")
                return menu_admin(pilates_shain)

            jadwal_paket = [j for j in JADWAL_PILATES if j["paket"] == paket_baru]
            if not jadwal_paket:
                print(f"Tidak ada jadwal untuk paket {paket_baru}.")
                return menu_admin(pilates_shain)

            print(f"\nJadwal tersedia untuk paket {paket_baru}:")
            for i, j in enumerate(jadwal_paket, 1):
                print(f"{i}. {j['hari']}, {j['waktu']}")

            pilih_jadwal = input(f"Pilih nomor jadwal (1-{len(jadwal_paket)}): ")
            if not (pilih_jadwal.isdigit() and 1 <= int(pilih_jadwal) <= len(jadwal_paket)):
                print("Pilihan jadwal tidak valid!")
                return menu_admin(pilates_shain)

            j_terpilih = jadwal_paket[int(pilih_jadwal) - 1]
            jadwal_baru = f"{j_terpilih['hari']}, {j_terpilih['waktu']} ({j_terpilih['paket']})"

            pilates_shain[id_m] = {
                "nama": nama_baru,
                "paket": paket_baru,
                "durasi": durasi_baru,
                "jadwal": jadwal_baru
            }
            print("ꔫ DATA BERHASIL DIUBAH ꔫ")

    elif pilih == "4":
        id_m = input("MASUKKAN ID MEMBER YANG INGIN DIHAPUS: ")
        if id_m in pilates_shain:
            del pilates_shain[id_m]
            print("ꔫ DATA BERHASIL DIHAPUS ꔫ")
        else:
            print("DATA TIDAK DITEMUKAN!")

    elif pilih == "5":
        print("LOGOUT BERHASIL ⭢ KEMBALI KE MENU UTAMA")
        return

    else:
        print("PILIHAN TIDAK VALID!")

    input("\nTekan ENTER untuk kembali...")
    return menu_admin(pilates_shain)