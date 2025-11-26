import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_id(users):
    """Menghasilkan ID baru otomatis 4 digit"""
    if not users:
        return "0001"  

    angka_terbesar = max(int(uid) for uid in users.keys())
    id_baru = angka_terbesar + 1
    return str(id_baru).zfill(4) 


def registrasi(users):
    clear()
    print("=== ✮ REGISTRASI AKUN ✮ ===")

    try:
        nama = input("MASUKKAN NAMA: ")
        usia = input("MASUKKAN USIA (12–40): ")
        role = input("MASUKKAN ROLE (admin/member): ")

        if not usia.isdigit() or not (12 <= int(usia) <= 40):
            print("⚠ USIA HARUS ANGKA DAN 12–40 TAHUN!")
            return

        if role.lower() not in ["admin", "member"]:
            print("⚠ ROLE TIDAK VALID!")
            return

        id_user = generate_id(users)

        users[id_user] = {
            "nama": nama,
            "usia": int(usia),
            "role": role.lower()
        }

        print(f"☆ REGISTRASI BERHASIL! ID ANDA: {id_user}")

    except Exception as e:
        print(f"⚠ TERJADI KESALAHAN: {e}")

def login(users, maks_percobaan):
    clear()
    for percobaan in range(1, maks_percobaan + 1):
        print("\n🟦 LOGIN USER 🟦")

        try:
            id_in = input("MASUKKAN ID: ")
            nama_in = input("MASUKKAN NAMA: ")

            if not (id_in.isdigit() and len(id_in) == 4):
                print("⚠ FORMAT ID HARUS 4 DIGIT ANGKA!")
                continue

            if id_in in users and nama_in == users[id_in]["nama"]:
                print("✨ LOGIN BERHASIL!")
                return id_in, users[id_in]

            else:
                print(f"❌ LOGIN GAGAL ({percobaan}/{maks_percobaan})")

        except Exception as e:
            print(f"⚠ TERJADI KESALAHAN SAAT LOGIN: {e}")

    print("\n❌ ANDA GAGAL LOGIN 3 KALI!")
    return None
