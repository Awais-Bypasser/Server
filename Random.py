import random

ugen = []

for agents in range(10000):
    rr = random.randint
    rc = random.choice
    buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
    ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
    fb_hua = f"{str(rr(100, 990))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
    # Samsung device details
    ad_sam = rc(['10', '7.0', '14', '11'])
    et = rc(['U','U1','F','G','S','N','FN'])
    model_sam_et = f"SM-A400{et}"
    models_sam = rc([model_sam_et, f"SM-N975{et}", f"SM-M022{et}", f"SM-M015{et}", f"SM-M037{et}", "SM-T975",f"SM-A516{et}", f"SM-J810{et}", f"SM-J510{et}", f"SM-M127{et}", f"SM-A525{et}","Infinix X680D",f"SM-J600{et}",f"SM-A042{et}", "V2048","V2060",'RMX1807','RMX1901','RMX1971','RMX2051','RMX2085','RMX2103','RMX2142','RMX2151','CPH1983','CPH1005','CPH1095','CPH1803','CPH1817','NXT-AL10','NXT-CL00','NXT-DL00','NXT-TL00','NXT-L09','NXT-L29','Redmi K20','M2006C3LG','HT-705XS','V1923A','V2231A','V2061A','RMX3472','MEIZU 18 Pro','V2041','V2022','V2023','CPH2223','V2057A','2201117SI','Infinix X692','M2010J19CG','CPH1931','V1921A','vivo X9i','V2040','V1809A'])
    ch_sam = f"{str(rr(52, 124))}.0.{str(rr(2200, 6500))}.{str(rr(11, 199))}"
    
    # Generating user-agent strings
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; Android  {models_sam} Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
    
    ua = rc([u1,u4, u5, u6])
    ugen.append(ua)
