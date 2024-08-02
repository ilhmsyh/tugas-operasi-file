def baca_file(nama_file):
    with open(nama_file, "r") as file_txt:
        isi_file = file_txt.read()
        print(isi_file)

def tulis_file(nama_file):
    
    baca_file("file.txt")

    nama_anggota = input("Nama anggota kelompok: ")
    text = "\n {}".format(nama_anggota)

    with open(nama_file, "a") as file_anggota:
        file_anggota.write(text)

tulis_file("file.txt")