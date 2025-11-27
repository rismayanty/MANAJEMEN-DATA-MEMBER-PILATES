import os
from colorama import init, Fore, Style
from operasi_final import biaya_pilates, opsi_paket, tampilkan_jadwal_pretty, JADWAL_PILATES

init(autoreset=True)

def tampilkan_jadwal_tersedia():
    tampilkan_jadwal_pretty(JADWAL_PILATES)

def menu_member(pilates_shain, current_user, current_user_id):
    print("\n╭════•✧ MENU MEMBER ✧•════╮")
    print("1. LIHAT DATA SAYA")
    print("2. DAFTAR SEBAGAI MEMBER")
    print("3. LIHAT JADWAL KELAS")
    print("4. LOGOUT")
    print("=" * 60)

    pilih = input("PILIH MENU: ").strip()

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
            print(f"Tagihan : Rp {biaya:,}".replace(",", "."))

            jadwal_str = data.get("jadwal", "Belum dipilih")
            warna_paket = {
                "RINGAN": Fore.GREEN,
                "BASIC": Fore.BLUE,
                "FOAM": Fore.MAGENTA,
                "LEGS": Fore.RED,
                "FULL": Fore.WHITE
            }
            warna = warna_paket.get(data['paket'], Fore.WHITE)
            jadwal_berwarna = warna + jadwal_str + Style.RESET_ALL

            print("\n" + Fore.MAGENTA + "✨ Jadwal Pilates Anda ✨")
            print(Fore.CYAN + "╭──────────────────────────────────────╮")
            print(f"│ {Fore.YELLOW}🧘‍♀️ {jadwal_berwarna:^36} {Fore.CYAN}│")
            print(Fore.CYAN + "╰──────────────────────────────────────╯")
        else:
            print("ANDA BELUM TERDAFTAR SEBAGAI MEMBER.")

    elif pilih == "2":
        if current_user_id in pilates_shain:
            print("ANDA SUDAH TERDAFTAR!")
        else:
            try:
                paket = input("PAKET PILATES (BASIC/FOAM/LEGS/FULL/RINGAN): ").upper()
                if paket not in opsi_paket:
                    print("⚠ PAKET TIDAK VALID!")
                else:
                    durasi = input("DURASI MEMBERSHIP (bulan): ")
                    if not durasi.isdigit() or int(durasi) <= 0:
                        print("⚠ DURASI HARUS ANGKA POSITIF!")
                    else:
                        jadwal_paket = [j for j in JADWAL_PILATES if j["paket"] == paket]
                        if not jadwal_paket:
                            print("Tidak ada jadwal untuk paket ini.")
                        else:
                            print(f"\n🗓️ JADWAL TERSEDIA UNTUK PAKET {paket}:")
                            for i, j in enumerate(jadwal_paket, 1):
                                print(f"{i}. {j['hari']}, {j['waktu']}")

                            pilih_jadwal = input(f"\nPilih nomor jadwal (1-{len(jadwal_paket)}): ")
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

                                warna_paket_map = {
                                    "RINGAN": Fore.GREEN,
                                    "BASIC": Fore.BLUE,
                                    "FOAM": Fore.MAGENTA,
                                    "LEGS": Fore.RED,
                                    "FULL": Fore.WHITE
                                }
                                warna = warna_paket_map.get(paket, Fore.WHITE)
                                jadwal_berwarna = warna + jadwal_str + Style.RESET_ALL

                                print("\n" + Fore.MAGENTA + "✨ Jadwal Pilates Anda ✨")
                                print(Fore.CYAN + "╭──────────────────────────────────────╮")
                                print(f"│ {Fore.YELLOW}🧘‍♀️ {jadwal_berwarna:^36} {Fore.CYAN}│")
                                print(Fore.CYAN + "╰──────────────────────────────────────╯")
                            else:
                                print("❌ Pilihan jadwal tidak valid!")
            except Exception as e:
                print(f"⚠ TERJADI KESALAHAN: {e}")

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