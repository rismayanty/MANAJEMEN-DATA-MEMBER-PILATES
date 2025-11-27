import os
import re

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def validasi_nama(nama):
    if not nama or nama.strip() != nama:
        return False
    if not re.match(r'^[A-Za-z]+(?: [A-Za-z]+)*$', nama):
        return False
    if nama.endswith('.'):
        return False
    return True

def registrasi(users):
    clear()
    print("=== ✮ REGISTRASI AKUN ✮ ===")

    try:
        nama = input("MASUKKAN NAMA: ")
        if not validasi_nama(nama):
            print("⚠ NAMA TIDAK VALID! Hanya huruf, tanpa titik di akhir, tanpa spasi berlebih.")
            return
        
        if any(data["nama"] == nama for data in users.values()):
             print("⚠ NAMA SUDAH TERDAFTAR! Silakan gunakan menu LOGIN.")
             return


        usia_input = input("MASUKKAN USIA (12-40 TAHUN): ")
        if not usia_input.isdigit():
            print("⚠ USIA HARUS ANGKA!")
            return

        usia = int(usia_input)
        if usia < 12 or usia > 40:
            print("⚠ USIA HARUS ANTARA 12 SAMPAI 40 TAHUN!")
            return
            return

        role = input("MASUKKAN ROLE (admin/member): ").lower()
        if role not in ["admin", "member"]:
            print("⚠ ROLE TIDAK VALID! Pilih: admin atau member")
            return

        if role == "admin":
            admin_ids = []
            for uid, data in users.items():
                if uid.isdigit() and data.get("role") == "admin":
                    admin_ids.append(int(uid))
            next_id = max(admin_ids, default=1000) + 1
            id_user = str(next_id)

        else:
            member_ids = []
            for uid, data in users.items():
                if uid.isdigit() and data.get("role") == "member":
                    member_ids.append(int(uid))
            next_id = max(member_ids, default=0) + 1
            if next_id > 9999:
                print("❌ KAPASITAS MEMBER PENUH (maks 9999 member)!")
                return
            id_user = f"{next_id:04d}"

        if id_user in users:
            print("❌ ID SUDAH DIGUNAKAN! Silakan coba lagi.")
            return

        users[id_user] = {
            "nama": nama,
            "usia": usia,
            "role": role
        }

        print(f"🎯 REGISTRASI BERHASIL!")
        print(f"🆔 ID    : {id_user}")
        print(f"👤 NAMA  : {nama}")
        print(f"🎂 USIA  : {usia}")
        print(f"🏷️ ROLE  : {role}")

    except Exception as e:
        print(f"❌ TERJADI KESALAHAN: {e}")

def login(users, maks_percobaan=3):
    clear()
    for percobaan in range(1, maks_percobaan + 1):
        print("\n🟦 LOGIN USER 🟦")
        try:
            id_in = input("MASUKKAN ID: ").strip()
            nama_in = input("MASUKKAN NAMA: ").strip()

            if not (id_in.isdigit() and len(id_in) == 4):
                print("⚠ FORMAT ID HARUS 4 DIGIT ANGKA! Contoh: 0001 atau 1001")
                continue

            if id_in in users and nama_in == users[id_in]["nama"]:
                print("✨ LOGIN BERHASIL!")
                return id_in, users[id_in]
            else:
                print(f"❌ LOGIN GAGAL ({percobaan}/{maks_percobaan})")

        except Exception as e:
            print(f"⚠ ERROR LOGIN: {e}")

    print("\n⛔ GAGAL LOGIN 3 KALI!")
    return None