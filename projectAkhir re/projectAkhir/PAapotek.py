# Modul
import os  # untuk mengakses sistem operasi yang mendasari aplikasi Python kita
from prettytable import (
    PrettyTable,
)  # Modul fitur untuk membuat tabel yang terlihat indah dan teratur dalam teks.
import pwinput  # Modul ini digunakan untuk menyembunyikan input pengguna saat mengetik password.
import json  # Modul ini digunakan untuk mengkonversi data antara format JSON dan data bawaan Python.
import datetime  # Modul ini menyediakan fungsi dan kelas untuk mengolah tanggal dan waktu dalam Python.

# Modul Membersihkan Terminal
os.system("cls")
# merupakan perintah dalam bahasa pemrograman Python yang digunakan untuk mengatur direktori root aplikasi.
ROOD_DIR = os.path.abspath(os.curdir)

# ini adalah prettytable untuk read produk obat
produkjson = f"{ROOD_DIR}/projectAkhir/crudpa.json"
try:
    with open(produkjson, "r") as jsonproduk:
        data_produk = json.loads(jsonproduk.read())
except FileNotFoundError:
    print("File tidak ditemukan.")
    data_produk = []
except Exception as e:
    print(f"Terjadi kesalahan: {e}")
except KeyboardInterrupt:
    print("\nMasukkan inputan dengan benar")

# ini adalah prettytable untuk read admin
tabelAdmin = PrettyTable()
tabelAdmin.field_names = ["nama admin", "password admin"]
adminjson = f"{ROOD_DIR}/projectAkhir/paloginadmin.json"
try:
    with open(adminjson, "r") as jsonadmin:
        data_admin = json.loads(jsonadmin.read())

    for i in data_admin:
        tabelAdmin.add_row([i["username"], i["password"]])
except FileNotFoundError:
    print(f"File not found: {adminjson}")
except KeyError:
    print("Invalid key in the JSON file.")
except json.JSONDecodeError:
    print("Invalid JSON file.")
except Exception as e:
    print(f"Unexpected error: {e}")
except KeyboardInterrupt:
    print("\nMasukkan inputan dengan benar")

# ini adalah prettytabel untuk read pelanggan apotik
tabelPelanggan = PrettyTable()
tabelPelanggan.field_names = ["username", "password", "saldo"]
pelangganjson = f"{ROOD_DIR}/projectAkhir/paloginpelanggan.json"
try:
    with open(pelangganjson, "r") as jsonpelanggan:
        data_pelanggan = json.loads(jsonpelanggan.read())

    for i in data_pelanggan:
        tabelPelanggan.add_row([i["username"], i["password"], i["saldo"]])
except FileNotFoundError:
    print(f"File not found: {pelangganjson}")
except KeyError:
    print("\nInvalid key in the JSON file.")
except json.JSONDecodeError:
    print("\nInvalid JSON file.")
except Exception as e:
    print(f"\nUnexpected error: {e}")
except KeyboardInterrupt:
    print("\nMasukkan inputan dengan benar")

# variabel saldo pelanggan
saldo_pelanggan = 0


