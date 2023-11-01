import menyular
import orqa_fon
import parollar_menejeri
def yangi_pin_uz():
    """Bu funksiya uzbek tilida karta pincod ini o'zgartiradi."""
    pin= orqa_fon.pin_orqa_uz()
    tasdiqlash =pin[1]
    new_pin=pin[0]
    if tasdiqlash == 1:
        print("Pinkod muvoffaqiyatli o'zgartirildi.")
        parollar_menejeri.parol_menejer(new_pin)
        menyular.uzbek()
    elif tasdiqlash == 2:
        orqa_fon.pin_orqa_uz()
    elif tasdiqlash == 3:
        menyular.uzbek()
def yangi_pin_eng():
    """Bu funksiya ingliz tilida karta pincod ini o'zgartiradi."""
    pin = orqa_fon.pin_orqa_eng()
    tasdiqlash = pin[1]
    new_pin = pin[0]

    if tasdiqlash == 1:
        print("PINCODE CHANGED SUCCESSFULLY")
        parollar_menejeri.parol_menejer(new_pin)
        menyular.inglizcha()
    elif tasdiqlash == 2:
        orqa_fon.pin_orqa_eng()
    else:
        menyular.inglizcha()
def yangi_pin_ru():
    """Bu funksiya rus tilida karta pincod ini o'zgartiradi."""
    pin = orqa_fon.pin_orqa_ru()
    tasdiqlash = pin[1]
    new_pin = pin[0]

    if tasdiqlash == 1:
        print("ПИН-КОД УСПЕШНО ИЗМЕНЕН.")
        parollar_menejeri.parol_menejer(new_pin)
        menyular.ruscha()
    elif tasdiqlash == 2:
        orqa_fon.pin_orqa_ru()
    else:
        menyular.ruscha()