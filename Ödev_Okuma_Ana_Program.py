from openpyxl import load_workbook

print(""""
[Ö]=========ÖTS============[-][o][x]
|                                 |
|     Programa Hoşgeldiniz!       |
|           Sürüm 1.0             |
|                                 |
|                                 |
|                                 |
|=================================|


""")

calismaKitabi=load_workbook(filename="rapor.xlsx")
sayfalar=calismaKitabi["sayfa"]
ogrenciListesi=[]
notlar=[]
dersIsimleri=["Türkçe","Matematik","Fen Bilimleri","Sosyal Bilgiler","İngilizce","Din"]

#Ders Fonksiyonları satır sayısını string olarak alıyor. Dizi olarak return ediyor.
def turkceAl(satir):
    turkce = []
    turkce.append(sayfalar["H"+str(satir)].value)
    turkce.append(sayfalar["I"+str(satir)].value)
    turkce.append(sayfalar["J"+str(satir)].value)
    return turkce

def matematikAl(satir):
    matematik = []
    matematik.append(sayfalar["M"+str(satir)].value)
    matematik.append(sayfalar["N"+str(satir)].value)
    matematik.append(sayfalar["O"+str(satir)].value)
    matematik.append(sayfalar["P"+str(satir)].value)

    return matematik

def fenAl(satir):
    fen = []
    fen.append(sayfalar["S"+str(satir)].value)
    fen.append(sayfalar["T"+str(satir)].value)
    return fen

def sosyalAl(satir):
    sosyal = []
    sosyal.append(sayfalar["W"+str(satir)].value)
    sosyal.append(sayfalar["X"+str(satir)].value)

    return sosyal

def ingilizceAl(satir):
    ing = []
    ing.append(sayfalar["Z" + str(satir)].value)
    ing.append(sayfalar["AA" + str(satir)].value)
    ing.append(sayfalar["AB" + str(satir)].value)
    ing.append(sayfalar["AC" + str(satir)].value)
    ing.append(sayfalar["AD" + str(satir)].value)
    ing.append(sayfalar["AE" + str(satir)].value)
    ing.append(sayfalar["AF" + str(satir)].value)
    return ing

def dinAl(satir):
     din = []

#Tarih Fonksiyonu. Tarihi return ediyor.
def tarihiAl():
    tarih=sayfalar["G2"].value
    return tarih

#Öğrenci Liste Fonksiyonu. Öğrenci Listesini alıyor dizi olarak return ediyor.
def ogrenciListeAl(satir):
    satir=int(satir)
    ogrListe=[]
    for i in range(5,satir):
        ogrListe.append(sayfalar["E"+str(i)].value)
    return ogrListe
#Ders Al Fonksiyonu: Parametre olarak satır sayısını alır. Tüm dersleri bir diziye atar ve return eder.
def dersAl(satir):
    notlar=[]
    for i in range(5,satir):
        notlar.append(turkceAl(i))
        notlar.append(matematikAl(i))
        notlar.append(fenAl(i))
        notlar.append(sosyalAl(i))
        notlar.append(ingilizceAl(i))
        notlar.append(dinAl(i))
    return notlar

sonSatir=input("Lütfen Son Satırı Giriniz:\n")
ogrenciListesi=ogrenciListeAl(sonSatir)
notlar=dersAl(int(sonSatir))

for i in range(0,int(sonSatir)-5):
    print(ogrenciListesi[i])
    for j in range(0,6):
        print(dersIsimleri[j])
        print(notlar[j])
    print("\n")
