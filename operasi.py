from prettytable import PrettyTable

studio_name = "PILATES SHAIN"
opsi_paket = ["BASIC", "FOAM", "LEGS", "FULL", "RINGAN"]

def welcome():
    print("\n" + "="*60)
    print(f"🎀 SELAMAT DATANG DI STUDIO {studio_name} 🎀".center(60))
    print("="*60)

def menu_utama():
    print("\n╭════•✧ MENU UTAMA STUDIO PILATES SHAIN ✧•════╮".center(60))
    print("\n1. REGISTRASI\n2. LOGIN\n3. KELUAR")
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
        table.field_names = ["ID", "Nama", "Paket", "Durasi (bulan)", "Biaya (Rp)", "Jadwal"]

        biaya = biaya_pilates(data['paket'], data['durasi'])

        table.add_row([
            member_id, 
            data['nama'], 
            data['paket'], 
            data['durasi'], 
            biaya,
            data.get("jadwal", "Belum ditentukan")
        ])

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
    jadwal = data.get("jadwal", "Belum ditentukan")

    table = PrettyTable()
    table.field_names = ["JADWAL KELAS PILATES"]
    table.add_row([jadwal])
    table.align = "c"

    print("\n📅 JADWAL MEMBER:")
    print(table)