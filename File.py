import random

ugeni = []

# Devices for the lists
samsung_devices = ['SM-A115F/DS', 'SM-A115F', 'SM-A115M', 'SM-A115M/DS', 'SM-A115U', 'SM-A115A', 'SM-A115AZ', 
                   'SM-A115U1', 'SM-A115W', 'SM-A115AP', 'SM-S115DL']
realme_devices = ['RMX3310', 'RMX3312', 'RMX3311']
oppo_devices = ['JMM-AL00', 'JMM-AL10', 'JMM-TL00', 'JMM-TL10', 'JMM-L22']
lg_devices = ['Infinix X559C', 'Infinix X559', 'Infinix X559F']
sony_devices = ['F3311', 'F3313', 'C1604']
vivo_devices = ['SM-G870A', 'SC-02G', 'SM-G870D', 'SM-G870F', 'SM-G870W']
sdr = ['1816', '1817', '1820', '1811']
# Carrier and Language
fbcr = random.choice(["Telenor", "UFONE-PAKTel", "Zong", "Jazz", "Jio", "Vodafone", "Airtel", "BSNL", 
                      "Robi", "Banglalink", "Zong 4G", "LTE", "Jio 4G", "Ufone", "UFONE-PK", "null"])
fblc = random.choice(['en_US', 'en_GB', 'en_PK', 'ur_PK'])

# Models
ft = ['SM-M625F', 'LM-K525', 'NID-1050', 'SM-A3051', 'CPH2069', 'RMX3286', 'A101XM', 'SM-A505GT', 'WKG-LX9', 
      'SM-A4260', 'Infinix X680C', 'RMX3265', 'GLA-LX1', 'Redmi 4X', 'V2204', 'vivo 2018', 'PCB-T104', 
      '2201122G', 'Infinix X688B', 'RMP2106', 'OXF-AN10', 'Infinix X6835B', 'CPH2399', 'SM-F731B', 'SM-T515', 
      'CPH2209', 'M2101K6R', 'V2135', 'SM-M307FN', 'JLN-LX3', 'CPH2123', 'Lenovo TB-X605F', 'V2110', 
      'RMX3572', 'LM-X420']

# OS Versions
su = ['QP1A.190711.020', 'QKQ1.190918.001', 'TP1A.220624.014', 'SP1A.210812.016', 'QTG3.200617.002', 
      'SQ3A.220705.0040', 'RP1A.200720.011']

# Random OS version
so = random.choice(su)
efg = random.choice(ft)

# Generate random User-Agent strings
for agents in range(10000):
    # Select device models
    samsung = random.choice(samsung_devices)
    realme = random.choice(realme_devices)
    oppo = random.choice(oppo_devices)
    lg = random.choice(lg_devices)
    vivo = random.choice(vivo_devices)
    vivo1 = random.choice(sdr)
    
    # Create user agent components
    ua6 = f"[FBAN/FB4A;FBAV/{random.randint(111, 555)}.0.0.{random.randint(9, 49)}{random.randint(11, 77)};FBBV/{random.randint(1111111, 7777777)};FBLC/{fblc};FBCR/{fbcr};FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/{realme};FBSV/12;FBOP/14;FBCA/arm64-v8a;]"
    ua5 = f"[FBAN/FB4A;FBAV/{random.randint(111, 555)}.0.0.{random.randint(9, 49)}{random.randint(11, 77)};FBBV/{random.randint(1111111, 7777777)};FBLC/{fblc};FBCR/{fbcr};FBMF/HONOR;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/{oppo};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = f"[FBAN/FB4A;FBAV/{random.randint(111, 555)}.0.0.{random.randint(9, 49)}{random.randint(11, 77)};FBBV/{random.randint(1111111, 7777777)};FBLC/{fblc};FBCR/{fbcr};FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/{vivo1};FBSV/8.1.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua2 = f"[FBAN/FB4A;FBAV/{random.randint(111, 555)}.0.0.{random.randint(9, 49)}{random.randint(11, 77)};FBBV/{random.randint(1111111, 7777777)};FBLC/{fblc};FBCR/{fbcr};FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/{lg};FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua7 = f"[FBAN/FB4A;FBAV/{random.randint(111, 555)}.0.0.{random.randint(9, 49)}{random.randint(11, 77)};FBBV/{random.randint(1111111, 7777777)};FBLC/{fblc};FBCR/{fbcr};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/{vivo};FBSV/4.4.2;FBCA/armeabi-v7a:armeabi;]"
    ua10 = f"[FBAN/FB4A;FBAV/{random.randint(11, 77)}.0.0.{random.randint(9, 49)}{random.randint(11, 77)};FBBV/{random.randint(1111111, 7777777)};FBLC/en_US;FBCR/MobileNation;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/Samsung Galaxy A54 5G;FBSV/8.0;FBCA/armeabi-v7a:armeabi;]"
    ua1 = f"Dalvik/2.1.0 (Linux; U; Android {random.randint(4, 13)}; {efg} Build/{so}) [FBAN/FB4A;FBAV/{random.randint(111, 555)}.0.0.{random.randint(9, 49)}{random.randint(11, 77)};FBBV/{random.randint(1111111, 7777777)};FBLC/{fblc};FBCR/{fbcr};FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/{samsung};FBSV/10;FBOP/1;FBCA/arm64-v8a;]"

    # Randomly pick a user agent from the list
    ua = random.choice([ua6, ua5, ua7, ua2, ua4, ua1])
    
    # Append to list
    ugeni.append(ua)
