import random

ugen = []

for agents in range(10000):
    rr = random.randint
    rc = random.choice
    
    # Oppo device details
    and_oppo = rc(['14', '11', '10'])
    model_oppo = rc(['CPH2203', 'CPH3803', 'CPH3805','CPH1987','CPH1015', 'CPH1077', 'CPH1137', 'CPH1817', 'CPH1101', 'CPH1805', 'CPH1821','CPH2059','CPH2337','CPH2339','CPH3837'])
    chrome_oppo = f"{str(rr(80, 444))}.0.{str(rr(3000, 6500))}.{str(rr(11, 499))}"
    
    # Infinix device details
    models_inf = rc(['X655D', 'X662B', '559C', 'X601', '610B','X610B','X267','X5515','X605'])
    ch_inf = f"{str(rr(80, 999))}.0.{str(rr(3200, 6500))}.{str(rr(11, 999))}"
    
    # Facebook Hua device details
    fb_hua = f"{str(rr(100, 490))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
    
    # Vivo device details
    and_vivo = f"{str(rr(11, 14))}"
    models_vivo = rc(['vivo 2018', 'V2238A', 'V2147','V2065A', 'V2135', 'V2022','V2027','V2023', 'V2110', 'vivo 1920','V2046','V2206','V2080A','V2190A','V1916A'])
    
    # Realme device details
    models_re = rc(['RMX1851', 'RMX1911', 'RMX1945','RMX1993','RMX2021', 'RMX2032', 'RMX2063','RMX2071','RMX2111', 'RMX2101', 'RMX2180','RMX3081','RMX1993','RMX2086'])
    buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
    ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
    
    # Samsung device details
    ad_sam = rc(['10', '7.0', '14', '11'])
    et = rc(['U','U1','F','G','S','N','FN'])
    model_sam_et = f"SM-A705{et}"
    models_sam = rc([model_sam_et, f"SM-A500{et}", f"SM-G920{et}", f"SM-J320{et}", f"SM-J510{et}", f"SM-G900{et}", f"SM-A426{et}", f"SM-A326{et}", f"SM-N915{et}", f"SM-G988{et}",f"SM-A507{et}",f"SM-T515{et}", "SM-X200", 'LM-V500N','PAR-AL00','PAR-LX1M','PAR-LX1','PAR-LX9','PAR-TL20','PAR-TL00','M2012K11AG',f'SM-A600{et}','LM-Q310N','M2101K6P'])
    ch_sam = f"{str(rr(52, 124))}.0.{str(rr(2200, 6500))}.{str(rr(11, 199))}"
    ewg = rc([models_sam,models_re,models_vivo,model_oppo])
    
    # Generating user-agent strings
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {model_oppo} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{chrome_oppo} Mobile Safari/537.36"
    u2 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; Infinix {models_inf} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_inf} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u3 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_vivo} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_re} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; Android {ewg} Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
    
    ua = rc([u1, u2, u3, u4, u5, u6])
    ugen.append(ua)
