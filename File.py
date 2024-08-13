import random

ugeni = []
for agents in range(10000):
    samsung = random.choice(['MHA-L29','MHA-L09','MHA-AL00','MHA-TL00'])
    oppo = random.choice(['SM-G610F', 'SM-G610Y', 'SM-G610M', 'SM-G610'])
    vivo = random.choice(['SM-J250F','SM-J250G','SM-J250F','SM-J250M','SM-J250Y'])
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
    fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
    ft = ['SM-M625F', 'LM-K525', 'NID-1050', 'SM-A3051', 'CPH2069', 'RMX3286', 'A101XM', 'SM-A505GT', 'WKG-LX9', 'SM-A4260', 'Infinix X680C', 'RMX3265', 'GLA-LX1', 'Redmi 4X', 'V2204', 'vivo 2018', 'PCB-T104', '2201122G', 'Infinix X688B', 'RMP2106', 'OXF-AN10', 'Infinix X6835B', 'CPH2399', 'SM-F731B', 'SM-T515', 'CPH2209', 'M2101K6R', 'V2135', 'SM-M307FN', 'JLN-LX3', 'CPH2123', 'Lenovo TB-X605F', 'V2110', 'RMX3572', 'LM-X420']
    
    su = ['QP1A.190711.020', 'QKQ1.190918.001', 'TP1A.220624.014', 'SP1A.210812.016', 'QTG3.200617.002', 'SQ3A.220705.0040', 'RP1A.200720.011']
    so = random.choice(su)
    efg = random.choice(ft)
    
    ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946150;FBDM/{density=3.0,width=1440,height=2040};FBLC/en_GB;FBRV/269785748;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua2 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/338919009;FBDM/{density=2.8125,width=1080,height=2162};FBLC/en_US;FBRV/340870045;FBCR/Robi;FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/LE2117;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
    ua3 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/RealmeChat;FBAV/1.0.0;FBBV/123456789;FBDM/{density=3.0,width=1080,height=2400};FBLC/en_US;FBRV/123456789;FBCR/Verizon;FBMF/Realme;FBBD/7;FBPN/com.realmechat;FBDV/Realme 7;FBSV/10;FBOP/30;FBCA/arm64-v8a;]','[FBAN/RealmeLite;FBAV/2.0.0;FBBV/987654321;FBDM/{density=3.0,width=1080,height=2400};FBLC/es_ES;FBRV/987654321;FBCR/T-Mobile;FBMF/Realme;FBBD/C15;FBPN/com.realmelite;FBDV/Realme C15;FBSV/10;FBOP/29;FBCA/arm64-v8a;]"
    ua4 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/316.1.0.28.104;FBBV/421951021;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBRV/135836670;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/8.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
    ua9 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/196.0.0.22;FBPN/com.facebook.orca;FBLC/en_UM;FBBV/873542260;FBCR/EcoMobile;FBMF/Xiaomi;FBBD/Redmi;FBDV/Redmi A90;FBSV/11.1.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.0,width=1280,height=1080};FB_FW/1;FBRV/539255817;]"
    ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/76.0.0.87.50;FBBV/20748049;FBDM/{density=3.2,width=600,height=1024};FBLC/ky_KG;FBCR/Gomo;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-T111;FBSV/4.2;nullFBCA/armeabi-v7a:armeabi;]"
    ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/302.0.0.45.119;FBBV/268946150;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/371635748;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/6.0.1;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
    ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/76.0.0.87.50;FBBV/20748049;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.orca;FBDV/"+samsung;";FBSV/7.0;nullFBCA/armeabi-v7a:armeabi;]"
    ua8 = random.choice(["[FBAN/FB4A;FBAV/127.0.0.19.18;FBPN/com.facebook.katana;FBLC/en_US;FBBV/429059017;FBCR/ClaroNicaragua;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi 9i;FBSV/11.1.2;FBCA/armeabi- v7a:armeabi;FBDM/{density=2.125,width=720,height=1440};FB_FW/1;]","[FBAN/FB4A;FBAV/60.0.0.64.30;FBPN/com.facebook.katana;FBLC/en_US;FBBV/734909455;FBCR/CLAROArgentina;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi Note 9T;FBSV/15.0.2;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2183};FB_FW/1;]","[FBAN/FB4A;FBAV/351.0.0.85.32;FBPN/com.facebook.katana;FBLC/en_US;FBBV/162177917;FBCR/movistar;FBMF/samsung;FBBD/samsung;FBDV/Galaxy M51;FBSV/10.0.14393.222;FBCA/armeabi v7a:armeabi;FBDM/{density=2.625,width=1080,height=2322};FB_FW/1;]","[FBAN/FB4A;FBAV/305.0.0.28.17;FBPN/com.facebook.katana;FBLC/en_US;FBBV/579543474;FBCR/KolbiICE;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Mi 5s Plus;FBSV/10.3.3;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.0,width=1424,height=720};FB_FW/1;]","[FBAN/FB4A;FBAV/231.0.0.91.62;FBPN/com.facebook.katana;FBLC/en_US;FBBV/976718994;FBCR/TELCEL GSM;FBMF/samsung;FBBD/samsung;FBDV/A637;FBSV/12.5.1;FBCA/armeabi-v7a:armeabi;FBDM/(densidad=2.625,ancho=1080,alto=2342);FB_FW/1;]","[FBAN/FB4A;FBAV/396.0.0.78.43;FBPN/com.facebook.katana;FBLC/en_US;FBBV/685802561;FBCR/I TIM;FBMF/samsung;FBBD/samsung;FBDV/Galaxy Y Duos S6102;FBSV/15.2.1;FBCA/arm64-v8a:null;FBDM/{density=1.75,width=720,height=1381};FB_FW/1;]","[FBAN/FB4A;FBAV/254.0.0.26.52;FBPN/com.facebook.katana;FBLC/en_US;FBBV/703135100;FBCR/CC;FBMF/Xiaomi;FBBD/Xiaomi;FBDV/Redmi K60E;FBSV/12.1.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=1920,height=1200};FB_FW/1;]","[FBAN/FB4A;FBAV/20.0.0.69.74;FBPN/com.facebook.katana;FBLC/en_US;FBBV/468172877;FBCR/Nextel;FBMF/OPPO;FBBD/OPPO;FBDV/Reno6 5G;FBSV/13.1;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/(density=1.875,width=720,height=1465):FB_FW/1:FBRV/0;FB_FW/1;]"])
    ua = str(random.choice([ua5,ua7,ua6,ua9,ua1]))
    ugeni.append(ua)
