from colorama import Fore,Style,Back

def ha_yoq_uz():
    """
    Bu funksiya xizmatlar oxirida boshqa xizmat bormi yo'qmi shuni so'raydi.
    Uzbek tili"""
    ha_yo=int(input(f"""
     
                    {Fore.YELLOW + Back.BLACK} XIZMATLARIMIZDAN FOYDALANGANINGGIZ UCHUN RAXMAT                                  {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} BOSHQA XIZMATLAR BORMI?                                                          {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} 1.HA                                                                             {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} 2.YO`Q                                                                           {Style.RESET_ALL}  
                    {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}"""))
    return ha_yo
def ha_yoq_ru():
    """
        Bu funksiya xizmatlar oxirida boshqa xizmat bormi yo'qmi shuni so'raydi.
        Rus tili"""
    ha_yo= (int(input(f"""

       {Fore.YELLOW + Back.BLACK} ЕСТЬ ДРУГИЕ УСЛУГИ?                                                              {Style.RESET_ALL} 
       {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
       {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
       {Fore.YELLOW + Back.BLACK}                                                                                  {Style.RESET_ALL} 
       {Fore.YELLOW + Back.BLACK} 1.ДА                                                                                 {Style.RESET_ALL} 
       {Fore.YELLOW + Back.BLACK} 2.НЕТ                                                                                 {Style.RESET_ALL} 
       {Fore.YELLOW + Back.BLACK}  =>  {Style.RESET_ALL} 
       """)))
    return ha_yo
#CREATED BY ZAFARBEK
def ha_yoq_eng():
    """
        Bu funksiya xizmatlar oxirida boshqa xizmat bormi yo'qmi shuni so'raydi.
        Ingliz tili"""
    ha_yo=(int(input(f"""
            {Fore.YELLOW + Back.BLACK} THANK YOU FOR USING OUR SERVICES                                                 {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} ARE THERE OTHER SERVICES?                                                          {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 1.YES                                                                             {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} 2.NO                                                                           {Style.RESET_ALL}  
            {Fore.YELLOW + Back.BLACK} => {Style.RESET_ALL}""")))
    return ha_yo