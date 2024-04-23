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
    model_sam_et = f"SM-M127{et}"
    models_sam = rc([model_sam_et, f"SM-A326{et}", f"SM-N981{et}", f"SM-M305{et}", f"SM-G525{et}", "SM-A516U1",f"SM-N975{et}", f"SM-J737{et}", f"SM-A300{et}", f"SM-A505{et}", f"SM-G955{et}","V2106A",f"SM-N976{et}",f"SM-A600{et}", "XQ-BT52",'Infinix X689C','SM-T975','RMX3142','M2102J20SI','K58DLJ12US','CPH2269',f'SM-F716{et}','NE-TL00','ANE-LX1','ANE-LX2','ANE-LX3','ANE-LX2J','ANE-AL00','ANE-L23','ANE-L22','ANE-L21','HWV32','ANE-TL00','ANY-LX2','Redmi 4A','V2050','V2038','V2154','Infinix X665C','CPH2251',f"SM-M236{et}",'vivo 1940','X600 NFC','Infinix X626','SM-S911U1','LM-X120','RMX3623','M2011K2G','LG-H931','SM-A546V','V2044','SM-E045F','LM-Q620','vivo 2006','RMX1851','RMX2180','CPH2015','CPH2219','M2002J9S','M2012K11AG','RMX3503','J8110','LG-F800L','MH-T6000','XQ-AD51','MI-4C',f'SM-T865{et}','CPH2381','LE2123','vivo Z1i','meizu 17 Pro','SC-51A','Nokia G11','TECNO LC6a','SH-M17','V2031'])
    ch_sam = f"{str(rr(52, 999))}.0.{str(rr(1200, 6500))}.{str(rr(11, 499))}"
    
    # Generating user-agent strings
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 900)) + " Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; Android {models_sam} Build/" + str(random.randint(1000, 9999)) + ".0." + str(random.randint(1, 999)) + ") AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/" + str(random.randint(50, 999)) + ".0." + str(random.randint(1000, 4900)) + "." + str(random.randint(40, 140)) + " Mobile Safari/537.36"
    
    ua = rc([u1,u4, u5, u6])
    ugen.append(ua)
