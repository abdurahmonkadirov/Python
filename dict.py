#Assalomu alayum do'stlar bugun sizlar bilan lug'atlar haqida gaplashamiz
myDict={} #Bu xato bo'ladi yani buni type(myDict) qilsak set deb qaytaradi.Buni dictga aylantirish uchun
myDict["integer"]=7#integer bu key 7esa value kalit va qiymat bo'ladi
myDict["string"]="bu matn"
myDict["list"]=["bu royxat","royhatning ikkinchi elmenti"]
myDict["dictionary"]={"bu dict":"bu dictning qiymati"}
print(myDict) #Output:{'integer': 7, 'string': 'bu matn', 'list': ['bu royxat', 'royhatning ikkinchi elmenti'], 'dictionary': {'bu dict': 'bu dictning qiymati'}}
#Bizga dictni nima keragi bor deyish mumkin men hozir sizga dictni eng kerakli qismini o'rgataman
#Keling ekranga integerlarni chiqaramiz
print(myDict["integer"]) #Output:7
#Endi qolganlarni chiiqaramiz
print(myDict["string"]) #Output:"bu matn"
print(myDict["list"]) #Output:['bu royxat', 'royhatning ikkinchi elmenti']
print(myDict["dictionary"]) #Output:{'bu dict': 'bu dictning qiymati'}
#Mana bular dictni funksiyalari:
print(myDict.get("integers","Bunday so'z topilmadi")) #Agar dictda valu bo'lsa ishlaydi Bo'lmasa "Bunday so'z topilmadi" xabarini qaytaradi
for key,value in myDict.items(): #myDictning barcha key valuelarini beradi
  print(key,value)
#Demak siz bilan biroz dict bilan tanishib oldik keyingi darsda siz bilan kichik lug'at yaratamiz
  

