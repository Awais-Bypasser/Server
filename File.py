import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A015F','SM-A015F/DS','SM-A015G','SM-A015G/DS','SM-A015M','SM-A015M/DS','SM-A015T1','SM-S111DL','SM-A015V','SM-A015A','SM-A015AZ','SM-A015U','SM-A015U1'])
	realme = random.choice(['RMX1825','RMX1821','realme 1821'])
	oppo = random.choice(['TRT-L53','TRT-L21A','TRT-AL00','SLA-TL10','TRT-TL10','SLA-AL00','TRT-AL00A'])
	lg = random.choice(['X662','X662B','X689F'])
	sony = random.choice(['vivo 1907','V1907','vivo 1907_19','V1913A'])
	vivo = random.choice(['SM-G950FD','SM-G950W','SM-G950S','SM-G950K','SM-G950L','SM-G9500','SM-G950A','SM-G950P','SM-G950T','SM-G950U','SM-G950V','SM-G950F','SM-G950U1','SM-G950N','SC-02J','SCV36','SM-G950','G950F'])
	ft = ['SM-M625F','LM-K525', 'NID-1050','SM-A3051','CPH2069','RMX3286','A101XM','SM-A505GT','WKG-LX9','SM-A4260','Infinix X680C','RMX3265','GLA-LX1','Redmi 4X','V2204','vivo 2018','PCB-T104','2201122G','Infinix X688B','RMP2106','OXF-AN10','Infinix X6835B','CPH2399','SM-F731B','SM-T515','CPH2209','M2101K6R','V2135','SM-M307FN','JLN-LX3','CPH2123','Lenovo TB-X605F','V2110','RMX3572','LM-X420']
	su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
	so = random.choice(su)
	efg = random.choice(ft)
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
	fblc = random.choice(['ar_AE','ar_BH','ar_DJ','ar_DZ','ar_EG','ar_EH','ar_ER','ar_IL','ar_IQ','ar_JO','ar_KM','ar_KW','ar_LB','ar_LY','ar_MA','ar_MR','ar_OM','ar_PS','ar_QA','ar_SA','ar_SD','ar_SO','ar_SS','ar_SY','ar_TD','ar_TN','ar_YE','bas_CM','bez_TZ','bn_BD','bn_IN','bo_CN','bo_IN','br','br_FR','ca_AD','ca_ES','ca_FR','ca_IT','chr_US','cy_GB','de_AT','de_BE','de_CH','de_DE','de_IT','de_LI','de_LU','dje_NE','dsb','dsb_DE','dyo_SN','dz_BT','ebu_KE','ee','ee_GH','ee_TG','el_CY','el_GR','en_AG','en_AI','en_AS','en_AT','en_AU','en_BB','en_BE','en_BI','en_BM','en_BS','en_BW','en_BZ','en_CA','en_CC','en_CH','en_CK','en_CM','en_CX','en_DE','en_DG','en_DK','en_DM','en_ER','en_FI','en_FJ','en_FK','en_FM','en_GB','en_GD','en_GG','en_GH','en_GI','en_GM','en_GU','en_GY','en_HK','en_IE','en_IL','en_IM','en_IN','en_IO','en_JE','en_JM','en_KE','en_KI','en_KN','en_KY','en_LC','en_LR','en_LS','en_MG','en_MH','en_MO','en_MP','en_MS','en_MT','en_MU','en_MW','en_MY','en_NA','en_NF','en_NG','en_NL','en_NR','en_NU','en_NZ','en_PG','en_PH','en_PK','en_PN','en_PR','en_PW','en_RW','en_SB','en_SC','en_SD','en_SE','en_SG','en_SH','en_SI','en_SL','en_SS','en_SX','en_SZ','en_TC','en_TK','en_TO','en_TT','en_VI','en_VU','en_WS','en_ZA','des_HN','es_IC','es_MX','es_NI','es_PA','es_PE','es_PR','es_PY','es_SV','es_US','es_UY','es_VE','et_EE','eu_ES','fa_AF','fa_IR','ff_CM','ff_GN','ff_MR','ff_SN','fi','fi_FI','fil','fil_PH','fo','fo_DK','fo_FO','fr','fr_BE','fr_BF','fr_BI','fr_BJ','fr_BL','fr_CA','fr_CD','fr_CF','fr_CG','fr_CH','fr_CI','fr_CM','fr_DJ','fr_DZ','fr_HT','fr_KM','fr_LU','fr_MA','fr_MC','fr_MF','fr_MG','fr_ML','fr_MQ','fr_MR','fr_MU','fr_NC','fr_NE','fr_PF','fr_PM','fr_RE','fr_RW','fr_SC','fr_SN','fr_SY','fr_TD','fr_TG','fr_TN','fr_VU','fr_WF','fr_YT','fur','fur_IT','fy','fy_NL','ga','ga_IE','gl_ES','gsw','gsw_CH','gsw_FR','gsw_LI','gu_IN','guz','guz_KE','gv','gv_IM','ha','ha_GH','ha_NE','ha_NG','haw','haw_US','he','he_IL','hi','hi_IN','hr','hr_BA','hr_HR','hsb','hsb_DE','hu','hu_HU','hy','hy_AM','ig','ig_NG','ii','ii_CN','in_ID','is','is_IS','it','it_CH','it_IT','it_SM','it_VA','iw','iw_IL','ja','ja_JP','jgo','jgo_CM','jmc','jmc_TZ','ka','ka_GE','kab','kab_DZ','kam','kam_KE','kde','kde_TZ','kea','kea_CV','khq','khq_ML','ki','ki_KE','kk','kk_KZ','kkj','kkj_CM','kl','kl_GL','kln','kln_KE','km','km_KH','kn','kn_IN','ko','ko_KP','ko_KR','kok','kok_IN','ks','ks_IN','ksb','ksb_TZ','ksh','ksh_DE','kw','kw_GB','ky','ky_KG','lag','lag_TZ','lt','lt_LT','lb','lb_LU','lv','lv_LV','lg','lg_UG','mk','mk_MK','ml','ml_IN','mr','mr_IN','ms','ms_MY','mt','mt_MT','nl','nl_BE','nl_NL','no','no_NO','no_NO_NY','pl','pl_PL','pt','pt_AO','pt_BR','pt_CH','pt_CV','pt_GQ','pt_GW','pt_LU','pt_MO','pt_MZ','pt_PT','pt_ST','pt_TL','ro','ro_RO','ru','ru_BY','ru_KG','ru_KZ','ru_MD','ru_RU','ru_UA','sk','sk_SK','sl','sl_SI','sq','sq_AL','sr','sr_BA','sr_CS','sr_ME','sr_RS','sv_SE','th_TH','th_TH_TH','tr_TR','vi_VN','zh_Hans','uz_UZ','uk_UA','zh_Hans_HK','zh_Hans_MO','zh_Hans_SG','zh_Hant','zh_Hant_HK','zh_Hant_MO','zh_Hant_TW','zh_HK','zu_ZA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/173.0.0.54.72;FBBV/3719472;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/83.0.0.16.39;FBBV/1847294;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua4 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/83.0.0.16.39;FBBV/5274830;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/"+sony+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/122.0.0.18.63;FBBV/389908;FBDM/{density=3.0,width=1080,height=2408};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/INFINIX;FBBD/INFINIX;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/47.0.0.12.63;FBBV/1848285;FBDM/{density=2.75,width=1440,height=2960};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/7.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/213.0.0.41.24;FBBV/3712948;FBDM/{density=2.75,width=720,height=1520};FBLC/"+fblc+";FBRV/281639673;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	ua3 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/257.0.0.17.137;FBBV/2184026;FBDM/{density=2.75,width=720,height=1612};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/CPH2389;FBSV/12;FBCA/arm64-v8a:;]"
	ua = str(random.choice([ua6,ua7,ua2,ua1,ua3]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
