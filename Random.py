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
    model_sam_et = f"SM-A205{et}"
    models_sam = rc([model_sam_et, f"SM-A326{et}", f"SM-A035{et}", f"SM-M305{et}", f"SM-G525{et}", "SM-A516U1", f"SM-N975{et}", f"SM-J737{et}", f"SM-A300{et}", f"SM-A505{et}", f"SM-G955{et}", "vivo 1920", f"SM-A115{et}", f"SM-A105{et}", "CPH2109", 'V2207', 'vivo 1951', 'LM-K200', 'XQ-AT52', '2203129G', 'FIG-AL10', f"SM-A526{et}", 'CPH1941', 'V2219', 'V2032', 'V2054A', 'CPH2083', 'vivo 1818', '22127RK46C', 'M2101K9AI', 'BLA-L29', 'BLA-L09', 'BLA-AL00', 'BLA-A09', 'BLA-TL00', 'BQ-5732L', 'LE2121', 'SM-R860', 'ZTE Blade A7 2020', 'SM-X900', '2201116SG', "V2106A", 'RMX3142', 'RMX3115', 'Infinix X695D', 'CPH2269', 'V2133A', 'RMX3371', 'CPH2081', 'vivo 1912', 'V2066', 'U1006H', '100026203', 'vivo 1906', 'CPH1911', 'TECNO CH6i', 'CPH2251', 'SM-G981V', 'LM-V350', 'RMX3151', 'Infinix X657C', 'LM-K315IM', 'SM-S757BL', 'CPH1979', 'M1908C3JGG', 'V1990A', 'V2127', 'YT7260L', 'CPH2381', 'Moto X4', 'CPH2173', 'RMX1992', 'vivo 1804', 'RMX2002', 'SM-P205', 'CPH2387', f"SM-A102{et}", 'M2010J19SI'])
    ch_sam = f"{str(rr(52, 999))}.0.{str(rr(1200, 6500))}.{str(rr(11, 499))}"
    
    # Generating user-agent strings
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; Android {models_sam} Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
    
    ua = rc([u1,u4, u5, u6])
    ugen.append(ua)
