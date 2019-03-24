import gspread
import time
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('OdevSistemi-fc12779d1a3c.json', scope)
client = gspread.authorize(creds)

def besinciSinif(tarih):

    sheet = client.open('5. Sınıflar Haftalık Çalışma Programı').sheet1

    sheet.update_acell('H2', tarih)
    sheet.update_acell('B6','')
    sheet.update_acell('C6', '')
    sheet.update_acell('D6', '')
    sheet.update_acell('E6', '')
    sheet.update_acell('F6', '')
    sheet.update_acell('G6', '')
    sheet.update_acell('H6', '')
    sheet.update_acell('B9', '')
    sheet.update_acell('C9', '')
    sheet.update_acell('D9', '')
    sheet.update_acell('E9', '')
    sheet.update_acell('F9', '')
    sheet.update_acell('G9', '')
    sheet.update_acell('H9', '')
    sheet.update_acell('B12', '')
    sheet.update_acell('C12', '')
    sheet.update_acell('D12', '')
    sheet.update_acell('E12', '')
    sheet.update_acell('F12', '')
    sheet.update_acell('G12', '')

    time.sleep(20)
    print("5. Sınıf Çalışma Programı Sıfırlanmıştır")

def altinciSinif(tarih):

    sheet = client.open('6. Sınıflar Haftalık Çalışma Programı').sheet1

    sheet.update_acell('H2', tarih)
    sheet.update_acell('B6','')
    sheet.update_acell('C6', '')
    sheet.update_acell('D6', '')
    sheet.update_acell('E6', '')
    sheet.update_acell('F6', '')
    sheet.update_acell('G6', '')
    #sheet.update_acell('H6', '')
    sheet.update_acell('B9', '')
    sheet.update_acell('C9', '')
    sheet.update_acell('D9', '')
    sheet.update_acell('E9', '')
    sheet.update_acell('F9', '')
    sheet.update_acell('G9', '')
    #sheet.update_acell('H9', '')
    sheet.update_acell('B12', '')
    sheet.update_acell('C12', '')
    sheet.update_acell('D12', '')
    sheet.update_acell('E12', '')
    sheet.update_acell('F12', '')
    sheet.update_acell('G12', '')

    time.sleep(20)
    print("6. Sınıf Çalışma Programı Sıfırlanmıştır")

def yedinciSinif(tarih):

    sheet = client.open('7. Sınıflar Haftalık Çalışma Programı').sheet1

    sheet.update_acell('H2', tarih)
    sheet.update_acell('B6','')
    sheet.update_acell('C6', '')
    sheet.update_acell('D6', '')
    sheet.update_acell('E6', '')
    sheet.update_acell('F6', '')
    sheet.update_acell('G6', '')
    sheet.update_acell('H6', '')
    sheet.update_acell('B9', '')
    sheet.update_acell('C9', '')
    sheet.update_acell('D9', '')
    sheet.update_acell('E9', '')
    sheet.update_acell('F9', '')
    sheet.update_acell('G9', '')
    sheet.update_acell('H9', '')
    sheet.update_acell('B12', '')
    sheet.update_acell('C12', '')
    sheet.update_acell('D12', '')
    sheet.update_acell('E12', '')
    sheet.update_acell('F12', '')
    sheet.update_acell('G12', '')

    time.sleep(20)
    print("7. Sınıf Çalışma Programı Sıfırlanmıştır")

