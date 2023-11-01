from colorama import Fore,Style,Back
import  Naqd_pul_orqa_fon
import chekni_chiqarish
import ha_yoq
import Karta_Balans
import menyular
import Bankomat_main
def naqd_pul1():
    """Bu funksiya pulni kartada hamda bankomatda bor yoki yo'qligini tekshiradi.
    Uzbek tili"""
    bank=1000000
    Miqdor = Naqd_pul_orqa_fon.naqd_orqa_fon()
    if Miqdor == 1:
        if Karta_Balans.karta_balans()>500000/100+500000 and 505000<bank:
            Karta_Balans.karta_balans(yechish=500000)
            chekni_chiqarish.Tasdiqlash(500000)
            bank-=505000

        else:
            "Amal bajarilmadi yoki Plastik kartanggizda mablag' yetarli emas."

            tekshir = ha_yoq.ha_yoq_uz()
            if tekshir== 1:
                menyular.uzbek()
            else:
                Bankomat_main.boshlash()
    elif Miqdor == 2:
        if Karta_Balans.karta_balans()>300000/100+300000 and 303000<bank:
            Karta_Balans.karta_balans(yechish=303000)
            chekni_chiqarish.Tasdiqlash(300000)
            bank -= 303000

        else:
            "Amal bajarilmadi yoki Plastik kartanggizda mablag' yetarli emas."

            tekshir = ha_yoq.ha_yoq_uz()
            if tekshir== 1:
                menyular.uzbek()
            else:
                Bankomat_main.boshlash()

    elif Miqdor == 3:
        if Karta_Balans.karta_balans()>101000 and bank>101000:
            Karta_Balans.karta_balans(yechish=101000)
            chekni_chiqarish.Tasdiqlash(100000)
            bank -= 101000

        else:
            "Amal bajarilmadi yoki Plastik kartanggizda mablag' yetarli emas."

            tekshir = ha_yoq.ha_yoq_uz()
            if tekshir== 1:
                menyular.uzbek()
            else:
                Bankomat_main.boshlash()
    elif Miqdor == 4:
        if Karta_Balans.karta_balans()>50500 and bank>50500:
            Karta_Balans.karta_balans(yechish=50500)
            chekni_chiqarish.Tasdiqlash(50000)
            bank -=50500

        else:
            "Amal bajarilmadi yoki Plastik kartanggizda mablag' yetarli emas."

            tekshir = ha_yoq.ha_yoq_uz()
            if tekshir== 1:
                menyular.uzbek()
            else:
                Bankomat_main.boshlash()
    elif Miqdor == 5:
        if Karta_Balans.karta_balans()>20200 and bank>20200:
            Karta_Balans.karta_balans(yechish=20200)
            chekni_chiqarish.Tasdiqlash(20000)
            bank -= 20000

        else:
            "Amal bajarilmadi yoki Plastik kartanggizda mablag' yetarli emas."

            tekshir = ha_yoq.ha_yoq_uz()
            if tekshir== 1:
                menyular.uzbek()
            else:
                Bankomat_main.boshlash()
    elif Miqdor == 6:

        boshqa_summa = int(input(f"""
        {Fore.YELLOW + Back.BLACK} Minimal summa ming UZS( pul miqdroni kiritiganda oxtiri 3 ta 0 bilan tugashi kerak aks xolada datur ishlamaydi.) {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} PUL MIQDORINI KIRITING => {Style.RESET_ALL}"""))
        if Karta_Balans.karta_balans()>boshqa_summa/100+boshqa_summa and boshqa_summa<bank:
            Karta_Balans.karta_balans(yechish=boshqa_summa/100+boshqa_summa)
            chekni_chiqarish.Tasdiqlash(boshqa_summa)
            bank -= boshqa_summa
        else:
            print("Amal bajarilmadi.Bankomatda  yoki Plastik kartanggizda mablag' yetarli emas.")
            tekshir = ha_yoq.ha_yoq_uz()
            if tekshir== 1:
                menyular.uzbek()
            else:
                Bankomat_main.boshlash()
    else:
        "Xatolik"
        naqd_pul1()
                                           #RUS TILI
