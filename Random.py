import random

ugen = []

for agents in range(10000):
    rr = random.randint
    rc = random.choice
    
    # Oppo device details
    and_oppo = rc(['14', '11', '10'])
    model_oppo = rc(['CPH2235', 'CPH2251', 'CPH2249','CPH2237','CPH2247', 'CPH2359', 'CPH2357', 'CPH1983', 'CPH2109', 'CPH2089', 'CPH2091','CPH2009','CPH2037','CPH2043','CPH1951'])
    chrome_oppo = f"{str(rr(80, 444))}.0.{str(rr(3000, 6500))}.{str(rr(11, 499))}"
    
    # Infinix device details
    models_inf = rc(['X6823C', 'X6511B', 'X680', 'X5516B', 'X609B','X660','X660B','X652A','X450'])
    ch_inf = f"{str(rr(80, 999))}.0.{str(rr(3200, 6500))}.{str(rr(11, 999))}"
    
    # Facebook Hua device details
    fb_hua = f"{str(rr(100, 490))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
    
    # Vivo device details
    and_vivo = f"{str(rr(11, 14))}"
    models_vivo = rc(['vivo NEX A', 'V2143', 'V1922A','V2206', 'V2102', 'V2059','V2148A','V2133A', 'V2066', 'V2050','V2025','V2126','V2028'])
    
    # Realme device details
    models_re = rc(['RMX1805', 'RMX1821', 'RMX1851','RMX1911','RMX2032', 'RMX1929', 'RMX2103','RMX3231','RMX2063', 'RMX3063', 'RMX3197','RMX3581','RMX3312','RMX3357'])
    buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
    ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
    
    # Samsung device details
    ad_sam = rc(['10', '7.0', '14', '11'])
    et = rc(['U','U1','F','G','S','N','FN'])
    model_sam_et = f"SM-A705{et}"
    models_sam = rc([model_sam_et, f"SM-A516{et}", f"SM-A525{et}", f"SM-A600{et}", f"SM-A605{et}", f"SM-A606{et}", f"SM-A700{et}", f"SM-A725{et}", f"SM-G887{et}", f"SM-G885{et}",f"SM-A908{et}",f"SM-T295{et}", 'CLT-L29C','CLT-L29','CLT-L09C','CLT-L09','CLT-AL00','CLT-AL01','CLT-TL01','CLT-AL00L','CLT-L04','HW-01K','CLT-L0J','LMX420','LMX420EMW','LM-X420'])
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
