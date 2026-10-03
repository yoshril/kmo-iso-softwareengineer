anggota = ["Nazril", "Fadil", "Nando", "Rasya", "Abyaz", "Mentari", "Rahmat", "Kamil", "Rama", "Cici", "Salwa", "Khansa", "Fakhri", "Rizki", "Afif"]

while True:
    print("====== Menu  ======") 
    print("1. Profil Kelompok")
    print("2. Anggota Kelompok")
    print("3. Nama Bindam")
    print("4. Menambah anggota")
    print("5. Menghapus anggota")
    print("6. Keluar")
    pilihan = input("Masukkan pilihan (1-6): ")

    if pilihan == "1":
        print("=============== Profil Kelompok ===============")
        print("Bentuk hexagon dan perpaduan warna biru melamnbangkan keandalan tingkat tinggi, performa maksimal, serta ketajaman logika. Roda gigi dan simbol kode menggambarkan bentuk harmonis mesin teknis dan kendali kode yang bekerja presisi")
    elif pilihan == "2":
        print("============= Anggota Kelompok =============")
        print(anggota)
    elif pilihan == "3":
        print("============= Nama Bindam =============")
        print("1. Gilbert Finsen Zakaria Lian")
        print("2. Ken Bilqis Nuraini")
    elif pilihan == "4":
        print("============= Menambah Anggota =============")
        anggota_baru = input("Masukkan nama anggota baru: ")
        anggota.append(anggota_baru)
        print(f"Anggota {anggota_baru} telah ditambahkan")
    elif pilihan == "5":
        print("============= Menghapus Anggota =============")
        print(anggota)
        anggota_hapus = input("Masukkan nama anggota yang ingin dihapus: ")
        anggota.remove(anggota_hapus)
        print(f"Anggota {anggota_hapus} telah dihapus")
    elif pilihan == "6":
        print("Keluar dari program")
        break
    else:
        print("Pilihan tidak ada, Silakan coba lagi")