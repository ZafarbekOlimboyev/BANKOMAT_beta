from colorama import Fore,Back,Style


def pul_beta_uz(summa,til,til1):
    print(f"{Fore.YELLOW + Back.BLACK}CHIQARILGAN PUL BIRLIKLARI : {Style.RESET_ALL}")
    print(f"{Fore.YELLOW + Back.BLACK}ВЫПУЩЕННЫЕ ВАЛЮТЫ :          {Style.RESET_ALL}")
    print(f"{Fore.YELLOW + Back.BLACK}CURRENCIES ISSUED :          {Style.RESET_ALL}")
    words= {"uz":"DONA",'uz1':'MINGLIK','eng':'PIECES FOR','eng1':'THOUSAND','ru':'ШТУК','ru1':
            'ТЫСЯЧ'}
    pul_1000=10
    pul_2000=10
    pul_5000=10
    pul_10000=7
    pul_20000=23
    pul_50000=12
    pul_100000=7
    pul_200000=5
    total=pul_200000*200000 + pul_100000*100000 + pul_50000 * 50000 + pul_20000 * 20000 + pul_10000 * 10000 + pul_5000 * 5000 + pul_2000 * 2000 + pul_1000 * 1000
    ikkiyuz=summa//200000
    yuz=(summa%200000)//100000
    ellik=((summa%200000)%100000)//50000
    yigirma = (((summa%200000)%100000)%50000)//20000
    on=((((summa%200000)%100000)%50000)%20000)//10000
    besh=(((((summa%200000)%100000)%50000)%20000)%10000)//5000
    ikki = ((((((summa%200000)%100000)%50000)%20000)%10000)%5000)//2000
    ming=(((((((summa%200000)%100000)%50000)%20000)%10000)%5000)%2000)//1000
    if summa%1000 ==0:
        if ikkiyuz>0 and ikkiyuz<=pul_200000:
            if yuz>0 and pul_100000>=yuz:
                if ellik>0 and pul_50000>=ellik:
                    if yigirma>0 and pul_20000>=yigirma:
                        if on >0 and pul_10000>=on:
                            if besh>0 and pul_5000>=besh:
                                if ikki >0 and pul_2000>=ikki:
                                    if ming >0 and pul_1000>=ming:
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}  {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}  {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni=(f"""
                                            {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                            {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                            {on} {words[til]} 10 {words[til1]}  {besh} {words[til]} 5 {words[til1]}
                                            {ikki} {words[til]} 2 {words[til1]}  
                                            """)
                                        return soni
                                else:
                                    if ming >0 and pul_1000>=ming:
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}  {besh} {words[til]} 5 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni=(f"""
                                            {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                            {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                            {on} {words[til]} 10 {words[til1]}  {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:
                                if ikki >0 and pul_2000>=ikki:
                                    if ming >0 and pul_1000>=ming:
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}  {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni=(f"""
                                            {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                            {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                            {on} {words[til]} 10 {words[til1]}  {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:
                                    if ming >0 and pul_1000>=ming:
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}   {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni=(f"""
                                            {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                            {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                            {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else:
                            if besh>0 and pul_5000>=besh:
                                if ikki >0 and pul_2000>=ikki:
                                    if ming >0 and pul_1000>=ming:
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}    {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}    {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:
                                    if ming >0 and pul_1000>=ming:
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}     {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:
                                if ikki >0 and pul_2000>=ikki:
                                    if ming >0 and pul_1000>=ming:
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}  {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:
                                    if ming >0 and pul_1000>=ming:
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                            """)
                                        return soni
                    else:  #20 minglik yo`q
                        if on >0 and pul_10000>=on:#10ming bor
                            if besh>0 and pul_5000>=besh: # besh mingik bor
                                if ikki >0 and pul_2000>=ikki: # ikki minglik bor
                                    if ming >0 and pul_1000>=ming: #minglik bor
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}    {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else: #minglik yo'q
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}    {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else: #ikki minglik yo'q
                                    if ming >0 and pul_1000>=ming: #minglik bor
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}  {ming} {words[til]} {words[til1]}
                                        
                                        """)
                                        return soni
                                    else: #minglik yo'q
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else: #5minglik yo'q
                                if ikki >0 and pul_2000>=ikki:# ikki minglik bor
                                    if ming >0 and pul_1000>=ming:#minglik bor
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}   {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:#minglik yo'q
                                        soni=(f"""
                                            {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else: # ikki minglik yo'q
                                    if ming >0 and pul_1000>=ming: #minglik bor
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:#minglik yo'q
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else: #10 minglik yo'q
                            if besh>0 and pul_5000>=besh:#5 minglik bor
                                if ikki >0 and pul_2000>=ikki: #2 minglik bor
                                    if ming >0 and pul_1000>=ming: #minglik bor
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}    {besh} {words[til]} 5 {words[til1]}   
                                        {ikki} {words[til]} 2 {words[til1]}      {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:#minglik yo'q
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}    {besh} {words[til]} 5 {words[til1]}   
                                        {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else: #2 minglik yo'q
                                    if ming >0 and pul_1000>=ming: #minglik bor
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}    {besh} {words[til]} 5 {words[til1]}   
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else: #minglik yo'q
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}    {besh} {words[til]} 5 {words[til1]}   
                                            """)
                                        return soni
                            else: #5 minglik yo'q
                                if ikki >0 and pul_2000>=ikki: #ikki minglik bor
                                    if ming >0 and pul_1000>=ming: #minglik bor
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}     {ikki} {words[til]} 2 {words[til1]} 
                                        {ming} {words[til]} {words[til1]}""")
                                        return soni
                                    else: #minglik yo'q
                                        soni=(f"""
                                            {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}     {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else: #ikki minglik yo'q
                                    if ming >0 and pul_1000>=ming: #minglik bor
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}    {ming} {words[til]} {words[til1]}""")

                                        return soni
                                    else: #minglik yo'q
                                        soni=(f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}
                                            """)
                                        return soni
                else:# 50minglik yo'q
                    if yigirma > 0 and pul_20000 >= yigirma: #20 minglik bor
                        if on > 0 and pul_10000 >= on: #10 minglik bor
                            if besh > 0 and pul_5000 >= besh: #5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:# 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming: #minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}  
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else: #minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else: #2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming: # Minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                        {besh} {words[til]} 5 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else: # Minglikyo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else: #  5 minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki: # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming: # Minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else: # Minglik yo'q
                                        soni = (f"""
                                            {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                            {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                            {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else: # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming: #minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else: # Minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else:
                            if besh > 0 and pul_5000 >= besh: #5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki: #2minglik bor
                                    if ming > 0 and pul_1000 >= ming: # Minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {besh} {words[til]} 5 {words[til1]} 
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:   # Minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {besh} {words[til]} 5 {words[til1]} 
                                        {ikki} {words[til]} 2 {words[til1]}     
                                            """)
                                        return soni
                                else: # 2 mingliki yo'q
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {besh} {words[til]} 5 {words[til1]} 
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:
                                if ikki > 0 and pul_2000 >= ikki:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {ikki} {words[til]} 2 {words[til1]} 
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}
                                            """)
                                        return soni
                    else:  # 20 minglik yo`q
                        if on > 0 and pul_10000 >= on:  # 10ming bor
                            if besh > 0 and pul_5000 >= besh:  # besh mingik bor
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                        {ming} {words[til]} {words[til1]}

                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  # 5minglik yo'q 50 minglik yo'q 20 minlik yo'q
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else:  # 10 minglik yo'q 50 minglik yo'q 20 minglik yoq
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}   
                                            """)
                                        return soni
                            else:  # 5 minglik yo'q  10 minglik yo'q 50 minglik yo'q 20 minglik yoq
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}""")
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        {ming} {words[til]} {words[til1]}""")

                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yuz} {words[til]} 100 {words[til1]}
                                        """)
                                        return soni
            else: #100 minglik yo'q
                if ellik > 0 and pul_50000 >= ellik: # 50 minglik bor
                    if yigirma > 0 and pul_20000 >= yigirma: #20 minglik bor 50 minglik bor
                        if on > 0 and pul_10000 >= on: # 10 minglik bor 20 minglik bor 50 minglik bor
                            if besh > 0 and pul_5000 >= besh: #besh minglik bor 10 minglik bor 20 minglik bor 50 minglik bor
                                if ikki > 0 and pul_2000 >= ikki: # ikki minglik bor  besh minglik bor 10 minglik bor 20 minglik bor 50 minglik bor
                                    if ming > 0 and pul_1000 >= ming: #minglik bor  ikki minglik bor  besh minglik bor 10 minglik bor 20 minglik bor 50 minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:#minglik yo'q  ikki minglik bor  besh minglik bor 10 minglik bor 20 minglik bor 50 minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}  
                                            """)
                                        return soni
                                else:# ikki minglik y'q  besh minglik bor 10 minglik bor 20 minglik bor 50 minglik bor
                                    if ming > 0 and pul_1000 >= ming:#minglik bor  ikki minglik yo'q  besh minglik bor 10 minglik bor 20 minglik bor 50 minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                            {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  #5 minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}   {ellik} {words[til]} 50 {words[til1]}  
                                        {yigirma} {words[til]} 20 {words[til1]}    {on} {words[til]} 10 {words[til1]}  
                                        {ikki} {words[til]} 2 {words[til1]}        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                         {ikkiyuz} {words[til]} 200 {words[til1]}   {ellik} {words[til]} 50 {words[til1]}  
                                        {yigirma} {words[til]} 20 {words[til1]}    {on} {words[til]} 10 {words[til1]}  
                                        {ikki} {words[til]} 2 {words[til1]}  
                                            """)
                                        return soni
                                else:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}   {ellik} {words[til]} 50 {words[til1]}  
                                        {yigirma} {words[til]} 20 {words[til1]}    {on} {words[til]} 10 {words[til1]}  
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}   {ellik} {words[til]} 50 {words[til1]}  
                                        {yigirma} {words[til]} 20 {words[til1]}    {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else: #10 minglik yo'q
                            if besh > 0 and pul_5000 >= besh: #5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki: #2 minglik bor
                                    if ming > 0 and pul_1000 >= ming: #minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}    {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else: #minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}    {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else: #ikkiminglik yo'q
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}    {besh} {words[til]} 5 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}    {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else: # 5 minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}
                                            """)
                                        return soni
                    else:  # 20 minglik yo`q
                        if on > 0 and pul_10000 >= on:  # 10ming bor
                            if besh > 0 and pul_5000 >= besh:  # besh mingik bor
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                        {ming} {words[til]} {words[til1]}

                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  # 5minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {ikki} {words[til]} 2 {words[til1]}       
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else:  # 10 minglik yo'q
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}      
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}   
                                            """)
                                        return soni
                            else:  # 5 minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}""")
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""                                    
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                        {ming} {words[til]} {words[til1]}""")

                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {ellik} {words[til]} 50 {words[til1]}
                                            """)
                                        return soni
                else:  # 50minglik yo'q
                    if yigirma > 0 and pul_20000 >= yigirma:  # 20 minglik bor
                        if on > 0 and pul_10000 >= on:  # 10 minglik bor
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]} {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}       {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}      {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]} {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}       {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}  
                                            """)
                                        return soni
                                else:  # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # Minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]} {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}       {besh} {words[til]} 5 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # Minglikyo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]} {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}       {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  # 5 minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # Minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}   
                                        {on} {words[til]} 10 {words[til1]}        {ikki} {words[til]} 2 {words[til1]}       
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # Minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}   
                                        {on} {words[til]} 10 {words[til1]}        {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:  # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}   
                                        {on} {words[til]} 10 {words[til1]}        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # Minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}   
                                        {on} {words[til]} 10 {words[til1]} 
                                            """)
                                        return soni
                        else:
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # Minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}   
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}       
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # Minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}   
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}     
                                            """)
                                        return soni
                                else:  # 2 mingliki yo'q
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}   
                                        {besh} {words[til]} 5 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}   
                                        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else: # 5 minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}   
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}   
                                        {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}   
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                            """)
                                        return soni
                    else:  # 20 minglik yo`q
                        if on > 0 and pul_10000 >= on:  # 10ming bor
                            if besh > 0 and pul_5000 >= besh:  # besh mingik bor
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ming} {words[til]} {words[til1]}

                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  # 5minglik yo'q 50 minglik yo'q 20 minlik yo'q
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)     #CREATED BY ZAFARBEK
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else:  # 10 minglik yo'q 50 minglik yo'q 20 minglik yoq
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {besh} {words[til]} 5 {words[til1]}       
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {besh} {words[til]} 5 {words[til1]}       
                                        {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {besh} {words[til]} 5 {words[til1]}       
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {besh} {words[til]} 5 {words[til1]}   
                                            """)
                                        return soni
                            else:  # 5 minglik yo'q  10 minglik yo'q 50 minglik yo'q 20 minglik yoq
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}   {ikki} {words[til]} 2 {words[til1]}       
                                        {ming} {words[til]} {words[til1]}""")
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}   {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}    {ming} {words[til]} {words[til1]}""")

                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  
                                        """)
                                        return soni
        else:
            if yuz > 0 and pul_100000 >= yuz:
                if ellik > 0 and pul_50000 >= ellik:
                    if yigirma > 0 and pul_20000 >= yigirma:
                        if on > 0 and pul_10000 >= on:
                            if besh > 0 and pul_5000 >= besh:
                                if ikki > 0 and pul_2000 >= ikki:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}  {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}  {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                            {yuz} {words[til]} 100 {words[til1]}
                                            {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                            {on} {words[til]} 10 {words[til1]}  {besh} {words[til]} 5 {words[til1]}
                                            {ikki} {words[til]} 2 {words[til1]}  
                                            """)
                                        return soni
                                else:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}  {besh} {words[til]} 5 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                            {yuz} {words[til]} 100 {words[til1]}
                                            {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                            {on} {words[til]} 10 {words[til1]}  {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:
                                if ikki > 0 and pul_2000 >= ikki:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}  {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                            {yuz} {words[til]} 100 {words[til1]}
                                            {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                            {on} {words[til]} 10 {words[til1]}  {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}   {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                            {yuz} {words[til]} 100 {words[til1]}
                                            {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                            {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else:
                            if besh > 0 and pul_5000 >= besh:
                                if ikki > 0 and pul_2000 >= ikki:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}    {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}    {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}     {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:
                                if ikki > 0 and pul_2000 >= ikki:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}  {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                            """)
                                        return soni
                    else:  # 20 minglik yo`q
                        if on > 0 and pul_10000 >= on:  # 10ming bor
                            if besh > 0 and pul_5000 >= besh:  # besh mingik bor
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}    {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}    {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}  {ming} {words[til]} {words[til1]}

                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  # 5minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}   {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}  {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else:  # 10 minglik yo'q
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}    {besh} {words[til]} 5 {words[til1]}   
                                        {ikki} {words[til]} 2 {words[til1]}      {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}    {besh} {words[til]} 5 {words[til1]}   
                                        {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}    {besh} {words[til]} 5 {words[til1]}   
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}    {besh} {words[til]} 5 {words[til1]}   
                                            """)
                                        return soni
                            else:  # 5 minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}     {ikki} {words[til]} 2 {words[til1]} 
                                        {ming} {words[til]} {words[til1]}""")
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}     {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}    {ming} {words[til]} {words[til1]}""")

                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ellik} {words[til]} 50 {words[til1]}
                                            """)
                                        return soni
                else:  # 50minglik yo'q
                    if yigirma > 0 and pul_20000 >= yigirma:  # 20 minglik bor
                        if on > 0 and pul_10000 >= on:  # 10 minglik bor
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}  
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:  # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # Minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                        {besh} {words[til]} 5 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # Minglikyo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  # 5 minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # Minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # Minglik yo'q
                                        soni = (f"""
                                            {yuz} {words[til]} 100 {words[til1]}
                                            {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                            {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:  # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}  
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # Minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else:
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # Minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {besh} {words[til]} 5 {words[til1]} 
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # Minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {besh} {words[til]} 5 {words[til1]} 
                                        {ikki} {words[til]} 2 {words[til1]}     
                                            """)
                                        return soni
                                else:  # 2 mingliki yo'q
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {besh} {words[til]} 5 {words[til1]} 
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:
                                if ikki > 0 and pul_2000 >= ikki:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {ikki} {words[til]} 2 {words[til1]} 
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}
                                            """)
                                        return soni
                    else:  # 20 minglik yo`q
                        if on > 0 and pul_10000 >= on:  # 10ming bor
                            if besh > 0 and pul_5000 >= besh:  # besh mingik bor
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                        {ming} {words[til]} {words[til1]}

                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  # 5minglik yo'q 50 minglik yo'q 20 minlik yo'q
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else:  # 10 minglik yo'q 50 minglik yo'q 20 minglik yoq
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}   
                                            """)
                                        return soni
                            else:  # 5 minglik yo'q  10 minglik yo'q 50 minglik yo'q 20 minglik yoq
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}""")
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        {ming} {words[til]} {words[til1]}""")

                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yuz} {words[til]} 100 {words[til1]}
                                        """)
                                        return soni
            else:  # 100 minglik yo'q
                if ellik > 0 and pul_50000 >= ellik:  # 50 minglik bor
                    if yigirma > 0 and pul_20000 >= yigirma:  # 20 minglik bor 50 minglik bor
                        if on > 0 and pul_10000 >= on:  # 10 minglik bor 20 minglik bor 50 minglik bor
                            if besh > 0 and pul_5000 >= besh:  # besh minglik bor 10 minglik bor 20 minglik bor 50 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor  besh minglik bor 10 minglik bor 20 minglik bor 50 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor  ikki minglik bor  besh minglik bor 10 minglik bor 20 minglik bor 50 minglik bor
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q  ikki minglik bor  besh minglik bor 10 minglik bor 20 minglik bor 50 minglik bor
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}  
                                            """)
                                        return soni
                                else:  # ikki minglik y'q  besh minglik bor 10 minglik bor 20 minglik bor 50 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor  ikki minglik yo'q  besh minglik bor 10 minglik bor 20 minglik bor 50 minglik bor
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  # 5 minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}  
                                        {yigirma} {words[til]} 20 {words[til1]}    {on} {words[til]} 10 {words[til1]}  
                                        {ikki} {words[til]} 2 {words[til1]}        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}  
                                        {yigirma} {words[til]} 20 {words[til1]}    {on} {words[til]} 10 {words[til1]}  
                                        {ikki} {words[til]} 2 {words[til1]}  
                                            """)
                                        return soni
                                else:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}  
                                        {yigirma} {words[til]} 20 {words[til1]}    {on} {words[til]} 10 {words[til1]}  
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}  
                                        {yigirma} {words[til]} 20 {words[til1]}    {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else:  # 10 minglik yo'q
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}    {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}    {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:  # ikkiminglik yo'q
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}    {besh} {words[til]} 5 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}    {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  # 5 minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}   {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {yigirma} {words[til]} 20 {words[til1]}
                                            """)
                                        return soni
                    else:  # 20 minglik yo`q
                        if on > 0 and pul_10000 >= on:  # 10ming bor
                            if besh > 0 and pul_5000 >= besh:  # besh mingik bor
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q     #CREATED BY ZAFARBEK
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                        {ming} {words[til]} {words[til1]}

                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  # 5minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {ikki} {words[til]} 2 {words[til1]}       
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else:  # 10 minglik yo'q
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}      
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}   
                                            """)
                                        return soni
                            else:  # 5 minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}""")
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""                                    
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                        {ming} {words[til]} {words[til1]}""")

                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ellik} {words[til]} 50 {words[til1]}
                                            """)
                                        return soni
                else:  # 50minglik yo'q
                    if yigirma > 0 and pul_20000 >= yigirma:  # 20 minglik bor
                        if on > 0 and pul_10000 >= on:  # 10 minglik bor
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}       {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}      {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}       {besh} {words[til]} 5 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}  
                                            """)
                                        return soni
                                else:  # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # Minglik bor
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}       {besh} {words[til]} 5 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # Minglikyo'q
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}
                                        {on} {words[til]} 10 {words[til1]}       {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  # 5 minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # Minglik bor
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}   
                                        {on} {words[til]} 10 {words[til1]}        {ikki} {words[til]} 2 {words[til1]}       
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # Minglik yo'q
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}   
                                        {on} {words[til]} 10 {words[til1]}        {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:  # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}   
                                        {on} {words[til]} 10 {words[til1]}        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # Minglik yo'q
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}   
                                        {on} {words[til]} 10 {words[til1]} 
                                            """)
                                        return soni
                        else:
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # Minglik bor
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}   
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}       
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # Minglik yo'q
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}   
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}     
                                            """)
                                        return soni
                                else:  # 2 mingliki yo'q
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}   
                                        {besh} {words[til]} 5 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}   
                                        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  # 5 minglik yo'q
                                if ikki > 0 and pul_2000 >= ikki:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}   
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}   
                                        {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:
                                    if ming > 0 and pul_1000 >= ming:
                                        soni = (f"""
                                        {yigirma} {words[til]} 20 {words[til1]}   
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:
                                        soni = (f"""
                                        {ikkiyuz} {words[til]} 200 {words[til1]}  {yigirma} {words[til]} 20 {words[til1]}
                                            """)
                                        return soni
                    else:  # 20 minglik yo`q
                        if on > 0 and pul_10000 >= on:  # 10ming bor
                            if besh > 0 and pul_5000 >= besh:  # besh mingik bor
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ikki} {words[til]} 2 {words[til1]} 
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}       {ming} {words[til]} {words[til1]}

                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {on} {words[til]} 10 {words[til1]}
                                        {besh} {words[til]} 5 {words[til1]}
                                            """)
                                        return soni
                            else:  # 5minglik yo'q 50 minglik yo'q 20 minlik yo'q
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {on} {words[til]} 10 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {on} {words[til]} 10 {words[til1]}
                                        {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {on} {words[til]} 10 {words[til1]}
                                        {ming} {words[til]} {words[til1]}
                                        """)  # CREATED BY ZAFARBEK
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {on} {words[til]} 10 {words[til1]}
                                            """)
                                        return soni
                        else:  # 10 minglik yo'q 50 minglik yo'q 20 minglik yoq
                            if besh > 0 and pul_5000 >= besh:  # 5 minglik bor
                                if ikki > 0 and pul_2000 >= ikki:  # 2 minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {besh} {words[til]} 5 {words[til1]}       
                                        {ikki} {words[til]} 2 {words[til1]}       {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {besh} {words[til]} 5 {words[til1]}       
                                        {ikki} {words[til]} 2 {words[til1]}""")
                                        return soni
                                else:  # 2 minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {besh} {words[til]} 5 {words[til1]}       
                                        {ming} {words[til]} {words[til1]}
                                        """)
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {besh} {words[til]} 5 {words[til1]}   
                                            """)
                                        return soni
                            else:  # 5 minglik yo'q  10 minglik yo'q 50 minglik yo'q 20 minglik yoq
                                if ikki > 0 and pul_2000 >= ikki:  # ikki minglik bor
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ikki} {words[til]} 2 {words[til1]}       
                                        {ming} {words[til]} {words[til1]}""")
                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                        {ikki} {words[til]} 2 {words[til1]}
                                            """)
                                        return soni
                                else:  # ikki minglik yo'q
                                    if ming > 0 and pul_1000 >= ming:  # minglik bor
                                        soni = (f"""
                                        {ming} {words[til]} {words[til1]}""")

                                        return soni
                                    else:  # minglik yo'q
                                        soni = (f"""
                                          
                                        """)
                                        return soni
#CREATED BY ZAFARBEK