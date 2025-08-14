import random

ugen = []

for agents in range(10000):
    rr = random.randint
    rc = random.choice
    
    # Oppo device details
    and_oppo = rc(['14', '11', '10'])
    model_oppo = rc(['CPH2373', 'CPH2071', 'CPH2269','CPH2421','CPH1837', 'CPH1605', 'CPH2139', 'CPH1701', 'CPH2309', 'CPH1717', 'CPH1715','CPH1729','CPH1939','CPH1913','CPH1969'])
    chrome_oppo = f"{str(rr(80, 444))}.0.{str(rr(3000, 6500))}.{str(rr(11, 499))}"
    
    # Infinix device details
    models_inf = rc(['X572', 'X671B', 'X573B', 'X655D', 'X655C','X650D','X606D','X559C','X6816D','X665'])
    ch_inf = f"{str(rr(80, 999))}.0.{str(rr(3200, 6500))}.{str(rr(11, 999))}"
    
    # Facebook Hua device details
    fb_hua = f"{str(rr(100, 490))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
    
    # Vivo device details
    and_vivo = f"{str(rr(11, 14))}"
    models_vivo = rc(['V2139', 'V2131', 'V2141A','vivo 1933', 'V1911A', 'V1930A','vivo 1806','V2058', 'V1813BT', 'vivo 1907','V2116','vivo 1910','V2134'])
    
    # Realme device details
    models_re = rc(['RMX3357', 'RMX3560', 'RMX3350','RMX2156','RMX3430', 'RMX3171', 'RMX3092','RMX3574','RMX3093', 'RMX2112', 'RMX2142','RMX2086','RMX2072','RMX3462'])
    buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
    ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
    
    # Samsung device details
    ad_sam = rc(['10', '7.0', '14', '11'])
    et = rc(['U','U1','F','G','S','N','FN'])
    model_sam_et = f"SM-A015{et}"
    models_sam = rc([model_sam_et, f"SM-A405{et}", f"SM-A305{et}", f"SM-A307{et}", f"SM-A320{et}", f"SM-A300{et}", f"SM-A260{et}", f"SM-A136{et}", f"SM-A137{et}", f"SM-A127{et}",f"SM-A107{et}",f"SM-A102{et}", 'ELS-NX9','ELS-N04','ELS-AN00','ELS-TN00','LM-G900N','LM-G900EM','LM-G900','LM-G900TM'])
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
