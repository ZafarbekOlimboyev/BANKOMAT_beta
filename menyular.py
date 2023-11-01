import orqa_fon
import parollar_edit
import Bankomat_main
import smsxabarnoma
import Karta_Balans
import naqd_pul
def uzbek():
    """
    Bu funksiya Uzbek tili xizmatlarini chiqarib beradi hamda tanlangan xizmatga dasturni yo'naltiradi
    """
    password = orqa_fon.xizmatlar_fon_uz()
    if password == 1:
        parollar_edit.yangi_pin_uz()
    elif password == 2:
        naqd_pul.naqd_pul1()
    elif password == 3:
        print("Balans :",Karta_Balans.karta_balans())

        uzbek()
    elif password == 4:
        smsxabarnoma.sms_xabar_uz()
    elif password == 5:
        print("Xizmatlarimizdan foydalanganinggiz uchun raxmat.")
        print("""
        _______________________________________________________________________________
        """)
        Bankomat_main.boshlash()
    else:
        print("Xatolik!!!")
        Bankomat_main.boshlash()
def ruscha():
    """
        Bu funksiya Rus tili xizmatlarini chiqarib beradi hamda tanlangan xizmatga dasturni yo'naltiradi
        """
    password = orqa_fon.xizmatlar_fon_ru()
    if password == 1:
        parollar_edit.yangi_pin_ru()
    elif password == 2:
        naqd_pul.naqd_pul_ru()
    elif password == 3:
        print("Баланс :",Karta_Balans.karta_balans())
        ruscha()
    elif password == 4:
        print("You are Clever")
    elif password ==5:
        print("THANK YOU FOR USING OUR SERVICES.")
        print("""
        _______________________________________________________________________________
        """)
        Bankomat_main.boshlash()

# CREATED BY ZAFARBEK
    else:
        print("Ошибка!!!")
        Bankomat_main.boshlash()
def inglizcha():
    """
        Bu funksiya Ingliz tili xizmatlarini chiqarib beradi hamda tanlangan xizmatga dasturni yo'naltiradi
        """
    password = orqa_fon.xizmatlar_fon_eng()
    if password == 1:
        parollar_edit.yangi_pin_eng()
    elif password == 2:
        naqd_pul.naqd_pul_eng()
    elif password == 3:

        print("Balance :",Karta_Balans.karta_balans())

        inglizcha()
    elif password == 4:
        print("Whatcha doing?")
    elif password ==5:
        print("THANK YOU FOR USING OUR SERVICES.")
        print("""
        _______________________________________________________________________________
        """)
        Bankomat_main.boshlash()
    else:
        print("Error!!!")
        Bankomat_main.boshlash()