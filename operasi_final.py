from prettytable import PrettyTable
from colorama import Fore, Style

studio_name = "PILATES SHAIN"
opsi_paket = ["BASIC", "FOAM", "LEGS", "FULL", "RINGAN"]

JADWAL_PILATES = [
    {"hari": "Senin",    "waktu": "17.00-18.00", "paket": "RINGAN", "harga": 100000},
    {"hari": "Selasa",   "waktu": "17.00-18.00", "paket": "BASIC", "harga": 150000},
    {"hari": "Rabu",     "waktu": "17.00-18.00", "paket": "FOAM", "harga": 200000},
    {"hari": "Kamis",    "waktu": "19.00-20.00", "paket": "LEGS", "harga": 250000},
    {"hari": "Jumat",    "waktu": "17.00-18.00", "paket": "FULL", "harga": 500000},
    {"hari": "Sabtu",    "waktu": "08.00-09.00", "paket": "BASIC", "harga": 150000},
    {"hari": "Minggu",   "waktu": "08.00-09.00", "paket": "RINGAN", "harga": 100000}
]

def welcome():
    print("\n" + "="*60)
    print(f"🎀 SELAMAT DATANG DI STUDIO {studio_name} 🎀".center(60))
    print("="*60)

def menu_utama():
    print("\n╭════•✧ MENU UTAMA STUDIO PILATES SHAIN ✧•════╮".center(60))
    print("\n1. REGISTRASI\n2. LOGIN\n3. MENU ENQUIRED\n4. KELUAR")
    print("="*60)
    return input("PILIH MENU: ")

def biaya_pilates(paket, durasi):
    list_harga = {"BASIC": 150000, "FOAM": 200000, "LEGS": 250000, "FULL": 500000, "RINGAN": 100000}
    try:
        return list_harga.get(paket.upper(), 0) * int(durasi)
    except ValueError:
        return False

def data_member(pilates_shain, member_id):
    if member_id in pilates_shain:
        data = pilates_shain[member_id]
        table = PrettyTable()
        table.field_names = ["ID", "NAMA", "PAKET", "DURASI (BULAN)", "BIAYA (Rp)", "JADWAL"]
        biaya = biaya_pilates(data['paket'], data['durasi'])
        table.add_row([member_id, data['nama'], data['paket'], data['durasi'], biaya, data.get("jadwal", "belum ditentukan")])
        print(table)
    else:
        print("(╥﹏╥) DATA TIDAK DITEMUKAN")

def hitung_member(data, index=0, keys=None):
    if keys is None:
        keys = list(data.keys())
    if index == len(keys):
        return 0
    return 1 + hitung_member(data, index + 1, keys)

def tampilkan_jadwal(pilates_shain, member_id):
    if member_id not in pilates_shain:
        print("(╥﹏╥) MEMBER TIDAK DITEMUKAN")
        return
    data = pilates_shain[member_id]
    jadwal = data.get("jadwal", "belum ditentukan")
    table = PrettyTable()
    table.field_names = ["JADWAL KELAS PILATES"]
    table.add_row([jadwal])
    table.align = "c"
    print("\n📅 JADWAL MEMBER:")
    print(table)

def required_menu():
    print("\n=== MENU REQUIRED ===")
    print("1. PAKET TERSEDIA")
    print("2. CARA MENDAFTAR MEMBER")
    print("3. LIHAT JADWAL KELAS")
    print("4. FASILITAS STUDIO")
    print("5. KELUAR")
    pilihan = input("PILIH: ").strip()
    if pilihan == "1":
        print("\nPAKET TERSEDIA: BASIC, FOAM, LEGS, FULL, RINGAN")
    elif pilihan == "2":
        print("\nCARA DAFTAR: Pilih MENU REGISTRASI PADA MENU UTAMA, ISI DATA.")
    elif pilihan == "3":
        print("\nSILAHKAN GUNAKAN MENU LOGIN -> MEMBER -> LIHAT JADWAL")
    elif pilihan == "4":
        print("\nFASILITAS: MATRAS, FOAM ROLLER, RING, COACH.")
    else:
        return

def tampilkan_jadwal_list(jadwal, pilates_shain=None):
    if not jadwal:
        print("BELUM ADA JADWAL TERDAFTAR.")
        return
    table = PrettyTable()
    table.field_names = ["NO", "JADWAL", "TERISI"]
    for i, j in enumerate(jadwal, start=1):
        terisi = sum(1 for m in pilates_shain.values() if m.get("jadwal") == j) if pilates_shain else 0
        table.add_row([i, j, terisi])
    print(table)

def tampilkan_jadwal_pretty(jadwal_list):
    if not jadwal_list:
        print(Fore.RED + "❌ Tidak ada jadwal tersedia." + Style.RESET_ALL)
        return
    table = PrettyTable()
    table.field_names = ["No", "Hari", "Waktu", "Paket", "Harga"]
    table.align = "l"
    table.border = False
    table.header = False

    warna_paket = {
        "RINGAN": Fore.GREEN,
        "BASIC": Fore.BLUE,
        "FOAM": Fore.MAGENTA,
        "LEGS": Fore.RED,
        "FULL": Fore.WHITE + Style.BRIGHT
    }

    for i, j in enumerate(jadwal_list, 1):
        paket = j["paket"]
        warna = warna_paket.get(paket, Fore.WHITE)
        harga_str = f"Rp {j['harga']:,}".replace(",", ".")
        paket_warna = warna + paket + Style.RESET_ALL
        harga_warna = Fore.GREEN + harga_str + Style.RESET_ALL
        table.add_row([i, j["hari"], j["waktu"], paket_warna, harga_warna])

    border_top = Fore.CYAN + "┌" + "─" * 58 + "┐" + Style.RESET_ALL
    border_bottom = Fore.CYAN + "└" + "─" * 58 + "┘" + Style.RESET_ALL
    title = Fore.CYAN + Style.BRIGHT + "🧘‍♀️ JADWAL PILATES SHAIN 🧘‍♀️".center(60)
    header_line = Fore.CYAN + "├" + "─" * 58 + "┤" + Style.RESET_ALL
    header_cols = (
        Fore.CYAN + "│ " +
        Fore.YELLOW + "No".ljust(2) + " " +
        Fore.YELLOW + "Hari".ljust(8) + " " +
        Fore.YELLOW + "Waktu".ljust(12) + " " +
        Fore.YELLOW + "Paket".ljust(7) + " " +
        Fore.YELLOW + "Harga".ljust(12) +
        Fore.CYAN + " │" + Style.RESET_ALL
    )

    print("\n" + border_top)
    print(title)
    print(header_line)
    print(header_cols)
    print(header_line)

    for row in str(table).splitlines():
        print(Fore.CYAN + "│ " + Style.RESET_ALL + row.ljust(56) + Fore.CYAN + " │" + Style.RESET_ALL)

    print(border_bottom)