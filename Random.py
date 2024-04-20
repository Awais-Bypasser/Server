import random

ugen = []

for agents in range(10000):
    rr = random.randint
    rc = random.choice
    
    # Oppo device details
    and_oppo = rc(['14', '11', '10'])
    model_oppo = rc(['CPH2035', 'CPH3987', 'CPH3983','CPH1853','CPH1837', 'CPH1805', 'CPH1809', 'CPH2201', 'CPH2185', 'CPH2161', 'CPH2139','CPH2385','CPH3803','CPH3853','CPH1005'])
    chrome_oppo = f"{str(rr(80, 444))}.0.{str(rr(3000, 6500))}.{str(rr(11, 499))}"
    
    # Infinix device details
    models_inf = rc(['X267', 'X571', 'X624B', 'X627V', 'X682B','X695C','X695','X6515','X670'])
    ch_inf = f"{str(rr(80, 999))}.0.{str(rr(3200, 6500))}.{str(rr(11, 999))}"
    
    # Facebook Hua device details
    fb_hua = f"{str(rr(100, 490))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
    
    # Vivo device details
    and_vivo = f"{str(rr(11, 14))}"
    models_vivo = rc(['V1955A', 'V2146', 'vivo Y66','V2158', 'vivo 1818', 'V2120','V2162A','V2118A', 'V2124', 'vivo 1951','V2203','V2205','V2117'])
    
    # Realme device details
    models_re = rc(['RMX1931', 'RMX1971', 'RMX1991','RMX1992','RMX2001', 'RMX2021', 'RMX2030','RMX2050','RMX2063', 'RMX2072', 'RMX2076','RMX2086','RMX2121','RMX2144'])
    buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
    ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
    
    # Samsung device details
    ad_sam = rc(['10', '7.0', '14', '11'])
    et = rc(['U','U1','F','G','S','N','FN'])
    model_sam_et = f"SM-A705{et}"
    models_sam = rc([model_sam_et, f"SM-A505{et}", f"SM-J415{et}", f"SM-G981{et}", f"SM-A305{et}", f"SM-G998{et}", f"SM-A326{et}", f"SM-A226{et}", f"SM-A725{et}", f"SM-N970{et}",f"SM-N986{et}",f"SM-A720{et}", 'AMN-LX9','AMN-LX1','AMN-LX2','AMN-LX3','VOG-L29','VOG-L09','VOG-AL00','VOG-TL00','VOG-L04','VOG-AL10','HW-02L','22101316UP','M2012K11AG','LM-Q730N','LMQ620WA','LM-Q620WA','LM-Q620VAB','LMQ620VAB','LM-Q730'])
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
