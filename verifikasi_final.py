import os
import re

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

 feat/verifikasi_final
def validasi_nama(nama):
    if not nama or nama.strip() != nama:
        return False

# Validasi ID: harus A### untuk admin atau M### untuk member (contoh A001, M001)
def validasi_id(id_user):
    return bool(re.match(r'^[AM]\d{3}$', id_user))

# Validasi nama: hanya huruf dan single space antar kata, tidak diawali/diakhiri spasi, tidak ada titik di akhir
def validasi_nama(nama):
    if not nama or nama.strip() != nama:
        return False
    # hanya huruf dan spasi tunggal antar kata
 main
    if not re.match(r'^[A-Za-z]+(?: [A-Za-z]+)*$', nama):
        return False
    if nama.endswith('.'):
        return False
    return True

 feat/verifikasi_final
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

# Generate ID otomatis berdasarkan role: A001.. untuk admin, M001.. untuk member
def generate_id(users, role):
    prefix = 'A' if role == 'admin' else 'M'
    max_num = 0
    for uid in users.keys():
        if uid.startswith(prefix):
            try:
                n = int(uid[1:])
                if n > max_num:
                    max_num = n
            except:
                continue
    return f"{prefix}{max_num+1:03d}"

def registrasi(users):
    clear()
    print("=== ✮ REGISTRASI AKUN ✮ ===")
    try:
        nama = input("MASUKKAN NAMA: ").strip()
        if not validasi_nama(nama):
            print("NAMA TIDAK VALID. Hanya huruf dan spasi tunggal, tidak boleh titik di akhir.")
            return

        usia = input("MASUKKAN USIA (12–40): ").strip()
        if not usia.isdigit() or not (12 <= int(usia) <= 40):
            print("USIA TIDAK VALID. Harus angka 12–40.")
            return

        role = input("MASUKKAN ROLE (admin/member): ").strip().lower()
        if role not in ["admin", "member"]:
            print("ROLE TIDAK VALID.")
            return

        id_user = generate_id(users, role)
        users[id_user] = {
            "nama": nama,
            "usia": int(usia),
            "role": role
        }

        print(f"☆ REGISTRASI BERHASIL! ID ANDA: {id_user}")

    except Exception as e:
        print("TERJADI KESALAHAN SAAT REGISTRASI:", e)

def login(users, maks_percobaan):
    clear()
    try:
        for percobaan in range(1, maks_percobaan + 1):
            print("\n=== LOGIN USER ===")
            id_in = input("MASUKKAN ID: ").strip().upper()
            nama_in = input("MASUKKAN NAMA: ").strip()

            # validasi format ID
            if not validasi_id(id_in):
                print("FORMAT ID SALAH. Gunakan A001 (admin) atau M001 (member).")
                continue

            if id_in in users and nama_in == users[id_in]["nama"]:
                print("LOGIN BERHASIL!")
                input("Tekan ENTER untuk lanjut...")
                clear()
                return id_in, users[id_in]
            else:
                print(f"LOGIN GAGAL ({percobaan}/{maks_percobaan})")
                if percobaan < maks_percobaan:
                    input("Tekan ENTER untuk coba lagi...")
                    clear()

        print("\nANDA GAGAL LOGIN 3 KALI!")
        return None

    except Exception as e:
        print("TERJADI KESALAHAN SAAT LOGIN:", e)
        return None
 main
