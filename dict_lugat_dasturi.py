#Aytgan vadamdagidek demak lug'at dasturini tuzishni boshlaymiz.
#Aytgan vadamdagidek demak lug'at dasturini tuzishni boshlaymiz.
lugtalar={
	"hello":"salom",
	"world":"dunyo",
	"programmer":"dasturchi",
	"computer":"kompyuter",
	"keyboards":"tugmalar",
	"hands":"qo'llar",
	"I":"Men",
	"You":"Sen",
	"We":"Biz",
	"They":"Ular",
	"He":"U(o'g'il bolaga nisbatan)",
	"She":"U(qiz bolga nisbatan)",
	"It":"U(Jonsiz narsalar va hayvonlarga nisbatan)",
	"Like":"Yoqtirmoq",
	"Runner":"Yuguruvchi",
	"Grab":"Uzmoq",
	"Hi there":"Salom",
	"Interesting":"Qiziqarli",
	"Fly":"Uchmoq",
	"In":"Ichida",
	"Sky":"Osmon",
	"a":"Noaniq artikl",
	"an":"Noqaniq artikl",
	"nature":"Tabiat",
	"birthday":"Tug'ilgan kun",
	"cake":"tort",
	"body":"tana",
	"track":"yuk mashina",
	"car":"mashina",
	"limusian":"limuzin",
	"wise":"1)Dono 2)Aqlli",
	"clever":"Aqlli",


}
#Mana royhatni to'ldirdik endi inputga o'tamiz
print("Salom men lug'atvoyman mendan foydalanishing mumkin.")
soz=str(input("Soz kiritishing mumkin:"))
while soz=="" or soz==" " or soz=="  " or soz=="   ":
    print("Soz xato!!!")
    soz=str(input("Sozni boshqattan kiriting:"))
    
#print(lugatlar[soz]) # Bu usul noto'g'ri chunki bu usuldan foydalanganda foydalanuvchi royhatda yo'q narsani kiritishi mumkin unda nima bo'ladi.Unda KeyError xatoligi yuz beradi.Buni oldin olish uchun get() funksiyasida foydalanamiz
print(lugatlar.get(soz,"Bunday so'z topilmadi!!!"))
