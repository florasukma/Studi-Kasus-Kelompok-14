# input: Mata Uang, Nilai Konversi Mata uang, Nominal Sebelum Konversi
# output: Nominal Setelah Konversi

listmatauang= [
              {
                  "matauang":"Dollar Amerika",
                  "nilairupiah":14082,
              },
              {
                  "matauang":"Dollar Australia",
                  "nilairupiah":10135,
              },
              {
                  "matauang":"Dollar Singapura",
                  "nilairupiah":10323,
              },
              {
                  "matauang":"Yen Jepang",
                  "nilairupiah":122.40,
              },
              {
                  "matauang":"Yuan China",
                  "nilairupiah":2083,
              },
              {
                  "matauang":"Ringgit Malaysia",
                  "nilairupiah":3237,
              },
              {
                  "matauang":"Euro",
                  "nilairupiah":15947,
              },
              {
                  "matauang":"Rupiah",
                  "nilairupiah":1
              }
    ]

#halaman awal
print('='*50)
print("Konversi Mata Uang PT.ICL")
print('='*50)

quest = True
while quest == True :

    #Menu utama
    print('Menu:\n1. Mengubah Data Konversi Mata Uang \n2. Konversi Mata Uang \n3. Keluar' )
    menu = int(input("Pilihan menu (1/2/3): "))

    # Mengubah data konversi
    if menu == 1:
        #login admin
        userpass = {"alfiko":"1234","khansa":"1234","danu":"1234","fitri":"1234","flora":"1234","aldi":"1234"}
        i=3
        while i>=1:
            userid = input("Masukkan username anda: ").lower()
            password = input("Masukkan password anda: ")
            if userid in userpass and password == userpass[userid]:
                print("Login Berhasil")
                break
            i-=1
            if i==0 :
                print("Login Gagal")
                quit()
            print("login ditolak, sisa percobaan login: ",i)
        
        # menampilkan data
        y = True
        while y == True:
            print("="*50,"\nBerikut merupakan data konversi mata uang:")        
            i=0
            for indeks, item in enumerate(listmatauang,start=1):
                matauang=listmatauang[i]['matauang']
                nilairupiah=listmatauang[i]['nilairupiah']
                print(indeks, '1', matauang,'=', 'Rp', nilairupiah)
                i+=1
                indeks+=1

            #pilih mata uang
            input1 = int(input("\nMasukkan kode mata uang yang akan diubah: "))
            input2 = float(input("Masukkan nominal baru: "))
            if input1 <= 7:
                listmatauang[input1-1]['nilairupiah']=input2
                print("="*50,"\nData Konversi Mata Uang ke Rupiah\n","="*50)
                i=0
                for indeks, item in enumerate(listmatauang,start=1):
                    matauang=listmatauang[i]['matauang']
                    nilairupiah=listmatauang[i]['nilairupiah']
                    print(indeks, '1', matauang,'=', 'Rp', nilairupiah)
                    i+=1
                    indeks+=1
                decision1 = (input("\nApakah Anda akan mengubah data konversi lain? (yes/no): "))
                if decision1 == "yes":
                    continue
                else:
                    break
            else:
                break

    # mengkonversi mata uang
    elif menu == 2:
        
        # menampilkan menu
        q = True
        while q == True:
            print("="*50,"\nBerikut merupakan data konversi mata uang: ")
            i=0
            for indeks, item in enumerate(listmatauang,start=1):
                matauang=listmatauang[i]['matauang']
                nilairupiah=listmatauang[i]['nilairupiah']
                print(indeks, '1', matauang,'=', 'Rp', nilairupiah)
                i+=1
                indeks+=1

            # melakukan konversi
            pilihan1=int(input('\nMasukkan kode mata uang yang dipilih:'))
            matauangterpilih1=listmatauang[pilihan1-1]['matauang']
            print('\nAnda akan mengkonversi mata uang', matauangterpilih1)
            nilairupiah=listmatauang[pilihan1-1]['nilairupiah']
            nominal=int(input('Masukkan nominal mata uang: '))

            pilihan2=int(input('Masukkan kode mata uang tujuan: '))
            nilairupiah=listmatauang[pilihan1-1]['nilairupiah']
            nilairupiah1=listmatauang[pilihan2-1]['nilairupiah']

            if pilihan2 == 1:
                hasil=nominal*nilairupiah/nilairupiah1
                print('Hasil konversinya yaitu: ', hasil, 'Dollar Amerika')

            elif pilihan2 == 2:
                hasil=nominal*nilairupiah/nilairupiah1
                print('Hasil konversinya yaitu: ', hasil, 'Dollar Australia')

            elif pilihan2 == 3:
                hasil=nominal*nilairupiah/nilairupiah1
                print('Hasil konversinya yaitu: ', hasil, 'Dollar Singapura')

            elif pilihan2 == 4:
                hasil=nominal*nilairupiah/nilairupiah1
                print('Hasil konversinya yaitu: ', hasil, 'Yen Jepang')

            elif pilihan2 == 5:
                hasil=nominal*nilairupiah/nilairupiah1
                print('Hasil konversinya yaitu: ', hasil, 'Yuan China')

            elif pilihan2 == 6:
                hasil=nominal*nilairupiah/nilairupiah1
                print('Hasil konversinya yaitu: ', hasil, 'Ringgit Malaysia')

            elif pilihan2 == 7:
                hasil=nominal*nilairupiah/nilairupiah1
                print('Hasil konversinya yaitu: ', hasil, 'Euro')

            else:
                hasil=nominal*nilairupiah/nilairupiah1
                print('Hasil konversinya yaitu: ', hasil, 'Rupiah')
            
            decision2 = (input("Apakah Anda akan melakukan konversi lagi? (yes/no): ")).lower()
            if decision2 == "yes":
                continue
            else:
                break

    # menu keluar
    else :
        print("Terima Kasih")
        quit()