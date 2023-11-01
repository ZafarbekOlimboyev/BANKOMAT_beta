import orqa_fon
import Karta_Balans
import menyular

def sms_xabar_uz():
    qiymatlar = orqa_fon.sms_orqa_fon()
    tasdiqlash = qiymatlar[1]
    new_number = qiymatlar [0]
    if tasdiqlash == 1:
        print("MUVOFFAQIYATLI O'ZGARTIRILDI.")
        Karta_Balans.sms_xabarnoma(new_number)
        menyular.uzbek()
    elif tasdiqlash == 2:
        orqa_fon.sms_orqa_fon()
    elif tasdiqlash == 3:
        menyular.uzbek()
    else :
        print("Xatolik!!!!")
        sms_xabar_uz()
def sms_xabar_ru():
    qiymatlar= orqa_fon.sms_orqa_ru()
    tasdiqlash=qiymatlar[1]
    new_number=qiymatlar[0]

    if tasdiqlash == 1:
        print("НОМЕР УСПЕШНО ИЗМЕНЕН.")

        Karta_Balans.sms_xabarnoma(new_number)
        menyular.ruscha()
    elif tasdiqlash == 2:
        orqa_fon.sms_orqa_ru()
    elif tasdiqlash == 3:
        menyular.ruscha()
    else:
        print("Ошибка")
        sms_xabar_ru()
def sms_xabar_eng():
    qiymatlar = orqa_fon.sms_orqa_eng()
    tasdiqlash = qiymatlar[1]
    new_number = qiymatlar[0]

    if tasdiqlash == 1:
        print("NUMBER CHANGED SUCCESSFULLY")
        Karta_Balans.sms_xabarnoma(new_number)
        menyular.inglizcha()
    elif tasdiqlash == 2:
        orqa_fon.sms_orqa_eng()
    elif tasdiqlash == 3:
        menyular.inglizcha()
    else:
        print("Error")
        sms_xabar_eng()