
import random

spisokslov = """time way year work government day man world life part house course case system place end group company party information school fact money point
example state business night area water thing family head hand order john side home development week power country council
use service room market problem court lot war police interest car law road form face education policy research sort office
body person health mother question period name book level child control society minister view door line community south
city god father centre effect staff position kind job woman action management act process north age evidence idea west support
moment sense report mind church morning death change industry land care century range table back trade history study street"""
slovabesprobels=spisokslov.split()
slovo=random.choice(slovabesprobels)
print(slovo)
procherk = []
lives = 5
spisok_bykv = []
print('Здравствуйте, это мего-супер крутая игра висилица, чтобы выиграть в ней нужно: \n1.сейчас вам распечатается прочерки , вам угадать слово. \n Делаетя это следующим оброзом:\n вы вписываете букву и слово постепено заполняется буквами \n, но не торопитесь писать весь алфавит ведь попыток всеволишь 5.УДАЧИ!!!!\n Угадываем только английские слова.')
alfavit =['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
cifra = ['1','2','3','4','5','6','7','8','9','0']
russia_alfavit = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']

for i in range(len(slovo)):
    procherk.append('-')
while lives >= 1:
    print(*procherk)
    bykva= input('введите букву: ')
#    if bykva in alfavit or bykva in cifra :
#        print('эй, мы так не договаривались')
#        continue
    if bykva.isdigit() or bykva.isupper() or bykva in russia_alfavit:  #проверка перем.bykva на число или реистор
        print('эй, можно вводить только маленькие английские буквы')
        continue
    if len(bykva) > 1:
        print('ошибка, введите только одну букву!!!!')
        continue
    if bykva in spisok_bykv:
        print('хм, гдето это я уже видел')
        continue
    spisok_bykv.append(bykva)
    if bykva in slovo:
        procherk_str = ''
        for i in range (len(slovo)):   # проходим по буквам в слове
            if bykva == slovo[i]:   # if буква в слове = введенной букве
                procherk[i] = bykva  #  заменяем прочерки на буквы
        print('молодец, ты угадал ')
        for el in procherk:
            procherk_str += el
        if procherk_str == slovo:
            print(*procherk)
            print('Поздровляем вас с выигрошом!')
            break
    else:
        lives -= 1
        print('осталось жизней:',lives)
        if lives ==  0:
            print('жизни закончились, ВЫ ПРОИГРАЛИ')
            break



