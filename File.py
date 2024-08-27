import random

ugeni = []
for agents in range(10000):
    samsung = random.choice(['SM-A326B','SM-A326B/DS','SM-A326BR/DS','SM-A326BR','SM-A326U','SM-A326W','SM-A326U1','SM-A326K','SCG08','SM-S326DL'])
    realme = random.choice(['RMX3195','RMX3197'])
    huawei = random.choice(['YAL-L21','YAL-L61','YAL-L71','YAL-L61D'])
    lg = random.choice(['vivo 1916', 'V1928A'])
    sony = random.choice(['X6511B','X6511','X6511E'])
    xiaomi = random.choice(['M2011K2C','M2011K2G'])
    oppo = random.choice(['VNS-L31','VNS-L21','VNS-L22','VNS-L23','VNS-L53','VNS-AL00','VNS-L62','VNS-L52','VNS-DL00','VNS-TL00','DIG-L22'])
    vivo = random.choice(['SM-J111F','SM-J110G','SM-J110F','SM-J110H','SM-J110M','SM-J110L','SM-J111M'])
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
    ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111, 555))+'.0.0.'+str(random.randrange(9, 49))+str(random.randint(11, 77))+";FBBV/"+str(random.randint(1111111, 7777777))+";[FBAN/Orca-Android;FBAV/27.0.0.34.79;FBBV/2351379;FBDM/{density=1.75,width=480,height=800};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
    ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111, 555))+'.0.0.'+str(random.randrange(9, 49))+str(random.randint(11, 77))+";FBBV/"+str(random.randint(1111111, 7777777))+";[FBAN/FB4A;FBAV/248.0.0.72.18;FBBV/1672945;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBRV/427953182;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/11;FBCA/arm64-v8a:;]"
    ua3 = "[FBAN/FB4A;FBAV/"+str(random.randint(11, 77))+'.0.0.'+str(random.randrange(9, 49))+str(random.randint(11, 77))+";FBBV/"+str(random.randint(1111111, 7777777))+";[FBAN/FB4A;FBAV/156.0.0.19.27;FBBV/2184026;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/487625183;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/6.0;FBCA/armeabi-v7a:armeabi;]"
    ua = random.choice([ua7,ua1, ua3])
    ugeni.append(ua)
