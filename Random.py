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
    model_sam_et = f"SM-G355{et}"
    models_sam = rc([model_sam_et, f"SM-A750{et}", "ZTE Blade L210RU", "ZTE Blade V10", "M2012K11AG", "RMX3031", "V2207A", f"SM-A415{et}", f"SM-A146{et}", f"SM-A805{et}", f"SM-M136{et}", "CPH1943", f"SM-A125{et}", f"SM-M307{et}", f"SM-A516{et}", f"SM-A102{et}", f"SM-A520{et}", "RMX1991", f"SM-F711{et}", f"SM-J610{et}", "RMX3612", 'RMX3561', 'ANG-L02B', 'ANG-L21B', 'ANG-L22B', 'ANG-LX1', 'ANG-LX2', 'CPH1919', 'ASUS_I001DE', 'NX627J', 'M2012K11AG', 'V2055A', f"SM-F907{et}", 'LM-K525', 'JKM-LX1', 'JKM-LX2', 'JKM-LX3', 'JKM-AL00', 'JKM-TL00', 'JKM-AL00a', 'JKM-AL00b', 'vivo 2006', 'Infinix X687', 'Primo NF5', 'vivo 1910', 'V2132A', 'V2131', 'vivo 2010', 'RMX3627', 'V2126', 'CPH2067', 'vivo 1938', 'V608C', 'M2007J22G', 'V2065', 'RMX2020', 'M2101K7AI', 'CPH2127', 'LG-H870S', 'V1923A', 'ZTE 2050', f"SM-A045{et}", 'SM-A015T1', 'M2102J20SI', 'LM-F100N', 'V2053', f"SM-G611{et}", 'V2042', "vivo 1909", "RMX3392", '23013RK75C', f"SM-J330{et}", 'CPH2025', 'CPH2415', 'X8A', 'ZTE Blade L130', 'V2037', 'LM-K410', 'LM-Q730N', 'Tab S5e', 'BQ-5540L', 'LM-Q910', 'RMX3063', 'CPH2461', 'vivo 1819', 'Redmi 4 Prime', 'ZTE A2121', 'ONEPLUS A6013', 'CPH2271', 'V2154', 'meizu 16Xs', 'CPH1819', 'V2105', 'X7'])
    ch_sam = f"{str(rr(52, 999))}.0.{str(rr(1200, 6500))}.{str(rr(11, 999))}"
    
    # Generating user-agent strings
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; Android {models_sam} Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
    
    ua = rc([u1,u4, u5, u6])
    ugen.append(ua)
