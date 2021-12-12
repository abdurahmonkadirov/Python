#funksiya yaraish
def salom_ber():
  print('Assalomu alykum!')
salom_ber()
#Bu Assalomu alaykum! ni qaytaradi
#Endi parametr deganini nima-yu argument nima?
#paramer bu funksiya berilgan o'zgaruvchi
def salom_ber(ism): #Ism parametr yani funksiyaga berilgan o'zgaruvchi
  print("Assalomu alaykum ",end='')
  return ism
#Assalomu alaykum ism deb qaytaradi.Faqat funsiyani ishlatayotgan payt mana bunday ishlatish kerak salom_ber('Abdurahmon') chunki bu argument qabul qiladigan funksiya.

