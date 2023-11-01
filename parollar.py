import Bankomat_main as main
import menyular
import parollar_menejeri as pm
from colorama import Fore, Back, Style
def parol_uz():
    """Bu funksiya Uzbek tilida parolni so'rash va tasdiqlash uchun ishlatiladi. Parol kitritiladi va uni tekshiradi agar to'g'ri bo'lsa
    keyingi menyuga o'kazadi aks holda boshiga qaytarib qo'yadi."""
    n=2
    while n>=0 :
        kod=int(input(f"""
    {Fore.YELLOW + Back.BLACK}  Pinkodni kiriting =>   {Style.RESET_ALL}"""))

        if kod == pm.parol_menejer():
            n= -100
            menyular.uzbek()
        elif n>0:
            n -=1
        elif n == 0:
            print("""
            Siz ko'p marotaba kodni xato kiritdingiz shu sababdan kartangiz bankomatda qoladi.
            """)
            print("""
            _______________________________________________________________________________________________________
            """)
            main.boshlash()
def parol_ru():
    """Bu funksiya Rus tilida parolni so'rash va tasdiqlash uchun ishlatiladi. Parol kitritiladi va uni tekshiradi agar to'g'ri bo'lsa
        keyingi menyuga o'kazadi aks holda boshiga qaytarib qo'yadi."""
    n=2
    while n>=0 :
        kod=int(input(f"""
    {Fore.YELLOW + Back.BLACK}  ВВЕДИТЕ ПИН-код =>   {Style.RESET_ALL}"""))

        if kod == pm.parol_menejer():
            n= (-1000)
            menyular.ruscha()
        elif n>0:
            n -=1
        elif n == 0:
            print("""
            ВЫ ВВЕДИЛИ КОД СЛИШКОМ МНОГО РАЗ. ПОЭТОМУ ПЛАСТИКОВАЯ КАРТА ОСТАЕТСЯ В БАНКОМАТЕ.""")
            print("""
            _______________________________________________________________________________________________________
            """)
            main.boshlash()
def parol_eng():
    n=2
    while n>=0 :
        kod=int(input(f"""
    {Fore.YELLOW + Back.BLACK}  INPUT PINCODE =>   {Style.RESET_ALL}"""))

        if kod == pm.parol_menejer():
            n= (-100)
            menyular.inglizcha()
        elif n>0:
            n -=1
        elif n == 0:
            print("""
            YOU HAVE ENTERED THE PIN CODE TOO MANY TIMES. THIS IS WHY THE CARD REMAINS IN THE ATM.""")
            print("""
            _______________________________________________________________________________________________________
            """)
            main.boshlash()