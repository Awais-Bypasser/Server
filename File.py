import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-G930A','SM-G930P','SM-G930V','SM-G930T','SM-G930R','SM-G930F','SM-G930U','SM-G930R4','SM-G930T1','SM-G930VL','SM-G930AZ','SM-G930R6','SM-G930R7'])
	realme = random.choice(['E973','E971','E975','F180L','F180K','F180S'])
	oppo = random.choice(['NEM-UL10','NEM-TL00H','NEM-L21','NMO-L31','NMO-L22','NMO-L23','NMO-L01','NEM-L22','NEM-L51','NEM-AL10','NEM-TL00'])
	vivo = random.choice(['SM-A5100','SM-A510F','SM-A510M','SM-A510Y','SM-A510FD','SM-A5108','SM-A510S','SM-A510K','SM-A510L','SM-A510'])
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
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401182;FBDM/{density=3.0,width=1440,height=2560};FBLC/"+fblc+";FBRV/274073372;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/173957193;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/44.0.0.8.52;FBPN/com.facebook.orca;FBLC/en_US;FBBV/16048044;FBCR/cricket;FBMF/zte;FBBD/zte;FBDV/Z987;FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=720,height=1184};FB_FW/1;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/149.0.0.40.71;FBBV/79007703;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/79424004;FBCR/vodafone P;FBMF/ZTE;FBBD/ZTE;FBPN/com.facebook.katana;FBDV/NOS NOVU II;FBSV/5.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/285816295;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/"+vivo+";FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/196.0.0.29.99;FBPN/com.facebook.orca;FBLC/th_TH;FBBV/135374479;FBCR/AIS;FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};FB_FW/1;]"
	ua = str(random.choice([ua5,ua7,ua6]))  # Add ua6 to the list of choices
	ugeni.append(ua) # 
