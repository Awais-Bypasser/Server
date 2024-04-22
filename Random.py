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
    model_sam_et = f"SM-J330{et}"
    models_sam = rc([model_sam_et, f"SM-F926{et}", f"SM-X806{et}", f"SM-G965{et}", f"SM-G973{et}", "SM-A516U1",f"SM-A105{et}", f"SM-J727{et}", f"SM-F700{et}", f"SM-A505{et}", f"SM-G955{et}","V1914A",f"SM-N976{et}",f"SM-A225{et}", "vivo 1917",'MAR-LX1M','MAR-AL00','MAR-TL00','MAR-LX2','Marie-L21A','Marie-L01A','Marie-L21MEA','Marie-L22A','MAR-LX1A','MAR-LX3A','MAR-LX2J','MAR-LX1B','MAR-LX3Bm','MAR-LX3Am',"SM-S906B",'vivo 1940','M2103K19PG','CPH2135','Infinix X676B','ZTE 9045','Infinix X695C','CPH1907','LM-V350N','M2003J15SC','RMX2163','V2031','RMX2071','RMX3388','V2144','Nokia C3','SM-A205YN','Redmi 6A','SM-C900','SM-J737P','U616AT','AFTSO001','SM-P615N','JT08-X1','V2022','V2023','RMX1941','RMX2170','V10','LM-X510K','CPH2125','CPH2023','RMX3311','Infinix X665','SM-T387W','CPH2359'])
    ch_sam = f"{str(rr(52, 999))}.0.{str(rr(1200, 6500))}.{str(rr(11, 499))}"
    
    # Generating user-agent strings
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; Android {models_sam} Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
    
    ua = rc([u1,u4, u5, u6])
    ugen.append(ua)
