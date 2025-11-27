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