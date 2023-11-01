import chek
import Naqd_pul_orqa_fon
import ha_yoq
import naqd_pul
import Bankomat_main
import menyular
import Pul_beta
def Tasdiqlash(summa):
    """
     Bu funksiya naqd pul olish funksiyasida tanlangan miqdorni chekini hciqarib beradi hamda
     boshqa xizmat bormi yoqmi shuni so'raydi.
     Uzbek tili
    """
    keylar=Naqd_pul_orqa_fon.miqdor_1(summa)
    summa=keylar[1]
    tasdiqlash=keylar[0]
    if tasdiqlash == 1:
        print(chek.chekuz(summa))
        print(Pul_beta.pul_beta_uz(summa,"uz","uz1"))
        def tekshir():
            tekshirish = ha_yoq.ha_yoq_uz()

            if tekshirish == 1:
                menyular.uzbek()
            elif tekshirish == 2:
                print("""
                      _____________________________________________________________________________________________________________________________
                       :)
                      """)
                Bankomat_main.boshlash()
            else:
                print("Xatolik")
                tekshir()
        tekshir()

    elif tasdiqlash == 2:
        naqd_pul.naqd_pul1()
    elif tasdiqlash == 3:
        menyular.uzbek()
        # CREATED BY ZAFARBEK
def Tasdiqlash1(summa):
    """
         Bu funksiya naqd pul olish funksiyasida tanlangan miqdorni chekini hciqarib beradi hamda
         boshqa xizmat bormi yoqmi shuni so'raydi.
         Rus tili
        """
    keylar=Naqd_pul_orqa_fon.miqdor_2(summa)
    summa =keylar[1]
    tasdiqlash=keylar[0]

    if tasdiqlash == 1:
        print(chek.chekru(summa))
        print(Pul_beta.pul_beta_uz(summa,"ru","ru1"))
        def tekshir():

            tekshirish=ha_yoq.ha_yoq_ru()
            if tekshirish == 1:
                menyular.ruscha()
            elif tekshirish == 2:
                print("""
                _____________________________________________________________________________________________________________________________
                :)
                """)
                Bankomat_main.boshlash()
            else:
                print("Ошибка")
                tekshir()
        tekshir()
    elif tasdiqlash == 2:
        naqd_pul.naqd_pul_ru()
    elif tasdiqlash == 3:
        menyular.ruscha()
def Tasdiqlash2(summa):
    """
         Bu funksiya naqd pul olish funksiyasida tanlangan miqdorni chekini hciqarib beradi hamda
         boshqa xizmat bormi yoqmi shuni so'raydi.
         Ingliz tili
        """
    keylar = Naqd_pul_orqa_fon.miqdor_3(summa)
    summa = keylar[1]
    tasdiqlash = keylar[0]

    if tasdiqlash == 1:
        print(chek.chekeng(summa))
        print(Pul_beta.pul_beta_uz(summa,"eng","eng1"))
        def tekshir():

            tekshirish = ha_yoq.ha_yoq_eng()
            if tekshirish == 1:
                menyular.inglizcha()
            elif tekshirish == 2:
                 print("""
                    _____________________________________________________________________________________________________________________________
                    :)
                    """)
                 Bankomat_main.boshlash()
            else:
                print("Error")
                tekshir()
        tekshir()
    elif tasdiqlash == 2:
        naqd_pul.naqd_pul_eng()
    elif tasdiqlash == 3:
        menyular.inglizcha()