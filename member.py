from prettytable import PrettyTable
from operasi import data_member, opsi_paket, biaya_pilates
import os
from colorama import init, Fore, Style

init(autoreset=True)

JADWAL_PILATES = [
    {"hari": "Senin",    "waktu": "17.00-18.00", "paket": "RINGAN", "harga": 100000},
    {"hari": "Selasa",   "waktu": "17.00-18.00", "paket": "BASIC", "harga": 150000},
    {"hari": "Rabu",     "waktu": "17.00-18.00", "paket": "FOAM", "harga": 200000},
    {"hari": "Kamis",    "waktu": "19.00-20.00", "paket": "LEGS", "harga": 250000},
    {"hari": "Jumat",    "waktu": "17.00-18.00", "paket": "FULL", "harga": 500000},
    {"hari": "Sabtu",    "waktu": "08.00-09.00", "paket": "BASIC", "harga": 150000},
    {"hari": "Minggu",   "waktu": "08.00-09.00", "paket": "RINGAN", "harga": 100000}
]

def tampilkan_jadwal_tersedia():
    print(Fore.CYAN + Style.BRIGHT + "\n" + "═" * 50)
    print(Fore.YELLOW + Style.BRIGHT + "        🗓️  JADWAL PILATES TERSEDIA 🗓️")
    print(Fore.CYAN + "═" * 50)

    table = PrettyTable()
    table.field_names = ["No", "Hari", "Waktu", "Paket", "Harga"]
    table.align = "c"

    warna_paket = {
        "RINGAN": Fore.GREEN,
        "BASIC": Fore.BLUE,
        "FOAM": Fore.MAGENTA,
        "LEGS": Fore.RED,
        "FULL": Fore.WHITE
    }

    for i, jadwal in enumerate(JADWAL_PILATES, 1):
        paket = jadwal["paket"]
        warna = warna_paket.get(paket, Fore.WHITE)
        harga_str = f"Rp {jadwal['harga']:,}".replace(",", ".")

        paket_berwarna = warna + paket + Style.RESET_ALL
        no_berwarna = Fore.YELLOW + str(i) + Style.RESET_ALL
        hari_berwarna = Fore.CYAN + jadwal["hari"] + Style.RESET_ALL
        waktu_berwarna = Fore.MAGENTA + jadwal["waktu"] + Style.RESET_ALL
        harga_berwarna = Fore.GREEN + harga_str + Style.RESET_ALL

        table.add_row([no_berwarna, hari_berwarna, waktu_berwarna, paket_berwarna, harga_berwarna])

    print(table)
    print(Fore.CYAN + "═" * 50 + "\n")

def menu_member(pilates_shain, current_user, current_user_id):
    print("\n╭════•✧ MENU MEMBER ✧•════╮")
    print("1. LIHAT DATA SAYA")
    print("2. DAFTAR SEBAGAI MEMBER")
    print("3. LIHAT JADWAL KELAS")
    print("4. LOGOUT")
    print("="*60)

    pilih = input("PILIH MENU: ")

    if pilih == "1":
        print(f"\nID USER : {current_user_id}")
        print(f"NAMA    : {current_user['nama']}")
        print(f"USIA    : {current_user['usia']}")

        if current_user_id in pilates_shain:
            data = pilates_shain[current_user_id]
            biaya = biaya_pilates(data["paket"], data["durasi"])

            print("\n☆ DATA MEMBER ANDA ☆")
            print(f"Paket   : {data['paket']}")
            print(f"Durasi  : {data['durasi']} bulan")
            print(f"Tagihan : Rp {biaya}")

            jadwal_str = data.get("jadwal", "Belum dipilih")
            paket_dipilih = data['paket']
            warna_paket = {
                "RINGAN": Fore.GREEN,
                "BASIC": Fore.BLUE,
                "FOAM": Fore.MAGENTA,
                "LEGS": Fore.RED,
                "FULL": Fore.WHITE
            }
            warna = warna_paket.get(paket_dipilih, Fore.WHITE)
            jadwal_berwarna = warna + jadwal_str + Style.RESET_ALL

            table = PrettyTable()
            table.field_names = ["JADWAL KELAS PILATES"]
            table.add_row([jadwal_berwarna])
            table.align = "c"

            print("\n📅 JADWAL ANDA:")
            print(table)
        else:
            print("ANDA BELUM TERDAFTAR SEBAGAI MEMBER.")

    elif pilih == "2":
        if current_user_id in pilates_shain:
            print("☆ ANDA SUDAH TERDAFTAR! ☆")
        else:
            try:
                paket = input("PAKET PILATES (BASIC/FOAM/LEGS/FULL/RINGAN): ").upper()
                durasi = input("DURASI MEMBERSHIP (bulan): ")

                if paket in opsi_paket and durasi.isdigit():
                    jadwal_paket = [j for j in JADWAL_PILATES if j["paket"] == paket]
                    
                    if not jadwal_paket:
                        print("Tidak ada jadwal untuk paket tersebut.")
                    else:
                        print(f"\nJadwal tersedia untuk paket {paket}:")
                        for i, j in enumerate(jadwal_paket, 1):
                            print(f"{i}. {j['hari']}, {j['waktu']}")

                        pilih_jadwal = input(f"Pilih nomor jadwal (1-{len(jadwal_paket)}): ")
                        if pilih_jadwal.isdigit() and 1 <= int(pilih_jadwal) <= len(jadwal_paket):
                            j_terpilih = jadwal_paket[int(pilih_jadwal) - 1]
                            jadwal_str = f"{j_terpilih['hari']}, {j_terpilih['waktu']} ({j_terpilih['paket']})"
                            
                            pilates_shain[current_user_id] = {
                                "nama": current_user["nama"],
                                "paket": paket,
                                "durasi": int(durasi),
                                "jadwal": jadwal_str
                            }

                            print("\n☆ PENDAFTARAN BERHASIL! ☆")
                            print(f"Jadwal Anda: {jadwal_str}")

                            warna_paket = {
                                "RINGAN": Fore.GREEN,
                                "BASIC": Fore.BLUE,
                                "FOAM": Fore.MAGENTA,
                                "LEGS": Fore.RED,
                                "FULL": Fore.WHITE
                            }
                            warna = warna_paket.get(paket, Fore.WHITE)
                            jadwal_berwarna = warna + jadwal_str + Style.RESET_ALL

                            table = PrettyTable()
                            table.field_names = ["JADWAL KELAS PILATES"]
                            table.add_row([jadwal_berwarna])
                            table.align = "c"
                            print("\n📅 JADWAL ANDA:")
                            print(table)

                        else:
                            print("Pilihan jadwal tidak valid.")
                else:
                    print("DATA TIDAK VALID!")
            except Exception as e:
                print("TERJADI KESALAHAN INPUT:", e)

    elif pilih == "3":
        tampilkan_jadwal_tersedia()

    elif pilih == "4":
        print("☆ LOGOUT BERHASIL! ☆")
        return

    else:
        print("PILIHAN TIDAK VALID!")

    input("\nTekan ENTER untuk lanjut...")
    os.system('cls' if os.name == 'nt' else 'clear')
    return menu_member(pilates_shain, current_user, current_user_id)