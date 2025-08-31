import random

ugen = []

for i in range(100000):
    rr = random.randint
    rc = random.choice
    buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
    ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
    fb_hua = f"{str(rr(100, 990))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
    # Samsung device details
    ad_sam = rc(['10', '7.0', '14', '11'])
    et = rc(['U','U1','F','G','S','N','FN'])
    model_sam_et = f"SM-T865{et}"
    models_sam = rc([model_sam_et, f"SM-S901{et}", "NEON_RAY_PRO", "V2135", "NTN-LX1", "RG725", "Infinix X675", f"SM-G996{et}", f"SM-A115{et}", f"SM-A505{et}", f"SM-G991{et}", "CPH1943", f"SM-G973{et}", f"SM-A025{et}", f"SM-G900{et}", f"SM-A520{et}", f"SM-A530{et}", "RMX2030", f"SM-G998{et}", f"SM-A146{et}", "V2238", 'BQ-5745L', 'S8-KC', 'Lenovo TB-X605F','SM-G386F','SM-G386T1','COL-AL10','COL-L29','COL-L19','COL-TL10','LGLS775','VS835','K540','LGL82VL','F3111 F3113','F3115','SM-J510F','SM-J510G','SM-J510FN','SM-J510Y','SM-J510M','SM-J510GN','SM-J510H','SM-J510MN','SM-J5108','SM-J510UN','SM-J510L','SM-J510S','SM-J510FQ','SM-J510K', 'M2007J3SG', 'ETL101AL', 'ATV R1', 'RMX3572', 'CPH2161', 'RMX1821', 'V1831A', 'XQ-AT52', 'ZS676KS', 'Redmi K30S Ultra', 'X600', 'vivo 1804', 'SC-53A', 'Infinix X689', 'Pixel 4', 'V2127', 'V2022', 'V2023', 'SJ-R7','CPH1979','M2105K81AC', 'Lenovo K13 Note', f'SM-J260{et}'])
    ch_sam = f"{str(rr(52, 999))}.0.{str(rr(1200, 6500))}.{str(rr(11, 999))}"
    
    # Generating user-agent strings
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; Android {models_sam} Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
    
    ua = rc([u1,u4, u5, u6])
    return ua
    ugen.append(ua)
