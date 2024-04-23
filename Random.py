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
    model_sam_et = f"SM-J320{et}"
    models_sam = rc([model_sam_et, f"SM-A202{et}", "V2126", "SM-X200", "V2028", "V2118A", "V2012A", f"SM-A022{et}", f"SM-M215{et}", f"SM-A405{et}", "SM-A516U1", f"SM-A125{et}", f"SM-A137{et}", f"SM-A207{et}", f"SM-A507{et}", f"SM-A135{et}", "vivo 1920", f"SM-A115{et}", f"SM-A105{et}", "CPH2109", 'YAL-L21', 'YAL-L61', 'YAL-L71', 'YAL-L61D', 'M2010J19SG', 'M2101K9G', 'Realme XT', 'LM-G820', 'CPH2293', f'SM-N981{et}', 'BND-AL10', 'BND-TL10', 'BND-L21', 'BND-L22', 'BND-L24', 'BND-L31', 'BND-L2', 'BND-L34', 'BND-AL00', 'CPH2013', 'V2046A', 'V2116', 'RMX3350', 'N10-EEA', 'V1816A', 'V1829A', 'RMX1831', 'CPH2305', 'J9210', 'UPD-BJ00R', 'V2145A', 'V1955A', 'CPH2307', 'V2146', 'M2006J10C', 'CPH2263', 'V1913A', 'V2168', 'RMX1821', 'CPH2001', 'V2031A', 'V1816T', 'RMX2121', 'Infinix X604', f'SM-A920{et}', 'V2139', "Infinix X676C", "CPH2359", 'V11', f'SM-N935{et}', 'Tab 7 Pro', 'V2162A', 'RMX3371', 'CPH2373', 'GT-I9505', 'CPH1938', 'CPH1877', 'RMX3242', 'ZTE Blade A51', 'LAVA LMX06', 'RMX1833', 'RMX1851', 'CPH2419', 'CPH2481', 'V2203'])
    ch_sam = f"{str(rr(52, 999))}.0.{str(rr(1200, 6500))}.{str(rr(11, 999))}"
    
    # Generating user-agent strings
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
    u7 = f"Mozilla/5.0 (Linux; Android {models_sam} Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
    
    ua = rc([u1,u4, u5, u6,u7])
    ugen.append(ua)
