import CalismaProgramiTemizleme
import time

print("""
*****************************************
|                                       |
|    Ödev Programı 1.0'a Hoş geldiniz   |
|            İlkokul                   |
|                                       |
*****************************************
""")

while True:
    print("""
    1-İlkokul Çalışma Programlarını Sıfırlayın
    2-İlkokul Raporları Sıfırlayın
    3-Çıkış
    """)
    secenek=input("Lütfen Seçeneğinizi Giriniz:\n")
    if(secenek=="3"):
        print("Programı Kullandığınız İçin Teşekkürler...")
        break
    elif(secenek=="1"):
        print("Çalışma Programları Sıfırlanıyor....")
        CalismaProgramiTemizleme.sifirla()
        print("Çalışma Programları Sıfırlandı")
    elif(secenek=="2"):
        print("Raporlar Sıfırlanıyor....")
        time.sleep(3)
        print("Raporlar Sıfırlandı")
    else:
        print("Yanlış Bir Seçenek Seçtiniz.")