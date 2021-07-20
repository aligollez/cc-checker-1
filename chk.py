from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import time


mail = input('Mail: ')
passw = input('Password: ')
Card = input('Card Number: ')
Skt = input('Month (type without using 0. Ex:4):')
Skt1 = input('Year (Ex:2024): ')
Cvv = input('Cvv: ')

driver_path = "C:\\Users\\XXXX\\Desktop\\checker\\chromedriver.exe"
options = Options()
options.add_argument('--headless')
options.add_argument('--disable-gpu')
browser = webdriver.Chrome(executable_path=driver_path,chrome_options=options)
browser.get('https://www.kirmizikedi.com/uyelik/uye-giris')

email = browser.find_element_by_id('EmailAddress')
email.send_keys(mail)
password = browser.find_element_by_id('Password')
password.send_keys(passw)
login = browser.find_element_by_xpath('/html/body/section[2]/div/div[1]/div/form/button')
login.click()
browser.get('https://www.kirmizikedi.com/kitap/urun/4b1aa737165344468b096a806b683d09')
sepete_ekle = browser.find_element_by_id('sepeteekle_4b1aa737165344468b096a806b683d09')
sepete_ekle.click()
time.sleep(3)
sepete_git = browser.find_element_by_id('cartLink')
sepete_git.click()
time.sleep(1)
buy = browser.find_element_by_xpath('/html/body/section[2]/div/div[1]/div[2]/div[2]/div/div[2]/a')
buy.click()
time.sleep(2)
""" yeni_adres = browser.find_element_by_xpath('/html/body/section[2]/div/div[1]/form/div[1]/a')
yeni_adres.click()

adres_adı = browser.find_element_by_name('Address.Name')
adres_adı.send_keys('ev')

alacak_kisi = browser.find_element_by_name('Address.DeliveryPerson')
alacak_kisi.send_keys('metin sen')

ülke = Select(browser.find_element_by_name('Address.CountryId'))
ülke.select_by_value('1')
time.sleep(1)
sehir = Select(browser.find_element_by_name('Address.CityId'))
sehir.select_by_value('4')
time.sleep(1)
ilce = Select(browser.find_element_by_name('Address.TownId'))
ilce.select_by_value('52')

posta_kodu = browser.find_element_by_id('Address_PostalCode')
posta_kodu.send_keys('21100')

acık_adres = browser.find_element_by_name('Address.StreetAddress')
acık_adres.send_keys('asdasdasdasd56as1d56as1da')

telefon = browser.find_element_by_name('Address.PhoneNumber')
telefon.send_keys('5523694951')

varsayılan = browser.find_element_by_xpath('/html/body/section[2]/div/div[1]/div/div[3]/form/div[11]/label/input')
varsayılan.click()

kaydet = browser.find_element_by_xpath('/html/body/section[2]/div/div[1]/div/div[3]/form/button')
kaydet.click()"""

devam_et = browser.find_element_by_xpath('/html/body/section[2]/div/div[1]/form/div[2]/div[2]/div/div[2]/button')
devam_et.click()
time.sleep(2)
devam_et2 = browser.find_element_by_xpath('/html/body/section[2]/div/div[1]/form/div[2]/div[2]/div/div[2]/button')
devam_et2.click()
cardname = browser.find_element_by_name('CreditCard.KarttakiIsim')
cardname.send_keys('Metin Şen')
CardNumber = browser.find_element_by_name('CreditCard.KartNum')
CardNumber.send_keys(Card)
Skt_number = Select(browser.find_element_by_name('CreditCard.ExpireDateMonth'))
Skt_number.select_by_visible_text(Skt)
Skt_year = Select(browser.find_element_by_name('CreditCard.ExpireDateYear'))
Skt_year.select_by_visible_text(Skt1)
Cvv_number = browser.find_element_by_id('CreditCard_Gk')
Cvv_number.send_keys(Cvv)
for i in range(1,2):
    browser.execute_script('window.scrollTo(0,document.body.scrollHeight)')
    time.sleep(3)
Ön_bilgilendirme = browser.find_element_by_xpath('/html/body/section[2]/div/div[1]/form/div[1]/div[5]/div/label/input')
Ön_bilgilendirme.click()
time.sleep(1)
Mesafeli = browser.find_element_by_xpath('/html/body/section[2]/div/div[1]/form/div[1]/div[6]/div/label/input')
Mesafeli.click()
time.sleep(1)
Sepeti_onayla = browser.find_element_by_id('btnCompleteOrder')
Sepeti_onayla.click()
time.sleep(5)
try:
    dec = browser.find_element_by_xpath('/html/body/section[2]/div/div[1]/form/div[1]/div[2]/div').text
    print(dec)
    print("Dec: "+Card+"|"+Skt+"|"+Skt1+"|"+Cvv)
except:
    a = ('Live: '+Card+"|"+Skt+"|"+Skt1+"|"+Cvv)
    print(a)    

   
