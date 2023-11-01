from colorama import Style, Back, Fore
import parollar as p
def uzbekcha():
    """Bu funksiya Bankomatniuzbek tiliga o'tiradi"""
    p.parol_uz()
def ruscha():
    p.parol_ru()
def inglizcha():
    p.parol_eng()
#CREATED BY ZAFARBEK

def boshlash():
    """
    Bu funksiya orqali til tanlanadi.
    """

    til = int(input(f"""                               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}
                               {Fore.YELLOW + Back.BLACK} | Tilni tanlang: | {Style.RESET_ALL}
                               {Fore.YELLOW + Back.BLACK} |----------------| {Style.RESET_ALL}

     {Fore.YELLOW + Back.BLACK} |---------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |---------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |---------------| {Style.RESET_ALL}        
     {Fore.YELLOW + Back.BLACK} |   1.O'ZBEK    | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   2.ENGLISH   | {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |   3.РУССЛИЙ   | {Style.RESET_ALL}
     {Fore.YELLOW + Back.BLACK} |---------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |---------------| {Style.RESET_ALL}       {Fore.YELLOW + Back.BLACK} |---------------| {Style.RESET_ALL}


     {Fore.YELLOW + Back.BLACK} => :{Style.RESET_ALL} """))
    if til == 1:
        uzbekcha()
    elif til == 2:
        inglizcha()
    elif til == 3:
        ruscha()
    else:
        print(f"{Fore.YELLOW + Back.BLACK}Siz mavjud bo'lmagan amalni kiritidnggiz{Style.RESET_ALL}")
        boshlash()

if __name__ == "__main__":
    print(f"""
    {Fore.YELLOW + Back.BLACK}Assalomu Alaykum.                     {Style.RESET_ALL}
    {Fore.YELLOW + Back.BLACK}                                      {Style.RESET_ALL}
    {Fore.YELLOW + Back.BLACK}Kartangizni kiriting  =>>             {Style.RESET_ALL}""")
    boshlash()