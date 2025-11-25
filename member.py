from prettytable import PrettyTable
from operasi import data_member, opsi_paket, biaya_pilates
import os

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

            table = PrettyTable()
            table.field_names = ["JADWAL KELAS PILATES"]
            table.add_row([data.get("jadwal", "Belum Diatur Admin")])
            table.align = "c"

            print("\n📅 JADWAL ANDA:")
            print(table)

        else:
            print("ANDA BELUM TERDAFTAR SEBAGAI MEMBER.")

    elif pilih == "2":
        if current_user_id in pilates_shain:
            print("ANDA SUDAH TERDAFTAR!")
            input("Tekan ENTER untuk lanjut...")
            os.system('cls' if os.name == 'nt' else 'clear')

        else:
            try:
                paket = input("PAKET PILATES (BASIC/FOAM/LEGS/FULL/RINGAN): ").upper()
                durasi = input("DURASI MEMBERSHIP (bulan): ")

                if paket in opsi_paket and durasi.isdigit():

                    pilates_shain[current_user_id] = {
                        "nama": current_user["nama"],
                        "paket": paket,
                        "durasi": durasi,
                        "jadwal": "Belum ditentukan admin"
                    }

                    print("☆ PENDAFTARAN MEMBER BERHASIL! ☆")

                else:
                    print("DATA TIDAK VALID!")

            except Exception as e:
                print("TERJADI KESALAHAN INPUT:", e)

    elif pilih == "3":
        if current_user_id not in pilates_shain:
            print("ANDA BELUM MENJADI MEMBER!")
        else:
            data = pilates_shain[current_user_id]
            table = PrettyTable()
            table.field_names = ["JADWAL KELAS PILATES"]
            table.add_row([data.get("jadwal", "Belum ditentukan admin")])
            table.align = "c"

            print("\n📅 JADWAL KELAS ANDA:")
            print(table)

    elif pilih == "4":
        print("☆ LOGOUT BERHASIL! ☆")
        return

    else:
        print("PILIHAN TIDAK VALID!")

    return menu_member(pilates_shain, current_user, current_user_id)