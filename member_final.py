from prettytable import PrettyTable
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_member(pilates_shain, current_user, current_user_id, jadwal):
    while True:
        clear()
        print("\n╭════•✧ MENU MEMBER ✧•════╮")
        print("1. LIHAT DATA SAYA")
        print("2. LIHAT JADWAL TERSEDIA")
        print("3. PILIH JADWAL")
        print("4. LOGOUT")
        pilih = input("PILIH MENU: ").strip()

        if pilih == "1":
            print(f"\nID USER: {current_user_id}")
            print(f"NAMA: {current_user['nama']}")
            print(f"USIA: {current_user['usia']}")
            mdata = pilates_shain.get(current_user_id)
            if mdata:
                from operasi_final import biaya_pilates
                biaya = biaya_pilates(mdata.get("paket",""), mdata.get("durasi","0"))
                print(f"Paket: {mdata.get('paket')}")
                print(f"Durasi: {mdata.get('durasi')} bulan")
                print(f"Tagihan: Rp {biaya}")
                print(f"Jadwal: {mdata.get('jadwal','Belum memilih')}")
            else:
                print("Anda belum terdaftar sebagai member di sistem pilates.")

            input("ENTER...")

        elif pilih == "2":
            from operasi_final import tampilkan_jadwal_list
            tampilkan_jadwal_list(jadwal, pilates_shain)
            input("ENTER...")

        elif pilih == "3":
            if not jadwal:
                print("Belum ada jadwal, hubungi admin.")
                input("ENTER...")
                continue

            from operasi_final import tampilkan_jadwal_list
            tampilkan_jadwal_list(jadwal, pilates_shain)
            try:
                nomor = int(input("PILIH NOMOR JADWAL: ").strip()) - 1
                if 0 <= nomor < len(jadwal):
                    pilih_j = jadwal[nomor]
                    # simpan ke pilates_shain; jika belum ada entry, buat
                    if current_user_id not in pilates_shain:
                        # minta paket & durasi dulu
                        paket = input("PAKET (BASIC/FOAM/LEGS/FULL/RINGAN): ").upper().strip()
                        durasi = input("DURASI (bulan): ").strip()
                        if not durasi.isdigit():
                            print("Durasi harus angka. Batal.")
                            input("ENTER...")
                            continue
                        pilates_shain[current_user_id] = {
                            "nama": current_user["nama"],
                            "paket": paket,
                            "durasi": durasi,
                            "jadwal": pilih_j
                        }
                    else:
                        pilates_shain[current_user_id]["jadwal"] = pilih_j
                    print(f"Anda berhasil memilih jadwal: {pilih_j}")
                else:
                    print("Nomor tidak valid.")
            except:
                print("Input harus angka.")
            input("ENTER...")

        elif pilih == "4":
            print("LOGOUT BERHASIL")
            return

        else:
            print("PILIHAN TIDAK VALID!")
            input("ENTER...")