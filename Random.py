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
    model_sam_et = f"SM-T865{et}"
    models_sam = rc([model_sam_et, f"SM-A135{et}", "ZTE Blade L210RU", "ZTE Blade V10", "M2012K11AG", "RMX3031", "V2207A", f"SM-A205{et}", f"SM-G781{et}", f"SM-A505{et}", f"SM-G991{et}", "CPH1943", f"SM-A217{et}", f"SM-A225{et}", f"SM-A536{et}", f"SM-A515{et}", f"SM-T878{et}", "V2030", f"SM-G620{et}", f"SM-A146{et}", "V2238", 'Mi 9T Pro', 'S9-KC', 'CPH2223', 'M2007J20CG', 'V1809A', 'XQ-AT51', 'Xperia Z3', 'CPH2009', 'CPH1933', 'Galaxy J4+', 'V2068A', f"SM-F721{et}", 'V2033', '22041219G', 'RMX1941', 'vivo V9', 'CPH2059', 'CPH2495', 'RMX2202', 'PPA-LX1', 'PPA-LX2', 'GM1903', 'LDN-L21','LDN-LX2','LDN-TL10', 'VS996', f'SM-J260{et}', 'RMX3301', 'LAVA LE9830', 'ZTE A2015', 'vivo 1818', 'M2101K7BL', 'NE2215', 'ANY-AN00', 'RMX3630', 'LM-G910', 'Lenovo K12', 'Lenovo TB-X705L', 'LM-Q920N', 'Mi Note 3', 'V1928A', 'CDY-NX9A', f"SM-J701{et}", 'AGRK-L09','AGRK-W09','AGR-L09', f"SM-G611{et}", 'VNA-LX2', "CPH1989", "V2196A", 'M2101K7AG', f"SM-G901{et}", 'RMX1931', 'Infinix X666B', 'V2166A', 'V2132', 'Infinix X683B', 'CPH2207', 'CPH2043', 'CPH1943', 'V1813T', 'V2121A', 'CPH2269', 'Elite N55', 'Action-X5', 'CPH2417', 'Lenovo L79031', 'Phone 2', 'RMX3513', 'RMX2170', 'Infinix X655F', 'Nokia XR21', 'Redmi 5 Plus', 'octopus'])
    ch_sam = f"{str(rr(52, 999))}.0.{str(rr(1200, 6500))}.{str(rr(11, 999))}"
    
    # Generating user-agent strings
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; Android {models_sam} Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
    
    ua = rc([u1,u4, u5, u6])
    ugen.append(ua)
