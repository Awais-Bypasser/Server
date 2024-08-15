import random
ugeni = []
for agents in range(10000):
    samsung = random.choice(['SM-G360T, SM-G3606, SM-G3608, SM-G3609, SM-G360BT, SM-G360F, SM-G360FY, SM-G360G, SM-G360GY, SM-G360H, SM-G360H/D, SM-G360BT, SM-G361, SM-G361H, SM-G361F, SM-G360HU, SM-G360T1, SM-G360M, SM-G360P, SM-G360V, SM-S820L, SM-G360AZ, SM-G361HU'])
    oppo = random.choice(['SM-A705F','SM-A705FN','SM-A705GM','SM-A705MN','SM-A7050','SM-A705W','SM-A705YN','SM-A705X','SM-A705U'])
    vivo = random.choice(['SM-A805F','SM-A8050','SM-A805X','SM-A805N'])
    realme = random.choice(['RMX1911','RMX1919','RMX1927'])
    fbcr = random.choice([
    "Verizon Wireless", "AT&T", "T-Mobile", "Sprint", "Cricket Wireless", "US Cellular", 
    "Boost Mobile", "Metro by T-Mobile", "TracFone Wireless", "Virgin Mobile USA", "Xfinity Mobile", 
    "Google Fi", "Consumer Cellular", "Straight Talk", "Republic Wireless", "C Spire", "Mint Mobile", 
    "Ultra Mobile", "Simple Mobile", "Total Wireless", "Visible", "Ting", "Net10 Wireless", "H2O Wireless", 
    "FreedomPop", "Red Pocket Mobile", "TextNow", "Page Plus Cellular", "GoSmart Mobile", "Lycamobile", 
    "Gen Mobile", "Wing Alpha", "Tello", "Good2Go Mobile", "Patriot Mobile", "Twigby", "Spectrum Mobile", 
    "US Mobile", "Affinity Cellular", "Reach Mobile", "AirVoice Wireless", "Selectel Wireless", "Boom Mobile", 
    "Telcel América", "EasyGO Wireless", "Speedtalk Mobile", "Black Wireless", "EcoMobile", "ROK Mobile", 
    "GIV Mobile", "Life Wireless", "Pix Wireless", "Global Connection Inc.", "H2O Bolt", "Real Mobile", 
    "STI Mobile", "EcoMobile", "Allvoi Wireless", "Zing PCS", "Lyca Mobile", "GIV Mobile", "Red Pocket Mobile", 
    "FonAngle", "CREDO Mobile", "Jolt Mobile", "Good2GO Mobile", "Flash Wireless", "EcoMobile", "LYCAMOBILE", 
    "h2o Bolt", "LYCAMOBILE", "Dingtone", "Black Wireless", "Eco Mobile", "AF Mobile", "Selectel Wireless", 
    "Boss Revolution Mobile", "Starlink Wireless", "Verizon Prepaid", "TruConnect", "Dollar Phone Pinless", 
    "AirVoice Wireless", "FreeUP Mobile", "GreatCall", "OTG Mobile", "Slickdeals Mobile", "LYCAMOBILE", 
    "Proven Wireless", "Ptel Mobile", "netTALK", "Liberty Wireless", "Allvoi Wireless", "Snapfon", 
    "USA Communications", "EasyGO", "i3 Mobile", "FLEX Mobile", "MobileNation", "CHT Global", "LYCAMOBILE", 
    "Basis Wireless", "GlobalTel", "Lively", "Kroger Wireless", "Teleplus Wireless", "Nokia Voicefon", 
    "GoodCall", "AF Mobile", "Proven Wireless", "Best Cellular", "Ultra Mobile", "Espanol Mobile", "EcoMobile", 
    "Snap Mobile", "TerreStar", "MyPeak Wireless", "Gomo", "BLU", "Slingshot Wireless", "EcoMobile", 
    "Open Mobile", "Nemont", "Affinity Cellular", "emobile", "Blue Green Mobile", "Twigby", "GLOMOBILE", 
    "OneSimCard", "PocketiNet", "Good2GO Mobile", "NetZero", "Defense Mobile", "HiSky", "Sterling Cellular", 
    "G-Tel", "GlobalTone", "ZingPCS", "Hello Mobile", "Alta Wireless", "Sprocket Wireless", "FamilyTalk Wireless", 
    "XCom Global", "Iridium Satellite", "Kroger Wireless", "LYCAMOBILE", "Fast Track Communications", "Invictus Wireless", 
    "Wavelength Wireless", "GreatCall", "H2O Wireless", "ROK Mobile", "Zing PCS", "EasyGo", "EasyGo", "Life Wireless", 
    "easyGO Wireless", "Lyca Mobile", "Republic Wireless", "Red Pocket Mobile", "Snap Mobile", "EcoMobile", "Triton Wireless", 
    "H2O Wireless", "US Mobile", "Tempo Telecom", "Verizon Prepaid", "Good2GO Mobile", "CellNUVO", "Net10 Wireless", "Wave7", 
    "VoxOx", "OneSimCard", "Basic PCS", "Invictus Wireless", "Credo Mobile", "NUU Mobile", "BIC Telcom", "H2O Wireless", 
    "NET10 Wireless", "Future Wireless", "Eco Mobile", "Black Wireless", "Ethicall", "Kajeet", "Global SIM Card", "USA Connect", 
    "NetZero", "Dish Wireless", "Telrite Holdings", "Lycamobile", "Flash Wireless", "VIKING SATCOM", "Tuyo Mobile", 
    "Mobile Vikings", "Madstar Mobile", "Voxter Mobile", "Lively", "Shaka Mobile", "SiriusXM", "Blaze Wireless", 
    "i3 Mobile", "GLOMOBILE", "Hello Mobile", "Boost Mobile", "Verizon Prepaid", "H2O Wireless", "AT&T", "T-Mobile", 
    "Cricket Wireless", "US Cellular", "Ultra Mobile", "TracFone Wireless", "Ting", "Republic Wireless", "Straight Talk", 
    "Consumer Cellular", "Visible", "Lycamobile", "TextNow", "GoSmart Mobile", "Wing Alpha", "Good2Go Mobile", "Twigby", 
    "US Mobile", "Spectrum Mobile", "Speedtalk Mobile", "EcoMobile", "Flash Wireless", "Black Wireless", "Selectel Wireless", 
    "Proven Wireless", "Lively", "Hello Mobile", "Net10 Wireless", "H2O Wireless", "Red Pocket Mobile", "LYCAMOBILE", "Boss Revolution Mobile", 
    "AirVoice Wireless", "Ultra Mobile", "EasyGO Wireless", "FreeUP Mobile", "GreatCall", "OTG Mobile", "Proven Wireless", "netTALK", 
    "Liberty Wireless", "Snapfon", "USA Communications", "MobileNation", "LYCAMOBILE", "GlobalTel", "BLU", "EcoMobile", "Open Mobile", 
    "Nemont", "OneSimCard", "PocketiNet", "Defense Mobile", "Iridium Satellite", "Fast Track Communications", "H2O Wireless", "ROK Mobile", 
    "Life Wireless", "easyGO Wireless", "Tempo Telecom", "VoxOx", "OneSimCard", "Basic PCS", "Invictus Wireless", "Credo Mobile", "NUU Mobile", 
    "NET10 Wireless", "Ethicall", "Kajeet", "Global SIM Card", "USA Connect", "NetZero", "Dish Wireless", "Telrite Holdings", "Flash Wireless", 
    "VIKING SATCOM", "Tuyo Mobile", "Mobile Vikings", "Madstar Mobile", "Voxter Mobile", "Shaka Mobile", "SiriusXM", "Blaze Wireless", "i3 Mobile", 
    "GLOMOBILE", "Hello Mobile"
])
    fblc = random.choice(['ar_AE','ar_BH', 'ar_DJ', 'ar_DZ', 'ar_EG', 'ar_EH', 'ar_ER', 'ar_IL', 'ar_IQ', 'ar_JO', 'ar_KM', 'ar_KW', 'ar_LB', 'ar_LY', 'ar_MA', 'ar_MR', 'ar_OM', 'ar_PS', 'ar_QA', 'ar_SA', 'ar_SD', 'ar_SO', 'ar_SS', 'ar_SY', 'ar_TD', 'ar_TN', 'ar_YE', 'bas_CM', 'bez_TZ', 'bn_BD', 'bn_IN', 'bo_CN', 'bo_IN', 'br_FR', 'ca_AD', 'ca_ES', 'ca_FR', 'ca_IT', 'chr_US', 'cy_GB', 'de_AT', 'de_BE', 'de_CH', 'de_DE', 'de_IT', 'de_LI', 'de_LU', 'dje_NE', 'dsb_DE', 'dyo_SN', 'dz_BT', 'ebu_KE', 'ee_GH', 'ee_TG', 'el_CY', 'el_GR', 'en_AG', 'en_AI', 'en_AS', 'en_AT', 'en_AU', 'en_BB', 'en_BE', 'en_BI', 'en_BM', 'en_BS', 'en_BW', 'en_BZ', 'en_CA', 'en_CC', 'en_CH', 'en_CK', 'en_CM', 'en_CX', 'en_DE', 'en_DG', 'en_DK', 'en_DM', 'en_ER', 'en_FI', 'en_FJ', 'en_FK', 'en_FM', 'en_GB', 'en_GD', 'en_GG', 'en_GH', 'en_GI', 'en_GM', 'en_GU', 'en_GY', 'en_HK', 'en_IE', 'en_IL', 'en_IM', 'en_IN', 'en_IO', 'en_JE', 'en_JM', 'en_KE', 'en_KI', 'en_KN', 'en_KY', 'en_LC', 'en_LR', 'en_LS', 'en_MG', 'en_MH', 'en_MO', 'en_MP', 'en_MS', 'en_MT', 'en_MU', 'en_MW', 'en_MY', 'en_NA', 'en_NF', 'en_NG', 'en_NL', 'en_NR', 'en_NU', 'en_NZ', 'en_PG', 'en_PH', 'en_PK', 'en_PN', 'en_PR', 'en_PW', 'en_RW', 'en_SB', 'en_SC', 'en_SD', 'en_SE', 'en_SG', 'en_SH', 'en_SI', 'en_SL', 'en_SS', 'en_SX', 'en_SZ', 'en_TC', 'en_TK', 'en_TO', 'en_TT', 'en_VI', 'en_VU', 'en_WS', 'en_ZA', 'des_HN', 'es_IC', 'es_MX', 'es_NI', 'es_PA', 'es_PE', 'es_PR', 'es_PY', 'es_SV', 'es_US', 'es_UY', 'es_VE', 'et_EE', 'eu_ES', 'fa_AF', 'fa_IR', 'ff_CM', 'ff_GN', 'ff_MR', 'ff_SN', 'fi_FI', 'fil_PH', 'fo_DK', 'fo_FO', 'fr_BE', 'fr_BF', 'fr_BI', 'fr_BJ', 'fr_BL', 'fr_CA', 'fr_CD', 'fr_CF', 'fr_CG', 'fr_CH', 'fr_CI', 'fr_CM', 'fr_DJ', 'fr_DZ', 'fr_HT', 'fr_KM', 'fr_LU', 'fr_MA', 'fr_MC', 'fr_MF', 'fr_MG', 'fr_ML', 'fr_MQ', 'fr_MR', 'fr_MU', 'fr_NC', 'fr_NE', 'fr_PF', 'fr_PM', 'fr_RE', 'fr_RW', 'fr_SC', 'fr_SN', 'fr_SY', 'fr_TD', 'fr_TG', 'fr_TN', 'fr_VU', 'fr_WF', 'fr_YT', 'fur_IT', 'fy_NL', 'ga_IE', 'gl_ES', 'gsw_CH', 'gsw_FR', 'gsw_LI', 'gu_IN', 'guz_KE', 'gv_IM', 'ha_GH', 'ha_NE', 'ha_NG', 'haw_US', 'he_IL', 'hi_IN', 'hr_BA', 'hr_HR', 'hsb_DE', 'hu_HU', 'hy_AM', 'ig_NG', 'ii_CN', 'in_ID', 'is_IS', 'it_CH', 'it_IT', 'it_SM', 'it_VA', 'iw_IL', 'ja_JP', 'jgo_CM', 'jmc_TZ', 'ka_GE', 'kab_DZ', 'kam_KE', 'kde_TZ', 'kea_CV', 'khq_ML', 'ki_KE', 'kk_KZ', 'kkj_CM', 'kl_GL', 'kln_KE', 'km_KH', 'kn_IN', 'ko_KP', 'ko_KR', 'kok_IN', 'ks_IN', 'ksb_TZ', 'ksh_DE', 'kw_GB', 'ky_KG', 'lag_TZ', 'lt_LT', 'lb_LU', 'lv_LV', 'lg_UG', 'mk_MK', 'ml_IN', 'mr_IN', 'ms_MY', 'mt_MT', 'nl_BE', 'nl_NL', 'no_NO', 'pl_PL', 'pt_AO', 'pt_BR', 'pt_CH', 'pt_CV', 'pt_GQ', 'pt_GW', 'pt_LU', 'pt_MO', 'pt_MZ', 'pt_PT', 'pt_ST', 'pt_TL', 'ro_RO', 'ru_BY', 'ru_KG', 'ru_KZ', 'ru_MD', 'ru_RU', 'ru_UA', 'sk_SK', 'sl_SI', 'sq_AL', 'sr_BA', 'sr_CS', 'sr_ME', 'sr_RS', 'sv_SE', 'th_TH', 'tr_TR', 'vi_VN', 'zh_Hans', 'uz_UZ', 'uk_UA', 'zh_Hant', 'zh_HK', 'zu_ZA'])
    ft = ['SM-M625F', 'LM-K525', 'NID-1050', 'SM-A3051', 'CPH2069', 'RMX3286', 'A101XM', 'SM-A505GT', 'WKG-LX9', 'SM-A4260', 'Infinix X680C', 'RMX3265', 'GLA-LX1', 'Redmi 4X', 'V2204', 'vivo 2018', 'PCB-T104', '2201122G', 'Infinix X688B', 'RMP2106', 'OXF-AN10', 'Infinix X6835B', 'CPH2399', 'SM-F731B', 'SM-T515', 'CPH2209', 'M2101K6R', 'V2135', 'SM-M307FN', 'JLN-LX3', 'CPH2123', 'Lenovo TB-X605F', 'V2110', 'RMX3572', 'LM-X420']
    su = ['QP1A.190711.020', 'QKQ1.190918.001', 'TP1A.220624.014', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011']
    so = random.choice(su)
    efg = random.choice(ft)
    ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/SamsungSocial;FBAV/3.0.0;FBBV/654321098;FBDM/{density=3.0,width=720,height=1600};FBLC/en_US;FBRV/654321098;FBCR/Verizon;FBMF/Samsung;FBBD/GalaxyA22;FBPN/com.samsungsocial;FBDV/Samsung Galaxy A22;FBSV/11;FBOP/28;FBCA/arm64-v8a;]"
    ua2 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919009;FBDM/{density=2.8125,width=1080,height=2162};FBLC/en_US;FBRV/340870045;FBCR/Robi;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/LE2117;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    ua3 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/RealmeChat;FBAV/1.0.0;FBBV/123456789;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/123456789;FBCR/Verizon;FBMF/Realme;FBBD/7;FBPN/com.realmechat;FBDV/Realme 7;FBSV/10;FBOP/30;FBCA/arm64-v8a;]','[FBAN/RealmeLite;FBAV/2.0.0;FBBV/987654321;FBDM/{density=3.0,width=1080,height=2400};FBLC/es_ES;FBRV/987654321;FBCR/T-Mobile;FBMF/Realme;FBBD/C15;FBPN/com.realmelite;FBDV/Realme C15;FBSV/10;FBOP/29;FBCA/arm64-v8a;]"
    ua4 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/316.1.0.28.104;FBBV/421951021;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBRV/135836670;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/8.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua9 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/196.0.0.22;FBPN/com.facebook.orca;FBLC/en_UM;FBBV/873542260;FBCR/EcoMobile;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi A90;FBSV/11.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.0,width=1280,height=1080};FB_FW/1;FBRV/539255817;]"
    ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/122.0.0.45.119;FBBV/268946150;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/261848295;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/6.0;nullFBCA/armeabi-v7a:armeabi;]"
    ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/67.0.0.38.165;FBBV/118946508;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/431876125;FBCR/"+fbcr+";FBMF/LG;FBBD/LS980;FBPN/com.facebook.katana;FBDV/LS980;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]"
    ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/33.0.0.32.62;FBBV/666395;FBDM/{density=2.5,width=480,height=800};FBLC/en_IN;FBCR/Red Pocket Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-G360BT;FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
    ua10 = "[FBAN/FB4A;FBAV/62.0.0.94.88;FBPN/com.facebook.katana;FBLC/en_US;FBBV/315190856;FBCR/KPNNL;FBMF/OPPO;FBBD/OPPO;FBDV/Find 5;FBSV/12.4.8;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.75,width=1440,height=2780};FB_FW/1;]"
    ua = str(random.choice([ua1,ua7,ua6,ua5]))  # Add ua6 to the list of choices
    ugeni.append(ua) # Append the randomly chosen user agent to the
