# -*- coding: utf-8 -*-
"""
@author: sametemirog
"""

import requests
from bs4 import BeautifulSoup

#Kitap Arama
arama = input("Kitap İsmini Girin: ")

#Arama Boşluk Karaterleri
aramaKY = arama.replace(" ","%20")
aramaKide = arama.replace(" ","+")

#Arama URL
kitapyurdu = "https://www.kitapyurdu.com/index.php?route=product/search&sort=p.price&order=ASC&filter_name="+aramaKY
kidega = "https://kidega.com/arama?query="+aramaKide+"&order=fiyatArtan&searchInput=&searchInput=&minPrice=&maxPrice="
d_r = "https://www.dr.com.tr/search?q="+aramaKY+"&cat=0%2C10001&parentId=10001"
bkm = "https://www.bkmkitap.com/arama?q="+aramaKide

#Web Site İstek
responseKY = requests.get(kitapyurdu)
htmlKY = responseKY.content

responseKidega = requests.get(kidega)
htmlKidega = responseKidega.content

responseDR = requests.get(d_r)
htmlDR = responseDR.content

responseBKM = requests.get(bkm)
htmlBKM = responseBKM.content

#Html Parçalama ve Yazdırma
soupKY = BeautifulSoup(htmlKY,"html.parser")
fiyatlarKY = soupKY.find_all("span",{"class":"value"},limit=4)
print("Kitap Yurdu:\n" + fiyatlarKY[1].text)

soupKidega = BeautifulSoup(htmlKidega,"html.parser")
fiyatlarKidega = soupKidega.find_all("b",{"class":"lastPrice"});
print("Kidega:\n"+fiyatlarKidega[0].text.replace(" ₺",""))

soupDR = BeautifulSoup(htmlDR,"html.parser")
fiyatlarDR = soupDR.find_all("span",{"class":"price"})
print("DR:\n"+fiyatlarDR[0].text)

soupBKM = BeautifulSoup(htmlBKM,"html.parser")
fiyatlarBKM = soupBKM.find_all("div",{"class":"col col-12 currentPrice"});
print("BKM:"+fiyatlarBKM[0].text.replace("TL",""))