def sekizASinifi(tarih):

    sheet = client.open('8-A Sınıfı Haftalık Çalışma Programı').sheet1

    sheet.update_acell('H2', tarih)
    sheet.update_acell('B6','')
    sheet.update_acell('C6', '')
    sheet.update_acell('D6', '')
    sheet.update_acell('E6', '')
    sheet.update_acell('F6', '')
    sheet.update_acell('G6', '')
    sheet.update_acell('H6', '')
    sheet.update_acell('B9', '')
    sheet.update_acell('C9', '')
    sheet.update_acell('D9', '')
    sheet.update_acell('E9', '')
    sheet.update_acell('F9', '')
    sheet.update_acell('G9', '')
    sheet.update_acell('H9', '')
    sheet.update_acell('B12', '')
    sheet.update_acell('C12', '')
    sheet.update_acell('D12', '')
    sheet.update_acell('E12', '')
    sheet.update_acell('F12', '')
    sheet.update_acell('G12', '')
    sheet.update_acell('H12', '')
    sheet.update_acell('B15', '')
    sheet.update_acell('C15', '')
    sheet.update_acell('D15', '')
    sheet.update_acell('E15', '')
    sheet.update_acell('F15', '')
    sheet.update_acell('G15', '')
    sheet.update_acell('H15', '')
    sheet.update_acell('H18', '')

    time.sleep(20)
    print("8-A Sınıfı Çalışma Programı Sıfırlanmıştır")

def sekizBSinifi(tarih):

    sheet = client.open('8-B Sınıfı Haftalık Çalışma Programı').sheet1

    sheet.update_acell('H2', tarih)
    sheet.update_acell('B6', '')
    sheet.update_acell('C6', '')
    sheet.update_acell('D6', '')
    sheet.update_acell('E6', '')
    sheet.update_acell('F6', '')
    sheet.update_acell('G6', '')
    sheet.update_acell('H6', '')
    sheet.update_acell('B9', '')
    sheet.update_acell('C9', '')
    sheet.update_acell('D9', '')
    sheet.update_acell('E9', '')
    sheet.update_acell('F9', '')
    sheet.update_acell('G9', '')
    sheet.update_acell('H9', '')
    sheet.update_acell('B12', '')
    sheet.update_acell('C12', '')
    sheet.update_acell('D12', '')
    sheet.update_acell('E12', '')
    sheet.update_acell('F12', '')
    sheet.update_acell('G12', '')
    sheet.update_acell('H12', '')
    sheet.update_acell('B15', '')
    sheet.update_acell('C15', '')
    sheet.update_acell('D15', '')
    sheet.update_acell('E15', '')
    sheet.update_acell('F15', '')
    sheet.update_acell('G15', '')
    sheet.update_acell('H15', '')
    sheet.update_acell('H18', '')

    time.sleep(20)
    print("8-B Sınıfı Çalışma Programı Sıfırlanmıştır")

def sekizCSinifi(tarih):

    sheet = client.open('8-C Sınıfı Haftalık Çalışma Programı').sheet1

    sheet.update_acell('H2', tarih)
    sheet.update_acell('B6', '')
    sheet.update_acell('C6', '')
    sheet.update_acell('D6', '')
    sheet.update_acell('E6', '')
    sheet.update_acell('F6', '')
    sheet.update_acell('G6', '')
    sheet.update_acell('H6', '')
    sheet.update_acell('B9', '')
    sheet.update_acell('C9', '')
    sheet.update_acell('D9', '')
    sheet.update_acell('E9', '')
    sheet.update_acell('F9', '')
    sheet.update_acell('G9', '')
    sheet.update_acell('H9', '')
    sheet.update_acell('B12', '')
    sheet.update_acell('C12', '')
    sheet.update_acell('D12', '')
    sheet.update_acell('E12', '')
    sheet.update_acell('F12', '')
    sheet.update_acell('G12', '')
    sheet.update_acell('H12', '')
    sheet.update_acell('B15', '')
    sheet.update_acell('C15', '')
    sheet.update_acell('D15', '')
    sheet.update_acell('E15', '')
    sheet.update_acell('F15', '')
    sheet.update_acell('G15', '')
    sheet.update_acell('H15', '')
    sheet.update_acell('H18', '')

    time.sleep(20)
    print("8-C Sınıfı Çalışma Programı Sıfırlanmıştır")

def sifirla():
    tarih=input("Ödev Tarihini Giriniz: \n")
    besinciSinif(tarih)
    altinciSinif(tarih)
    yedinciSinif(tarih)
    sekizASinifi(tarih)
    sekizBSinifi(tarih)
    sekizCSinifi(tarih)

    print("Tüm çalışma programı güncellemeleri bitmiştir. Lütfen kontol etmeyi ihmal etmeyiniz")


