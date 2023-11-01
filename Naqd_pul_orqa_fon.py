from colorama import Fore,Back,Style
import chek

def naqd_orqa_fon():
    """Naqd pul olish miqdorlarni chiqarib beruvchi funksiya
    Uzbek tili"""
    uzs_miqdori = int(
        input(F"""                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |MIQDORNI KIRITING| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}

               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |   1.500 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.300 000    | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |   3.100 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |     4.50 000   | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |    5.20 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 6.BOSHQA SUMMA | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
    {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
    return uzs_miqdori
                                    #RUS TILI
def naqd_orqa_fon_ru():
    """Naqd pul olish miqdorlarni chiqarib beruvchi funksiya
    Rua tili"""

    uzs_miqdori = int(
        input(F"""                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |  ВВЕДИТЕ ДЕНЬГИ | {Style.RESET_ALL}
                            {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}

               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |   1.500 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.300 000    | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |   3.100 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |     4.50 000   | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL} 
               {Fore.YELLOW + Back.BLACK} |    5.20 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 6.ДРУГАЯ СУММА | {Style.RESET_ALL}
               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
    {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
    return uzs_miqdori
def naqd_orqa_eng():
    """Naqd pul olish miqdorlarni chiqarib beruvchi funksiya
    Ingliz tili"""
    uzs_miqdori = int(
        input(F"""                                {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}
                                {Fore.YELLOW + Back.BLACK} |   ENTER AMOUNT  | {Style.RESET_ALL}
                                {Fore.YELLOW + Back.BLACK} |-----------------| {Style.RESET_ALL}

                   {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
                   {Fore.YELLOW + Back.BLACK} |   1.500 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.300 000    | {Style.RESET_ALL}
                   {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                   {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL} 
                   {Fore.YELLOW + Back.BLACK} |   3.100 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |     4.50 000   | {Style.RESET_ALL}
                   {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


                   {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL} 
                   {Fore.YELLOW + Back.BLACK} |    5.20 000    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |6.ANOTHER AMOUNT| {Style.RESET_ALL}
                   {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
        {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
    return uzs_miqdori



def miqdor_1(summa):
    """Naqd pul olishni tasdiqlovchi funksiya
    Uzbek tili"""
    print(chek.chek_uz(summa))
    tasdiqlash = int(input(F"""
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} |  1.TASDIQLASH  | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.QAYTA KIRITISH| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} | 3.BEKOR QILISH | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


         {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
    return [tasdiqlash,summa]
def miqdor_2(summa):
    """Naqd pul olishni tasdiqlovchi funksiya
    Rus tili"""
    print(chek.chek_ru(summa))
    tasdiqlash = int(input(F"""
       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
       {Fore.YELLOW + Back.BLACK} | 1.ПОДТВЕРЖДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |2.ПОВТОРНОЕ ВВЕДЕНИЕ| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.ОТМЕНА    | {Style.RESET_ALL}
       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |--------------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


    {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
    return [tasdiqlash,summa]
def miqdor_3(summa):
    # CREATED BY ZAFARBEK
    """Naqd pul olishni tasdiqlovchi funksiya
    Ingliz tili"""
    print(chek.chek_eng(summa))
    tasdiqlash = int(input(f"""
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}        
            {Fore.YELLOW + Back.BLACK} | 1.CONFIRMATION | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.RE-ENTER   | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |    3.CENCEL    | {Style.RESET_ALL}
            {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}


         {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL}"""))
    return [tasdiqlash,summa]
#CREATED BY ZAFARBEK