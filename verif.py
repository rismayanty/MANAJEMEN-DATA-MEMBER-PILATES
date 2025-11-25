import os

def clear(users):
    clear ()
    maks_percobaan = 3

    try:
        for i in range(maks_percobaan):
            print("\n𝜗ৎ LOGIN USER 𝜗ৎ")
            id_in = input("MASUKKAN ID: ").upper()
            nama_in = input("MASUKKAN NAMA: ")

            if id_in in users and nama_in == users[id_in]["nama"]:
                print("☆ LOGIN BERHASIL! ☆")
                input("tekan ENTER untuk next...")
                clear()
                return id_in, users[id_in]

            else:
                print(f"LOGIN GAGAL ({i+1}/3)")
                if i < maks_percobaan - 1:
                    input("tekan ENTER untuk next...")
                    clear()

        print("ANDA TELAH GAGAL LOGIN 3 KALI.")
        input("tekan ENTER untuk next...")
        clear()
        return None

    except Exception as e:
        print("❌ TERJADI KESALAHAN:", e)
        input("tekan ENTER untuk next...")
        clear()
        return None