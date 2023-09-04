def NextTime():
    jam = int(input("Masukkan jam: "))
    menit = int(input("Masukkan menit: "))
    detik = int(input("Masukkan detik: "))

    # Menambahkan 1 detik
    detik += 1

    # Memeriksa apakah detik mencapai 60
    if detik == 60:
        detik = 0
        menit += 1

        # Memeriksa apakah menit mencapai 60
        if menit == 60:
            menit = 0
            jam += 1

            # Memeriksa apakah jam mencapai 24
            if jam == 24:
                jam = 0

    print(f"Waktu berikutnya adalah {jam:02d}:{menit:02d}:{detik:02d}")

NextTime()