# fungsi untuk menyimpan file json bagian data pelanggan
def savedatapelanggan():
    try:
        with open(pelangganjson, "w") as sn:
            json.dump(data_pelanggan, sn, indent=4)
    except FileNotFoundError:
        print(f"File not found: {pelangganjson}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    except KeyboardInterrupt:
        print("\nMasukkan inputan dengan benar")


# fungsi untuk menyipan file json bagian produk
def savejsonProduk():
    try:
        with open(produkjson, "w") as sn:
            json.dump(data_produk, sn, indent=4)

    except FileNotFoundError:
        print(f"File not found: {produkjson}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    except KeyboardInterrupt:
        print("\nMasukkan inputan dengan benar")


# fungsi untuk create produk
def create_produk():
    while True:
        try:
            tambahId = int(input("tambahkan id baru: "))
            tambahObat = input("isi nama obatnya: ")
            tambahKategori = input("isi kategori obat: ")
            tambahHarga = int(input("isi harganya: "))
            tambahStok = int(input("tambahkan stok: "))
            if tambahObat == "":
                print("nama obat tidak boleh kosong")
                continue
            if tambahKategori == "":
                print("kategori obat tidak boleh kosong")
                continue
            for x in data_produk:
                if tambahId == x["id"]:
                    print("id sudah tersedia, buat id yang lain!")
                    return
                continue
            data_produk.append(
                {
                    "id": tambahId,
                    "nama": tambahObat,
                    "kategori": tambahKategori,
                    "harga": tambahHarga,
                    "stok": tambahStok,
                }
            )
            tabel_produk.add_row(
                [tambahId, tambahObat, tambahKategori, tambahHarga, tambahStok]
            )
            print("obat berhasil ditambahkan")
            savejsonProduk()
            lagi = input("apakah anda ingin menambah obat lagi? (y/n)")
            if lagi == "y":
                create_produk()
            elif lagi == "n":
                break
            else:
                print("input y/n")         
        except ValueError:
            print("Masukkan input yang benar")
        except Exception as e:
            print("Eror:", str(e))
        except KeyboardInterrupt:
            print("\nMasukkan inputan dengan benar")


# fungsi read produk
def read_produk():
    global tabel_produk
    tabel_produk = PrettyTable()
    tabel_produk.field_names = [
        "ID",
        "Nama Obat",
        "Kategori Obat",
        "Harga Obat",
        "Stok Obat",
    ]
    try:
        for x in data_produk:
            tabel_produk.add_row(
                [x["id"], x["nama"], x["kategori"], x["harga"], x["stok"]]
            )
        print(tabel_produk)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    except KeyboardInterrupt:
        print("\nMasukkan inputan dengan benar")


# fungsi update produk
def update_produk(id, nama=None, kategori=None, harga=None, stok=None):
    read_produk()
    try:
        print("Silahkan Update Daftar Obat")
        id = int(input("Masukkan ID Obat yang akan diperbarui: "))
        nama = str(input("Masukkan Nama Obat baru: "))
        kategori = str(input("Masukkan Kategori Obat Baru: "))
        harga = int(input("Masukkan Harga Obat baru: "))
        stok = int(input("Masukkan Stok Obat baru: "))
        for item in data_produk:
            if item["id"] == id:
                if nama:
                    item["nama"] = nama
                if kategori:
                    item["kategori"] = kategori
                if harga:
                    item["harga"] = harga
                if stok:
                    item["stok"] = stok
                savejsonProduk()
                print("Produk berhasil di Update")
                return
        print("Produk tidak ditemukan")
        return
    except ValueError:
        print("\nMasukkan input yang benar")
    except Exception as e:
        print("\nEror:", str(e))
    except KeyboardInterrupt:
        print("\ninput yang anda masukkan tidak valid")


# fungsi delete produk
def delete_produk(data_produk):
    try:
        hapusId = int(input("masukkan id obat yang akan dihapus: "))
        index = -1
        for i in range(0, len(data_produk)):
            id = data_produk[i]
            if hapusId == id["id"]:
                index = i
                break
        if index == -1:
            print("id obat tidak ditemukan")
        else:
            del data_produk[index]
            print("berhasil menghapus obat")
        savejsonProduk()
    except ValueError:
        print("Masukkan input yang benar")
    except Exception as e:
        print("Error:", str(e))
    except KeyboardInterrupt:
        print("\ninput yang anda masukkan tidak valid")


# Fungsi search produk
def search():
    try:
        cari_produk = str(input("Masukkan Nama Produk yang akan dicari: "))
        produk_dict = {produk["nama"]: produk for produk in data_produk}

        if cari_produk in produk_dict:
            print(f"pencarian anda: {cari_produk} ada di data ")

            if "nama" not in produk_dict[cari_produk]:
                print("Error: Data produk tidak lengkap, nama tidak ada")
            else:
                global tabel_produk
                tabel_produk = PrettyTable()
                tabel_produk.field_names = ["Nama", "Kategori", "Harga", "Stok"]
                tabel_produk.add_row(
                    [
                        produk_dict[cari_produk]["nama"],
                        produk_dict[cari_produk]["kategori"],
                        produk_dict[cari_produk]["harga"],
                        produk_dict[cari_produk]["stok"],
                    ]
                )
                print(tabel_produk)
        else:
            print(f"pencarian anda: {cari_produk} tidak ada di data ")
    except ValueError:
        print("Masukkan input yang benar")
    except Exception as e:
        print("Error:", str(e))
    except KeyboardInterrupt:
        print("\ninput yang anda masukkan tidak valid")


# Fungsi Sorting produk nama
def sort_nama():
    global tabel_produk
    tabel_produk = PrettyTable()
    tabel_produk.field_names = [
        "ID",
        "Nama Obat",
        "Kategori Obat",
        "Harga Obat",
        "Stok Obat",
    ]
    try:
        for x in data_produk:
            tabel_produk.add_row(
                [x["id"], x["nama"], x["kategori"], x["harga"], x["stok"]]
            )
        tabel_produk.sortby = "Nama Obat"
        print(tabel_produk)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    except KeyboardInterrupt:
        print("\ninput yang anda masukkan tidak valid")


# Fungsi Sorting produk kategori
def sort_kategori():
    global tabel_produk
    tabel_produk = PrettyTable()
    tabel_produk.field_names = [
        "ID",
        "Nama Obat",
        "Kategori Obat",
        "Harga Obat",
        "Stok Obat",
    ]
    try:
        for x in data_produk:
            tabel_produk.add_row(
                [x["id"], x["nama"], x["kategori"], x["harga"], x["stok"]]
            )
        tabel_produk.sortby = "Kategori Obat"
        print(tabel_produk)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    except KeyboardInterrupt:
        print("\ninput yang anda masukkan tidak valid")


# Fungsi Sorting produk harga
def sort_harga():
    global tabel_produk
    tabel_produk = PrettyTable()
    tabel_produk.field_names = [
        "ID",
        "Nama Obat",
        "Kategori Obat",
        "Harga Obat",
        "Stok Obat",
    ]
    try:
        for x in data_produk:
            tabel_produk.add_row(
                [x["id"], x["nama"], x["kategori"], x["harga"], x["stok"]]
            )
        tabel_produk.sortby = "Harga Obat"
        print(tabel_produk)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    except KeyboardInterrupt:
        print("\ninput yang anda masukkan tidak valid")


# Fungsi Sorting produk ID
def sort_id():
    global tabel_produk
    tabel_produk = PrettyTable()
    tabel_produk.field_names = [
        "ID",
        "Nama Obat",
        "Kategori Obat",
        "Harga Obat",
        "Stok Obat",
    ]
    try:
        for x in data_produk:
            tabel_produk.add_row(
                [x["id"], x["nama"], x["kategori"], x["harga"], x["stok"]]
            )
        tabel_produk.sortby = "ID"
        print(tabel_produk)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    except KeyboardInterrupt:
        print("\ninput yang anda masukkan tidak valid")


# fungsi untuk menu admin
def menuAdmin():
    while True:
        print(
            f"""
~~~~~~~| SELAMAT DATANG |~~~~~~~
~~~~~| Apotek SI'A Kel 10 |~~~~~
+------------------------------+
|     Menu Admin Apotek        |
+------------------------------+
|    [1.] Lihat Produk         |
|    [2.] Tambah Produk        |
|    [3.] Update Produk        |
|    [4.] Hapus Produk         | 
|    [0.] Keluar               |
+------------------------------+"""
        )
        try:
            pilihan = int(input("Masukkan pilihan Admin: "))
        except ValueError:
            print("\nmasukkan angka pilihan angka 0-4")
            continue
        except KeyboardInterrupt:
            print("\ninput yang anda masukkan tidak valid")
            continue
        if pilihan == 1:
            os.system("cls")
            print("*" * 60 + "\n")
            print("                   APOTEK SI'23 KEL 10                ")
            print("*" * 60 + "\n")
            read_produk()
        elif pilihan == 2:
            os.system("cls")
            print("*" * 60 + "\n")
            print("                   APOTEK SI'23 KEL 10                ")
            print("*" * 60 + "\n")
            read_produk()
            create_produk()    
        elif pilihan == 3:
            os.system("cls")
            print("*" * 60 + "\n")
            print("                   APOTEK SI'23 KEL 10                ")
            print("*" * 60 + "\n")
            update_produk(id, nama=None, harga=None, stok=None)
        elif pilihan == 4:
            os.system("cls")
            print("*" * 60 + "\n")
            print("                   APOTEK SI'23 KEL 10                ")
            print("*" * 60 + "\n")
            read_produk()
            delete_produk(data_produk)
        elif pilihan == 0:
            os.system("cls")
            break
        else:
            print("masukkan angka dengan benar")


# fungsi melihat list admin
def liatAdmin():
    try:
        print(tabelAdmin)
    except FileNotFoundError:
        print("File tidak ditemukan.")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    except KeyboardInterrupt:
        print("\ninput yang anda masukkan tidak valid")


# fungsi untuk menambah admin/registrasi
def regis():
    while True:
        try:
            print("Silahkan Registrasi Akun Anda^^")
            username = input("Masukkan nama admin baru: ")
            password = pwinput.pwinput("Masukkan password admin baru: ")
            if username == "":
                print("username tidak boleh kosong")
                continue
            if password == "":
                print("password tidak boleh kosong")
                continue
            for i in data_admin:
                if username == i["username"]:
                    print("username sudah tersedia, cari username yang lain!")
                    return
                continue
            data_admin.append({"username": username, "password": password})
            tabelAdmin.add_row([username, password])
            with open(adminjson, "w") as sn:
                json.dump(data_admin, sn, indent=4)
            print(f"Admin {username} berhasil ditambahkan.")
            print(tabelAdmin)
            break
        except ValueError:
            print("Masukkan input yang benar")
        except KeyboardInterrupt:
            print("\ninput yang anda masukkan tidak valid")
        except Exception as e:
            print("Gagal mendaftarkan admin: ", (e))


# fungsi buat login admin
def login_admin():
    try:
        admin_regis = input("Apakah Sudah Memiliki Akun? y/t: ")
        if admin_regis == "y":
            print("~~~~~~~~~~~~~~Silahkan Login~~~~~~~~~~~~~~~~")
            print("Masukkan Username dan Password dengan Benar!")
            username = input("Masukkan username: ")
            pw = pwinput.pwinput("Masukkan password: ")
            os.system("cls")
            for i in data_admin:
                if i["username"] == username:
                    if i["password"] == pw:
                        print("Login Berhasil.")
                        print(f"Hallo Admin: {username}")
                        menuAdmin()
                        return
                    else:
                        print("password atau username anda masukkan salah")
                        return
            else:
                print("password atau username anda tidak terdaftar")
                return
        elif admin_regis == "t":
            while True:
                buatadmin = input("Apakah Ingin Membuat Akun Admin? y/t: ")
                if buatadmin == "y":
                    regis()
                elif buatadmin == "t":
                    break
                else:
                    print("Pilihan Anda Tidak Valid")
        else:
            print("silahkan input pilihan y/t")
    except FileNotFoundError:
        print("Terjadi Kesalahan Saat Membaca File.")
    except ValueError:
        print("Silahkan Coba Lagi Nanti.")
    except KeyboardInterrupt:
        print("\ninput yang anda masukkan tidak valid")


# fungsi login pelanggan
def loginpelanggan():
    global saldo_pelanggan
    global inUsername
    print("Selamat Datang Di Apotek SI'A Kel 10")
    try:
        pilihMember = input("apakah sudah memiliki akun pelanggan? y/t: ")
        if pilihMember == "y":
            inUsername = input("masukkan username anda: ")
            inpass = pwinput.pwinput("masukkan password anda: ")
            for x in data_pelanggan:
                if x["username"] == inUsername:
                    for y in data_pelanggan:
                        if y["password"] == inpass:
                            saldo_pelanggan = x["saldo"]
                            os.system("cls")
                            print("Login Berhasil.")
                            print(f"Hallo Pelanggan: {inUsername}")
                            menu_pelanggan()
                            return True
            print("username atau password salah atau tidak terdaftar")
        elif pilihMember == "t":
            while True:
                pilihMember = input("Apakah Ingin Membuat Akun Pelanggan? y/t: ")
                if pilihMember == "y":
                    tambah_pelanggan()
                elif pilihMember == "t":
                    break
                else:
                    print("Pilihan Anda Tidak Valid")
    except ValueError:
        print("\nMasukkan input yang benar")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
    except KeyboardInterrupt:
        print("\ninput yang anda masukkan tidak valid")


# fungsi untuk menambah pelanggan
def tambah_pelanggan():
    global data_pelanggan
    global tabel_produk
    while True:
        try:
            username = input("Masukkan nama pelanggan baru: ")
            password = pwinput.pwinput("Masukkan password pelanggan baru: ")
            saldo = int(input("berapa saldo anda: "))
            if username == "":
                print("username tidak boleh kosong")
                continue
            if password == "":
                print("password tidak boleh kosong")
                continue
            for i in data_pelanggan:
                if username == i["username"]:
                    print("username sudah tersedia, cari username yang lain!")
                    return
                continue
            data_pelanggan.append(
                {"username": username, "password": password, "saldo": saldo}
            )
            tabelPelanggan.add_row([username, password, saldo])
            with open(pelangganjson, "w") as sn:
                json.dump(data_pelanggan, sn, indent=4)
            print(f"Pelanggan baru {username} berhasil ditambahkan.")
            print(tabelPelanggan)
            break
        except ValueError:
            print("\nMasukkan input yang benar")
        except Exception as e:
            print("\nGagal mendaftarkan admin: ", (e))
        except KeyboardInterrupt:
            print("\ninput yang anda masukkan tidak valid")


# fungsi untuk pembeli membeli obat dan dapat langsung mencetak struk
def belanja():
    global saldo_pelanggan
    produk_dict = {produk["id"]: produk for produk in data_produk}
    try:
        read_produk()
        pilih = int(input("Masukkan id obat: "))
    except FileNotFoundError:
        print("\nFile data_produk tidak ditemukan")
        return
    except ValueError:
        print("\nMasukkan inputan angka")
        return
    except KeyboardInterrupt:
        print("\ninput yang anda masukkan tidak valid")
        return
    if pilih in produk_dict:
        produk_terpilih = produk_dict[pilih]
        print(f"Produk yang anda pilih adalah {produk_terpilih['nama']}")
        kuantitas = int(input("Masukkan kuantitas barang: "))
        if kuantitas <= produk_terpilih["stok"]:
            harga_total = produk_terpilih["harga"] * kuantitas
            produk_terpilih["stok"] -= kuantitas
            if saldo_pelanggan >= harga_total:
                sisa_saldo = saldo_pelanggan - harga_total
                saldo_pelanggan = sisa_saldo
                for pelanggan in data_pelanggan:
                    if pelanggan["username"] == inUsername:
                        pelanggan["saldo"] = saldo_pelanggan
                        savedatapelanggan()
                print("Barang berhasil di beli")
                cetakstruk = input("Cetak Struk Belanja Anda? y/t: ")
                if cetakstruk == "y":
                    os.system("cls")
                    with open("struk.txt", "a") as f:
                        f.write("\n")
                        f.write("*" * 80 + "\n")
                        f.write(
                            "                 APOTEK SI'A KEL 10                " + "\n"
                        )
                        f.write("*" * 80 + "\n")

                        for pelanggan in data_pelanggan:
                            if pelanggan["username"] == inUsername:
                                tanggal_transaksi = datetime.datetime.now().strftime(
                                    "%Y-%m-%d %H:%M:%S"
                                )
                                print(f"Tanggal Transaksi: {tanggal_transaksi}")
                                f.write(f"Tanggal Transaksi: {tanggal_transaksi}\n")

                                print(f"Nama Pelanggan: {inUsername}")
                                f.write(f"Nama Pelanggan: {inUsername}\n")

                                tabelstruk = PrettyTable(
                                    [
                                        "ID Obat",
                                        "Nama Obat",
                                        "Kategori",
                                        "Kuantitas",
                                        "Harga Satuan",
                                        "Total Harga",
                                    ]
                                )
                                tabelstruk.add_row(
                                    [
                                        pilih,
                                        produk_terpilih["nama"],
                                        produk_terpilih["kategori"],
                                        kuantitas,
                                        produk_terpilih["harga"],
                                        harga_total,
                                    ]
                                )
                                print(tabelstruk)
                                f.write(str(tabelstruk) + "\n")

                                print(
                                    f"Saldo Anda Sebelum Transaksi: {saldo_pelanggan + harga_total}"
                                )
                                print(
                                    f"Saldo Anda Sesudah Transaksi: {saldo_pelanggan}"
                                )
                                print(
                                    "Terimakasih sudah berbelanja di Apotek SI'A Kel 10"
                                )
                                print("Semoga Lekas Sembuh")
                elif cetakstruk == "t":
                    print("Terimakasih sudah berbelanja di Apotek SI'A Kel 10")
                    print("Semoga Lekas Sembuh")
                else:
                    print("Pilihan anda tidak valid")
            else:
                print("Saldo tidak cukup")
        else:
            print("Kuantitas yang anda pesan melebihi stok")
    else:
        print("Barang tidak ada")


# fungsi menu pelanggan
def menu_pelanggan():
    global saldo_pelanggan
    while True:
        print(
            f"""
~~~~~~~~~~~| SELAMAT DATANG |~~~~~~~~~~
~~~~~~~~~| Apotek SI'A Kel 10 |~~~~~~~~
+--------------------------------------+
|         Menu Pembeli Apotek          |
+--------------------------------------+
|     [1.] Lihat dan beli Produk       |
|     [2.] Isi Saldo                   |
|     [3.] Tampilkan Saldo             |
|     [4.] Search Produk               |
|     [5.] Sorting Produk              |
|     [0.] Keluar                      |
+--------------------------------------+"""
        )
        try:
            pilih = int(input("pilih menu: "))
        except ValueError:
            print("\nmasukkan angka pilihan angka (0/1/2/3/4/5): ")
            continue
        except KeyboardInterrupt:
            print("\ninput yang anda masukkan tidak valid")
            continue
        if pilih == 1:
            os.system("cls")
            print("~" * 50)
            print("                 SELAMAT BERBELANJA!             ")
            print("~" * 50)
            belanja()
        elif pilih == 2:
            try:
                os.system("cls")
                print("~" * 50)
                print("                   SELAMAT DATANG                 ")
                print("                   ISI SALDO ANDA                 ")
                print("~" * 50)
                tambah_saldo = int(
                    input("Masukkan berapa saldo yang ingin ditambahkan: ")
                )
            except ValueError:
                print("\nmasukkan inputan yang benar")
                continue
            except KeyboardInterrupt:
                print("\nInput yang anda masukkan tidak valid")
                continue
            saldo_baru = saldo_pelanggan + tambah_saldo
            saldo_pelanggan = saldo_baru
            for pelanggan in data_pelanggan:
                if pelanggan["username"] == inUsername:
                    pelanggan["saldo"] = saldo_pelanggan
                    savedatapelanggan()
                    print("Saldo Anda Berhasil Di Tambahkan!")
        elif pilih == 3:
            os.system("cls")
            print("Login Berhasil.")
            print(f"Hallo Admin: {inUsername}")
            print(f"Saldo anda sekarang: {saldo_pelanggan}")
        elif pilih == 4:
            os.system("cls")
            search()
        elif pilih == 5:
            os.system("cls")
            print(
                f"""
+------------------------+
|    Sorting barang      |
+------------------------+
|   1. Sorting Nama      |
|   2. Sorting Kategori  |
|   3. Sorting Harga     |
|   4. Sorting ID        |
|   0. Keluar            |
+------------------------+"""
            )
            try:
                pilih = input("\nPilih Sorting berdasarkan (0/1/2/3/4): ")
                if pilih == "1":
                    os.system("cls")
                    print("\n===|SORTING OBAT SESUAI URUTAN NAMA|=== ")
                    sort_nama()
                elif pilih == "2":
                    os.system("cls")
                    print("\n===|SORTING OBAT SESUAI URUTAN KATEGORI|=== ")
                    sort_kategori()
                elif pilih == "3":
                    os.system("cls")
                    print("\n===|SORTING OBAT SESUAI URUTAN HARGA TERRENDAH|=== ")
                    sort_harga()
                elif pilih == "4":
                    os.system("cls")
                    print("\n===|SORTING OBAT SESUAI URUTAN ID|=== ")
                    sort_id()
                elif pilih == "0":
                    os.system("cls")
                    break
                else:
                    print("Pilihan anda tidak valid")
            except ValueError:
                print("\nmasukkan inputan yang benar")
                continue
            except KeyboardInterrupt:
                print("\nInput yang anda masukkan tidak valid")
                continue
        elif pilih == 0:
            os.system("cls")
            break
        else:
            print("Pilihan anda tidak valid")


# fungsi program utama
def main():
    while True:
        print(
            f"""
~~~~~~~| SELAMAT DATANG |~~~~~~~
~~~~~| Apotek SI'A Kel 10 |~~~~~
+-----------------------------+
|       MASUK SEBAGAI         |
+-----------------------------+
|        [1.] Admin           |
|        [2.] Pembeli         |
|        [0.] Keluar          |
+-----------------------------+"""
        )
        try:
            pilihan = int(input("Masuk Sebagai: "))
        except ValueError:
            print("\nMasukkan angka pilihan (0/1/2) ")
            continue
        except KeyboardInterrupt:
            print("\nInput yang anda masukkan tidak valid")
            continue
        if pilihan == 1:
            os.system("cls")
            login_admin()
        elif pilihan == 2:
            os.system("cls")
            loginpelanggan()
        elif pilihan == 0:
            os.system("cls")
            print("Terimakasih Telah Mengguanakan Program ini ^^ ! ")
            print(
                f"""
====================================
SEMANGAT BEKERJA DAN JAGA KESEHATAN!
===================================="""
            )
            break
        else:
            print("pilihan anda tidak valid")


main()