def naqd_pul_ru():
    """Bu funksiya pulni kartada hamda bankomatda bor yoki yo'qligini tekshiradi.
        Rus tili"""
    bank = 1000000
    miqdor = Naqd_pul_orqa_fon.naqd_orqa_fon_ru()
    if miqdor == 1:
        if Karta_Balans.karta_balans()>500000/100+500000 and 505000<bank:
            Karta_Balans.karta_balans(yechish=500000)
            chekni_chiqarish.Tasdiqlash1(500000)
            bank -=505000
        else:
            "Операция не была завершена или на Вашей Пластиковой карте недостаточно средств."
            tekshir =ha_yoq.ha_yoq_ru()

            if tekshir== 1:
                menyular.ruscha()
            else:
                Bankomat_main.boshlash()
    elif miqdor == 2:

        if Karta_Balans.karta_balans()>300000/100+300000 and 303000<bank:
            Karta_Balans.karta_balans(yechish=303000)
            chekni_chiqarish.Tasdiqlash1(300000)
            bank -=303000
        else:
            "Операция не была завершена или на Вашей Пластиковой карте недостаточно средств."
            tekshir =ha_yoq.ha_yoq_ru()

            if tekshir== 1:
                menyular.ruscha()
            else:
                Bankomat_main.boshlash()

    elif miqdor == 3:

        if Karta_Balans.karta_balans()>100000/100+100000 and 101000<bank:
            Karta_Balans.karta_balans(yechish=101000)
            chekni_chiqarish.Tasdiqlash1(100000)
            bank -=101000
        else:
            "Операция не была завершена или на Вашей Пластиковой карте недостаточно средств."
            tekshir =ha_yoq.ha_yoq_ru()

            if tekshir== 1:
                menyular.ruscha()
            else:
                Bankomat_main.boshlash()

    elif miqdor == 4:

        if Karta_Balans.karta_balans()>50000/100+50000 and 50500<bank:
            Karta_Balans.karta_balans(yechish=50500)
            chekni_chiqarish.Tasdiqlash1(50000)
            bank -=50500
        else:
            "Операция не была завершена или на Вашей Пластиковой карте недостаточно средств."
            tekshir =ha_yoq.ha_yoq_ru()

            if tekshir== 1:
                menyular.ruscha()
            else:
                Bankomat_main.boshlash()


    elif miqdor == 5:

        if Karta_Balans.karta_balans()>20000/100+20000 and 20200<bank:
            Karta_Balans.karta_balans(yechish=20200)
            chekni_chiqarish.Tasdiqlash1(20000)
            bank -=20200
        else:
            "Операция не была завершена или на Вашей Пластиковой карте недостаточно средств."
            tekshir =ha_yoq.ha_yoq_ru()

            if tekshir== 1:
                menyular.ruscha()
            else:
                Bankomat_main.boshlash()
    elif miqdor == 6:
        boshqa_summa = int(input(f"""
        {Fore.YELLOW + Back.BLACK} Минимальная сумма – одна тысяча сум (при вводе суммы денег она должна заканчиваться 3 нулями, иначе компьютер не будет работать.) {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} ВВЕДИТЕ СУММУ ДЕНЕГ => {Style.RESET_ALL}"""))

        if Karta_Balans.karta_balans() > boshqa_summa / 100 + boshqa_summa and boshqa_summa < bank:
            Karta_Balans.karta_balans(yechish=boshqa_summa / 100 + boshqa_summa)
            chekni_chiqarish.Tasdiqlash1(boshqa_summa)
            bank -= boshqa_summa
        else:
            print("Действие не выполнено Недостаточно средств в банкомате или на Вашей Пластиковой карте.")
            tekshir = ha_yoq.ha_yoq_ru()
            if tekshir == 1:
                menyular.ruscha()
            else:
                Bankomat_main.boshlash()
    else:
        "ОШИБКА"
        naqd_pul_ru()
                                        #INGLIZ TILI
