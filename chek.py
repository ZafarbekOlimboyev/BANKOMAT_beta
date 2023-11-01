import Karta_Balans
def chek_uz(summa):
    """Bu funksiya kiritilgan pulni foiz hamda kartadan yechib olinadigan summani chiqarib beradi.
    Uzbek tili"""
    if 1000000<=summa<=9999000:

        chek = (f"""    
        _______________________________________
        |                                     |
        |   SUMMA : {summa} GA TENG.          |
        |   FOIZ : {summa / 100}                    |
        |   JAMI : {summa + summa / 100}                  | 
        |                                     |
        ---------------------------------------
        """)
        return chek
    elif 100000<=summa<=999000:
        def chek1(summa):
            chek = (f"""    
            _______________________________________
            |                                      |
            |   SUMMA : {summa} GA TENG.            |
            |   FOIZ : {summa / 100}                      |
            |   JAMI : {summa + summa / 100}                    | 
            |                                      |
            ---------------------------------------
            """)
            return chek
        return chek1(summa)

    elif 10000<=summa<=99000:

        chek = (f"""    
        _______________________________________
        |                                     |
        |   SUMMA : {summa} GA TENG.            |
        |   FOIZ : {summa / 100}                      |
        |   JAMI : {summa + summa / 100}                    | 
        |                                     |
        ---------------------------------------
        """)
        return chek
    else:

        chek = (f"""    
        _______________________________________
        |                                     |
        |   SUMMA : {summa} GA TENG.             |
        |   FOIZ : {summa / 100}                       |
        |   JAMI : {summa + summa / 100}                     | 
        |                                     |
        ---------------------------------------
        """)
        return chek
def chekuz(summa):
    """ Bu funksiya olingan pulni chekini chiqarib beradi
    Uzbek tilida"""
    if 100000<=summa<=999900:
        chek=(f"""
        _______________________________________
        |            CHEK:                    |
        |   SUMMA : {summa} GA TENG.           |
        |   FOIZ : {summa/100}                     |
        |   JAMI : {summa+summa/100}                   |  
        |   KARTA: 9860********6796           |
        |   KARTADA QOLGAN SUMMA: {Karta_Balans.karta_balans(yechish=summa+summa/100)}    |
        ---------------------------------------
        """)
        return chek
    elif 10000<=summa<=99000:

        chek=(f"""
        _______________________________________
        |            CHEK:                    |
        |   SUMMA : {summa} GA TENG.            |
        |   FOIZ : {summa/100}                      | 
        |   JAMI : {summa+summa/100}                    |   
        |   KARTA: 9860********6796           |
        |   KARTADA QOLGAN SUMMA: {Karta_Balans.karta_balans(yechish=summa+summa/100)}    |     
        ---------------------------------------
        """)
        return chek
    elif 1000<=summa<=9000:


        chek=(f"""
        _______________________________________
        |            CHEK:                    |
        |   SUMMA : {summa} GA TENG.             |
        |   FOIZ : {summa/100}                       | 
        |   JAMI : {summa+summa/100}                     |   
        |   KARTA: 9860********6796           |
        |   KARTADA QOLGAN SUMMA: {Karta_Balans.karta_balans(yechish=summa+summa/100)}    |     
        ---------------------------------------""")
        return chek
                                     #RUS TILI
def chek_ru(summa):
    if 100000<=summa<=999000:
        chek=(f"""
                   _______________________________________
                   |                                     |  
                   |   ДЕНЬГИ: {summa}                    |
                   |   ПРОЦЕНТ : {summa / 100}                  |
                   |   ОБЩИЙ : {summa + summa / 100}                  |
                   |                                     |
                   ---------------------------------------
                   """)
        return chek
    elif 10000<=summa<=99000:

        chek=(f"""
                   _______________________________________
                   |                                     |  
                   |   ДЕНЬГИ: {summa}                     |
                   |   ПРОЦЕНТ : {summa / 100}                   |
                   |   ОБЩИЙ : {summa + summa / 100}                   |
                   |                                     |
                   ---------------------------------------
                   """)
        return chek
    elif 1000<=summa<=9000:


        chek=(f"""
                   _______________________________________
                   |                                     |  
                   |   ДЕНЬГИ: {summa}                      |
                   |   ПРОЦЕНТ : {summa / 100}                    |
                   |   ОБЩИЙ : {summa + summa / 100}                    |
                   |                                     |
                   ---------------------------------------
                   """)
        return chek
    elif 1000000<=summa<=9999000:

        chek=(f"""
                   _______________________________________
                   |                                     |  
                   |   ДЕНЬГИ: {summa}                   |
                   |   ПРОЦЕНТ : {summa / 100}                 |
                   |   ОБЩИЙ : {summa + summa / 100}                 |
                   |                                     |
                   ---------------------------------------
                   """)
        print(chek)
