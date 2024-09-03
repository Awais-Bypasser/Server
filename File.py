import random

ugeni = []
for agents in range(10000):
    samsung = random.choice(['SM-G750F', 'SM-G7508', 'SM-G7508Q', 'SM-G750H', 'SM-G750A'])
    realme = random.choice(['RMX1992', 'RMX1993', 'RMX1991'])
    oppo = random.choice(['CAG-L02', 'CAG-L22', 'CAG-L23', 'CAG-L03'])
    lg = random.choice(['CPH2035', 'CPH2037', 'CPH2036'])
    sony = random.choice(['Infinix_X625', 'Infinix_X625B', 'Infinix_X625D'])
    xiaomi = random.choice(['23100RN82L', '23106RN0DA', '23108RN04Y', '2311DRN14I'])
    vivo = random.choice(['SM-T715', 'SM-T710', 'SM-T719N', 'SM-T719', 'SM-T715Y', 'SM-T719Y', 'SM-T713'])
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
    fblc = "en_US"
    ft = ['SM-M625F', 'LM-K525', 'NID-1050', 'SM-A3051', 'CPH2069', 'RMX3286', 'A101XM', 'SM-A505GT', 'WKG-LX9', 'SM-A4260', 'Infinix X680C', 'RMX3265', 'GLA-LX1', 'Redmi 4X', 'V2204', 'vivo 2018', 'PCB-T104', '2201122G', 'Infinix X688B', 'RMP2106', 'OXF-AN10', 'Infinix X6835B', 'CPH2399', 'SM-F731B', 'SM-T515', 'CPH2209', 'M2101K6R', 'V2135', 'SM-M307FN', 'JLN-LX3', 'CPH2123', 'Lenovo TB-X605F', 'V2110', 'RMX3572', 'LM-X420']
    su = ['QP1A.190711.020', 'QKQ1.190918.001', 'TP1A.220624.014', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011']
    so = random.choice(su)
    efg = random.choice(ft)
    
    ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111, 555))+'.0.0.'+str(random.randrange(9, 49))+str(random.randint(11, 77))+";FBBV/"+str(random.randint(1111111, 7777777))+";[FBAN/FB4A;FBAV/112.0.0.75.49;FBBV/5891723;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111, 555))+'.0.0.'+str(random.randrange(9, 49))+str(random.randint(11, 77))+";FBBV/"+str(random.randint(1111111, 7777777))+";[FBAN/FB4A;FBAV/17.0.0.37.72;FBBV/184729472;FBDM/{density=1.75,width=480,height=854};FBLC/"+fblc+";FBRV/243196785;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/8.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua4 = "[FBAN/FB4A;FBAV/"+str(random.randint(111, 555))+'.0.0.'+str(random.randrange(9, 49))+str(random.randint(11, 77))+";FBBV/"+str(random.randint(1111111, 7777777))+";[FBAN/FB4A;FBAV/26.0.0.48.61;FBBV/4671823;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2029;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111, 555))+'.0.0.'+str(random.randrange(9, 49))+str(random.randint(11, 77))+";FBBV/"+str(random.randint(1111111, 7777777))+";[FBAN/FB4A;FBAV/167.0.0.83.27;FBBV/3104738;FBDM/{density=2.75,width=720,height=1520};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/"+sony+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111, 555))+'.0.0.'+str(random.randrange(9, 49))+str(random.randint(11, 77))+";FBBV/"+str(random.randint(1111111, 7777777))+";[FBAN/Orca-Android;FBAV/10.0.0.47.73;FBBV/1047284;FBDM/{density=3.0,width=1536,height=2048};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
    ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11, 77))+'.0.0.'+str(random.randrange(9, 49))+str(random.randint(11, 77))+";FBBV/"+str(random.randint(1111111, 7777777))+";[FBAN/Orca-Android;FBAV/38.0.0.0.18;FBBV/3619526;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.orca;FBDV/"+xiaomi+";FBSV/13;FBCA/arm64-v8a:;]"
    ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111, 555))+'.0.0.'+str(random.randrange(9, 49))+str(random.randint(11, 77))+";FBBV/"+str(random.randint(1111111, 7777777))+";[FBAN/FB4A;FBAV/169.0.0.57.168;FBBV/5816369;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/341524712;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/4.4.3;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
    ua3 = "[FBAN/FB4A;FBAV/"+str(random.randint(11, 77))+'.0.0.'+str(random.randrange(9, 49))+str(random.randint(11, 77))+";FBBV/"+str(random.randint(1111111, 7777777))+";[FBAN/FB4A;FBAV/257.0.0.17.137;FBBV/2184026;FBDM/{density=3.0,width=1080,height=2400};FBLC/"+fblc+";FBRV/185753291;FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/10;FBCA/arm64-v8a:;]"
    
    ua = random.choice([ua6, ua5, ua7, ua2, ua4, ua1, ua3, ua10])
    ugeni.append(ua)