def naqd_pul_eng():
    """Bu funksiya pulni kartada hamda bankomatda bor yoki yo'qligini tekshiradi.
    Ingliz tili"""

    bank = 1000000
    miqdor = Naqd_pul_orqa_fon.naqd_orqa_eng()
    if miqdor == 1:
        if Karta_Balans.karta_balans() > 500000 / 100 + 500000 and 505000 < bank:
            Karta_Balans.karta_balans(yechish=500000)
            chekni_chiqarish.Tasdiqlash2(500000)
            bank -= 505000
        else:
            "The operation was not completed or there are not enough funds on your Plastic Card."
            tekshir = ha_yoq.ha_yoq_eng()

            if tekshir == 1:
                menyular.inglizcha()
            else:
                Bankomat_main.boshlash()
    elif miqdor == 2:

        if Karta_Balans.karta_balans()>300000/100+300000 and 303000<bank:
            Karta_Balans.karta_balans(yechish=303000)
            chekni_chiqarish.Tasdiqlash2(300000)
            bank -=303000
        else:
            "The operation was not completed or there are not enough funds on your Plastic Card."
            tekshir =ha_yoq.ha_yoq_eng()

            if tekshir== 1:
                menyular.inglizcha()
            else:
                Bankomat_main.boshlash()
    elif miqdor == 3:

        if Karta_Balans.karta_balans()>100000/100+100000 and 101000<bank:
            Karta_Balans.karta_balans(yechish=101000)
            chekni_chiqarish.Tasdiqlash2(100000)
            bank -=101000
        else:
            "The operation was not completed or there are not enough funds on your Plastic Card."
            tekshir =ha_yoq.ha_yoq_eng()

            if tekshir== 1:
                menyular.inglizcha()
            else:
                Bankomat_main.boshlash()
    elif miqdor == 4:

        if Karta_Balans.karta_balans()>50000/100+50000 and 50500<bank:
            Karta_Balans.karta_balans(yechish=50500)
            chekni_chiqarish.Tasdiqlash2(50000)
            bank -=50500
        else:
            "The operation was not completed or there are not enough funds on your Plastic Card."
            tekshir =ha_yoq.ha_yoq_eng()

            if tekshir== 1:
                menyular.inglizcha()
            else:
                Bankomat_main.boshlash()
    elif miqdor == 5:

        if Karta_Balans.karta_balans()>20000/100+20000 and 20200<bank:
            Karta_Balans.karta_balans(yechish=20200)
            chekni_chiqarish.Tasdiqlash2(20000)
            bank -=20200
        else:
            "The operation was not completed or there are not enough funds on your Plastic Card."
            tekshir =ha_yoq.ha_yoq_eng()

            if tekshir== 1:
                menyular.inglizcha()
            else:
                Bankomat_main.boshlash()
    elif miqdor == 6:
        boshqa_summa = int(input(f"""
        {Fore.YELLOW + Back.BLACK} The minimum amount is one thousand soums (when entering an amount of money, it must end with 3 zeros, otherwise the computer will not work.) {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} ENTER AMOUNT OF MONEY => {Style.RESET_ALL}"""))
        # CREATED BY ZAFARBEK
        if Karta_Balans.karta_balans() > boshqa_summa / 100 + boshqa_summa and boshqa_summa < bank:
            Karta_Balans.karta_balans(yechish=boshqa_summa / 100 + boshqa_summa)
            chekni_chiqarish.Tasdiqlash2(boshqa_summa)
            bank -= boshqa_summa
        else:
            print("The operation was not completed or there are not enough funds on your Plastic Card.")
            tekshir = ha_yoq.ha_yoq_eng()
            if tekshir == 1:
                menyular.inglizcha()
            else:
                Bankomat_main.boshlash()
    else:
        "ERROR"
        naqd_pul_eng()