def chekru(summa):
    """ Bu funksiya olingan pulni chekini chiqarib beradi
    Rus tili"""
    if 1000<=summa<=9000:
        chek=(f"""
           _______________________________________
           |            CHEK:                    |               
           |   ДЕНЬГИ  : {summa}                    |
           |   ПРОЦЕНТ : {summa/100}                    |    
           |   ОБЩИЙ : {summa+summa/100}                    |      
           |   КАРТА: 9860********6796           |
           |   ОСТАЛОСЬ ДЕНЕГ НА КАРТЕ: {Karta_Balans.karta_balans(yechish=summa+summa/100)}  | 
           ---------------------------------------
           """)
        return chek
    elif 10000<=summa<=99000:

        chek=(f"""
           _______________________________________
           |            CHEK:                    |               
           |   ДЕНЬГИ  : {summa}                   |
           |   ПРОЦЕНТ : {summa/100}                   |    
           |   ОБЩИЙ : {summa+summa/100}                   |      
           |   КАРТА: 9860********6796           |
           |   ОСТАЛОСЬ ДЕНЕГ НА КАРТЕ: {Karta_Balans.karta_balans(yechish=summa+summa/100)} | 
           ---------------------------------------
           """)
        return chek
    elif 100000<=summa<=999000:
        chek=(f"""
           _______________________________________
           |            CHEK:                    |               
           |   ДЕНЬГИ  : {summa}                  |
           |   ПРОЦЕНТ : {summa/100}                  |    
           |   ОБЩИЙ : {summa+summa/100}                  |      
           |   КАРТА: 9860********6796           |
           |   ОСТАЛОСЬ ДЕНЕГ НА КАРТЕ: {Karta_Balans.karta_balans(yechish=summa+summa/100)} | 
           ---------------------------------------
           """)
        return chek
    elif 1000000<=summa<=9999000:

        chek=(f"""
           _______________________________________
           |            CHEK:                    |               
           |   ДЕНЬГИ  : {summa}                 |
           |   ПРОЦЕНТ : {summa/100}                 |    
           |   ОБЩИЙ : {summa+summa/100}                 |      
           |   КАРТА: 9860********6796           |
           |   ОСТАЛОСЬ ДЕНЕГ НА КАРТЕ: {Karta_Balans.karta_balans(yechish=summa+summa/100)}| 
           ---------------------------------------
           """)
        return chek
                          #INGLIZ TILI
def chek_eng(summa):
    """Bu funksiya kiritilgan pulni foiz hamda kartadan yechib olinadigan summani chiqarib beradi."""
    if 1000<=summa<=9000:
        chek=(f"""
        _______________________________________
        |                                     |     
        |   THE SUM IS : {summa}                 |
        |   PERCENT : {summa/100}                    |
        |   TOTAL : {summa+summa/100}                    |  
        |                                     |
        ---------------------------------------
        """)
        return chek
    elif 10000<=summa<=99000:
        chek=(f"""
        _______________________________________
        |                                     |     
        |   THE SUM IS : {summa}                |
        |   PERCENT : {summa/100}                   |
        |   TOTAL : {summa+summa/100}                   |  
        |                                     |
        ---------------------------------------
        """)
        return chek
    elif 100000<=summa<=999000:

        chek=(f"""
        _______________________________________
        |                                     |     
        |   THE SUM IS : {summa}               |
        |   PERCENT : {summa/100}                  |
        |   TOTAL : {summa+summa/100}                  |  
        |                                     |
        ---------------------------------------
        """)
        return chek
    elif 1000000<=summa<=9999000:


        chek=(f"""
        _______________________________________
        |                                     |     
        |   THE SUM IS : {summa}              |
        |   PERCENT : {summa/100}                 |
        |   TOTAL : {summa+summa/100}                 |  
        |                                     |
        ---------------------------------------
        """)
        return chek
def chekeng(summa):
    """ Bu funksiya olingan pulni chekini chiqarib beradi
    Ingliz tilida"""
    if 1000<=summa<=9000:
        chek=(f"""
            _____________________________________________
            |            CHEK:                          |
            |   THE SUM IS  : {summa}                      |
            |   PERCENT : {summa/100}                          |   
            |   TOTAL : {summa+summa/100}                          |     
            |   CARD: 9860********6796                  |
            |   AMOUNT REMAINING ON THE CARD: {Karta_Balans.karta_balans(yechish=summa+summa/100)}  | 
            ---------------------------------------------
            """)
        return chek
    elif 10000<=summa<=99000:

        chek=(f"""
            _____________________________________________
            |            CHEK:                          |
            |   THE SUM IS  : {summa}                     |
            |   PERCENT : {summa/100}                         |   
            |   TOTAL : {summa+summa/100}                         |     
            |   CARD: 9860********6796                  |
            |   AMOUNT REMAINING ON THE CARD: {Karta_Balans.karta_balans(yechish=summa+summa/100)}  | 
            ---------------------------------------------
            """)
        return chek
    elif 100000<=summa<=999000:


        chek=(f"""
            _____________________________________________
            |            CHEK:                          |
            |   THE SUM IS  : {summa}                    |
            |   PERCENT : {summa/100}                        |   
            |   TOTAL : {summa+summa/100}                        |     
            |   CARD: 9860********6796                  |
            |   AMOUNT REMAINING ON THE CARD: {Karta_Balans.karta_balans(yechish=summa+summa/100)}  | 
            ---------------------------------------------
            """)
        return chek
    elif 1000000<=summa<=9999000:


        chek=(f"""
            ______________________________________________
            |            CHEK:                           |
            |   THE SUM IS  : {summa}                    |
            |   PERCENT : {summa/100}                        |   
            |   TOTAL : {summa+summa/100}                        |     
            |   CARD: 9860********6796                   |
            |   AMOUNT REMAINING ON THE CARD: {Karta_Balans.karta_balans(yechish=summa+summa/100)} | 
            ----------------------------------------------
            """)
        return chek