from prettytable import PrettyTable

def menu_utama():
    print("\n╭════•✧ MENU UTAMA STUDIO PILATES SHAIN ✧•════╮".center(60))
    print("\n1. REGISTRASI\n2. LOGIN\n3. ENQUIRY\n4. KELUAR")
    print("="*60)
    return input("PILIH MENU: ").strip()

def enquiry_menu():
    print("\n=== MENU ENQUIRY ===")
    print("1. Daftar Paket")
    print("2. Cara Daftar Member")
    print("3. Lihat Jadwal Studio")
    print("4. Fasilitas Studio")
    print("5. Kembali")
    pilihan = input("PILIH: ").strip()
    if pilihan == "1":
        print("\nPaket tersedia: BASIC, FOAM, LEGS, FULL, RINGAN")
    elif pilihan == "2":
        print("\nCara daftar: Pilih menu REGISTRASI pada menu utama, isi data.")
    elif pilihan == "3":
        print("\nSilahkan gunakan menu LOGIN -> MEMBER -> Lihat Jadwal")
    elif pilihan == "4":
        print("\nFasilitas: Matras, Foam Roller, Ring, Instruktur bersertifikat.")
    else:
        return

def tampilkan_jadwal_list(jadwal, pilates_shain=None):
    """
    jadwal: list of strings e.g. "Senin - 10:00"
    pilates_shain (optional) untuk menghitung occupancy
    """
    if not jadwal:
        print("Belum ada jadwal terdaftar.")
        return

    table = PrettyTable()
    table.field_names = ["No", "Jadwal", "Terisi"]
    for i, j in enumerate(jadwal, start=1):
        terisi = 0
        if pilates_shain:
            for m in pilates_shain.values():
                if m.get("jadwal") == j:
                    terisi += 1
        table.add_row([i, j, terisi])
    print(table)

    