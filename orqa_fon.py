from colorama import Fore,Back,Style
def xizmatlar_fon_uz():
    """Bu funksiya uzbekcha xizmatlar menyusini orqa foni"""
    menyu = int(input(f"""                            
                                {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}
                                {Fore.YELLOW + Back.BLACK} |Xizmtani tanlang:| {Style.RESET_ALL}
                                {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}

                   {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                   {Fore.YELLOW + Back.BLACK} |1.PINKODNI O'ZGARTIRITSH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.NAQD PUL OLISH     | {Style.RESET_ALL}
                   {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}


                   {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL} 
                   {Fore.YELLOW + Back.BLACK} |     3.KARTA BALANS     | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |     4.SMS XABARNOMA    | {Style.RESET_ALL}
                   {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}


                                     {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                                     {Fore.YELLOW + Back.BLACK} |  5.KARTANI CHIQARISH   | {Style.RESET_ALL}
                                     {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                    {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
    return menyu
def xizmatlar_fon_ru():
    """Bu funksiya ruscha xizmatlar menyusini orqa foni"""
    menyu = int(input(f"""                            
                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |ВЫБЕРИТЕ УСЛУГУ :| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}

               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |   1.ИЗМЕНЕНИЕ ПИНКОДА  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |      2.НАЛИЧНЫЕ        | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}


               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |     3.БАЛАНС КАРТЫ     | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   4.СМС-уведомление    | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}


                                 {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                                 {Fore.YELLOW + Back.BLACK} |     5.ВЫПУСК КАРТЫ     | {Style.RESET_ALL}
                                 {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
    return menyu
def xizmatlar_fon_eng():
    """Bu funksiya inglizcha xizmatlar menyusini orqa foni"""
    menyu = int(input(f"""                            
                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |SELECT A SERVICE:| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}

               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |   1.PINCODE CHANGE     | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |      2.GET CASH        | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}


               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |     3.CARD BALANCE     | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   4.SMS NOTIFICATION   | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}


                                 {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                                 {Fore.YELLOW + Back.BLACK} |     5.CARD ISSUING     | {Style.RESET_ALL}
                                 {Fore.YELLOW + Back.BLACK} |------------------------| {Style.RESET_ALL}
                {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
    return menyu #CREATED BY ZAFARBEK
def pin_orqa_uz():
    """Bu funksiya uzbek tilidagi xizmatlar menyusini pin codini o'zgartirish xizmatini orqa foni"""
    n = 1
    while True:
        yangikod = int(input(f"{Fore.YELLOW + Back.BLACK} YANGI PINCODNI KIRITING =>  {Style.RESET_ALL}"))
        if 1000 <= yangikod <= 9999:
            tasdiqlash = int(input(f"""
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |PINKOD O'ZGARTIRILSINMI? | {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}

            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} |      1.HA      | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
            break

        else:
            print("Pinkod 4 xonali bo'lishi kerak.")
    return [yangikod, tasdiqlash]
def pin_orqa_eng():
    """Bu funksiya ingliz tilidagi xizmatlar menyusini pin codini o'zgartirish xizmatini orqa foni"""

    n = 1
    while n > 0:
        yangikod = int(input(f"{Fore.YELLOW + Back.BLACK}  INSERT NEW PIN   =>  {Style.RESET_ALL}"))
        if 1000 <= yangikod <= 9999:
            tasdiqlash = int(input(f"""
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |      CHANGE PINCODE?    | {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}

            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} |     1.YES      | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.RE-INTRODUCTION| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   3.CENCEL     | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
            n = 0 #CREATED BY ZAFARBEK
            return [yangikod, tasdiqlash]
        else:
            print("PINCODE MUST BE 4 DIGITS.")
def pin_orqa_ru():
    """Bu funksiya rus tilidagi xizmatlar menyusini pin codini o'zgartirish xizmatini orqa foni"""

    n = 1
    while n > 0:
        yangikod = int(input(f"{Fore.YELLOW + Back.BLACK}  ВВЕДИТЕ НОВЫЙ ПИН-КОД   =>  {Style.RESET_ALL}"))
        if 1000 <= yangikod <= 9999:
            tasdiqlash = int(input(f"""
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |         ИЗМЕНЯТЬ?       | {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}

            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |---------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} |     1.ДА       | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2..ПОВТОРНОЕ ВВЕДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   3.ОТМЕНА     | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |---------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
            n = 0
        # CREATED BY ZAFARBEK
        else:
            print("ПИН-КОД ДОЛЖЕН БЫТЬ 4 ЦИФРЫ.")
    return [yangikod,tasdiqlash]
def sms_orqa_fon():
    """
    Smsxabarnoma funksiyasini orqa foni
    Uzbek tilida"""
    n = 1
    while n > 0:
        numbers = int(input(f"{Fore.YELLOW + Back.BLACK}  YANGI RAQAMNI KIRIING   => +998 : {Style.RESET_ALL}"))
        if 100000000 <= numbers <= 999999999:
            tasdiqlash = int(input(f"""
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} | RAQAM O'ZGARTIRILSINMI? | {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}

            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} |     1.HA       | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA  KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
            n=0
        else:
            print("TELEFON RAQAM 9 XONALI BO'LISHI KERAK.")
    return [numbers,tasdiqlash]
def sms_orqa_ru():
    """
        Smsxabarnoma funksiyasini orqa foni
        Rus tilida"""
    n = 1
    while n > 0:
        numbers = int(input(f"{Fore.YELLOW + Back.BLACK}  ВВЕДИТЕ НОВЫЙ НОМЕР   => +998 : {Style.RESET_ALL}"))
        if 100000000 <= numbers <= 999999999:
            tasdiqlash = int(input(f"""
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |      ИЗМЕНИТЬ НОМЕР?    | {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}

            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}      {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} |     1.ДА       | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK}|2.ПОВТОРНОЕ ВВЕДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   3.ОТМЕНА     | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK}|--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
            n = 0

        else:
            print("НОМЕР ДОЛЖЕН БЫТЬ 9 ЦИФР.")
    return [numbers,tasdiqlash]
def sms_orqa_eng():
    """
        Smsxabarnoma funksiyasini orqa foni
        Ingliz tilida"""
    n = 1
    while n > 0:
        numbers = int(input(f"{Fore.YELLOW + Back.BLACK}  ENTER NEW NUMBER   => +998 : {Style.RESET_ALL}"))
        if 100000000 <= numbers <= 999999999:
            tasdiqlash = int(input(f"""
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |       CHANGE NUMBER?    | {Style.RESET_ALL}
                                  {Fore.YELLOW + Back.BLACK} |-------------------------| {Style.RESET_ALL}

            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} |     1.YES      | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.RE-INTRODUCTION| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   3.CENCEL     | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
            n = 0
        else:
            print("NUMBER MUST BE 9 DIGITS.")
    return [numbers,tasdiqlash]
#CREATED BY ZAFARBEK
