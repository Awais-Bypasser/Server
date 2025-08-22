import random

ugen = []

for agents in range(10000):
    rr = random.randint
    rc = random.choice
    buld_re = rc(['QP1A.190711.020', 'QKQ1.190918.001', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.004', 'RP1A.200720.011', 'UKQ1.230924.001', 'UKQ1.230917.001', 'TP1A.220624.014'])
    ch_re = f"{str(rr(120, 999))}.0.{str(rr(3000, 6500))}.{str(rr(11, 999))}"
    fb_hua = f"{str(rr(100, 990))}.0.0.{str(rr(11, 99))}.{str(rr(11, 990))}"
    # Samsung device details
    ad_sam = rc(['10', '11', '12', '13', '14'])
    et = rc(['U', 'U1', 'F', 'G', 'S', 'N', 'FN'])
    model_sam_et = f"SM-T865{et}"
    models_sam = rc([
        model_sam_et, 
        f"SM-S911{et}",  # Galaxy S23
        f"SM-S921{et}",  # Galaxy S24
        f"SM-A546{et}",  # Galaxy A54
        f"SM-F946{et}",  # Galaxy Z Fold 5
        f"SM-A346{et}",  # Galaxy A34
        f"SM-A135{et}",  # Galaxy A13
        f"SM-A205{et}",  # Galaxy A20
        f"SM-G781{et}",  # Galaxy S20 FE
        f"SM-A505{et}",  # Galaxy A50
        f"SM-G991{et}",  # Galaxy S21
        f"SM-A217{et}",  # Galaxy A21s
        f"SM-A225{et}",  # Galaxy A22
        f"SM-A536{et}",  # Galaxy A53
        f"SM-A515{et}",  # Galaxy A51
        f"SM-T878{et}",  # Galaxy Tab S7
        f"SM-F721{et}",  # Galaxy Z Flip 4
        f"SM-J701{et}",  # Galaxy J7
        f"SM-G901{et}",  # Galaxy S5 Neo
        f"SM-G611{et}",  # Galaxy J7 Prime
        "23076RA4BC",     # Redmi Note 12 Pro
        "23127PN0CC",     # Xiaomi 14
        "2311DRK48C",     # Poco X6 Pro
        "23100RN82L",     # Redmi 13C
        "CPH2607",        # Oppo Reno 11
        "CPH2585",        # Oppo Find X7
        "CPH2357",        # Oppo Reno 8 Pro
        "V2271A",         # Vivo Y78
        "V2309A",         # Vivo X100
        "V2318",          # Vivo V30
        "RMX3820",        # Realme GT 5
        "RMX3842",        # Realme 12 Pro
        "PJZ110",         # OnePlus 12
        "CPH2491",        # OnePlus Nord 3
        "GPJ41",          # Google Pixel 8
        "GR1YH",          # Google Pixel 9
        "TA-1581",        # Nokia G42
        "TA-1512"         # Nokia X30
    ])
    ch_sam = f"{str(rr(52, 999))}.0.{str(rr(1200, 6500))}.{str(rr(11, 999))}"
    
    # Generating user-agent strings
    u1 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36"
    u4 = f"Mozilla/5.0 (Linux; Android {str(rr(4, 13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/{ch_re} Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/{fb_hua};]"
    u5 = f"Mozilla/5.0 (Linux; Android {str(rr(4,13))}; {models_sam} Build/{buld_re}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/{str(rr(50, 999))}.0.{str(rr(1000, 4900))}.{str(rr(40, 900))} Mobile Safari/537.36"
    u6 = f"Mozilla/5.0 (Linux; Android {models_sam} Build/{str(rr(1000, 9999))}.0.{str(rr(1, 999))}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome 4.0/{str(rr(50, 999))}.0.{str(rr(1000, 4900))}.{str(rr(40, 140))} Mobile Safari/537.36"
    
    ua = rc([u1, u4, u5, u6])
    ugen.append(ua)
