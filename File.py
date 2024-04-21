import random
ugen = []
for agents in range(10005):
	samsung = random.choice(['SM-A505F','SM-A505FN','SM-A505GN','SM-A505G','SM-A505FM','SM-A505YN','SM-A505W','SM-A505X','SM-A505U','SM-A505GT','SM-A505U1','SM-A505G','SM-A505N','SM-S506DL'])
	oppo = random.choice(['CPH1909','CPH1920','CPH1912'])
	vivo = random.choice(['LM-Q610','LM-Q610.FG','LM-Q610.FGN','LM-Q610(FGN)','LM-Q610.YN','LM-Q725L','LM-Q725K','LM-Q725S'])
	realme = random.choice(['RMX1911','RMX1919','RMX1927'])
	ft = ['SM-M625F','LM-K525', 'NID-1050','SM-A3051','CPH2069','RMX3286','A101XM','SM-A505GT','WKG-LX9','SM-A4260','Infinix X680C','RMX3265','GLA-LX1','Redmi 4X','V2204','vivo 2018','PCB-T104','2201122G','Infinix X688B','RMP2106','OXF-AN10','Infinix X6835B','CPH2399','SM-F731B','SM-T515','CPH2209','M2101K6R','V2135','SM-M307FN','JLN-LX3','CPH2123','Lenovo TB-X605F','V2110','RMX3572','LM-X420']
	an = ['9','8']
	aru = ['{density=3.0,width=1080,height=2480}','{density=2.75,width=720,height=1612}','{density=3.0,width=1080,height=2400}','{density=2.75,width=720,height=1520}','{density=3.0,width=1080,height=2408}','{density=3.0,width=1080,height=2340}','{density=3.0,width=1080,height=2376}','{density=3.0,width=1080,height=2404}','{density=3.0,width=1080,height=2404}','{density=2.75,width=720,height=1280}','{density=3.0,width=1080,height=2408}','{density=2.75,width=720,height=1440}','{density=2.75,width=720,height=1280}','{density=3.0,width=1080,height=2448}','{density=3.0,width=1080,height=2448}','{density=3.0,width=1080,height=2448}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2412}','{density=3.0,width=1080,height=2160}','{density=3.0,width=1440,height=3040}','{density=3.0,width=1080,height=2340}','{density=3.0,width=1080,height=2340}','{density=3.0,width=1080,height=2340}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1440,height=3120}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2400}','{density=2.75,width=720,height=1640}','{density=2.75,width=720,height=1440}','{density=2.75,width=720,height=1600}','{density=2.75,width=720,height=1600}','{density=3.0,width=1080,height=2408}','{density=3.0,width=1080,height=2408}','{density=3.0,width=1080,height=2408}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2246}','{density=3.0,width=1080,height=2400}','{density=2.75,width=720,height=1612}']
	su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
	xg = ['armeabi-v7a:armeabi','arm64-v8a','armeabi-v8a:armeabi','arm64-v8a:armeabi']
	fr = ['en_US','en_GB','es_LA','fr_FR','en_PK','id_IN']
	cv = ['airtel','IND airtel','Nepal Telecom','Jio 4G','Jazz','UFONE','Zong 4G','Telenor']
	ap = random.choice(fr)
	af = random.choice(aru)
	fd = random.choice(cv)
	ux = random.choice(an)
	fo = random.choice(xg)
	efg = random.choice(ft)
	so = random.choice(su)
	ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027740;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBRV/0;FBCR/Iliad;FBMF/Meizu;FBBD/Meizu;FBPN/com.facebook.katana;FBDV/M6 Note;FBSV/7.1.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/186.0.0.40.121;FBBV/489186927;FBDM/{density=2.75,width=720,height=1600};FBLC/"+ap+";FBRV/381936593;FBCR/"+fd+";FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua3 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/336.0.0.40.121;FBBV/927195715;FBDM/{density=2.5,width=720,height=1520};FBLC/"+ap+";FBRV/185714729;FBCR/"+fd+";FBMF/oppo;FBBD/oppo;FBPN/com.facebook.katana;FBDV/CPH1955;FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua4 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/316.1.0.28.104;FBBV/421951021;FBDM/{density=3.0,width=1080,height=2160};FBLC/"+ap+";FBRV/431726670;FBCR/"+fd+";FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/"+vivo+";FBSV/8.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua6 = random.choice([
    "[FBAN/FB4A;FBAV/336.0.0.40.121;FBBV/4433241;FBDM/{density=2.75,width=720,height=1600};FBLC/en_PK;FBRV/185719264;FBCR/IND airtel;FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/LM-K420;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
    "[FBAN/FB4A;FBAV/460.0.0.34.89;FBBV/588414891;FBDM/{density=2.0,width=720,height=1507};FBLC/en_GB;FBRV/0;FBCR/Warid;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/22120RN86G;FBSV/13;FBOP/1;FBCA/arm64-v8a:;]",
    "[FBAN/FB4A;FBAV/336.0.0.40.121;FBBV/4433241;FBDM/{density=3.0,width=1440,height=3120};FBLC/en_GB;FBRV/384618284;FBCR/Jazz;FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/PAR-AL00;FBSV/8.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
    "[FBAN/FB4A;FBAV/453.0.0.40.107;FBBV/570632523;FBDM/{density=2.0,width=720,height=1464};FBLC/en_US;FBRV/573679895;FBCR/;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBPN/com.facebook.katana;FBDV/TECNO LD7;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
    "[FBAN/Orca-Android;FBAV/453.0.0.38.109;FBPN/com.facebook.orca;FBLC/en_US;FBBV/586043100;FBCR/Zong;FBMF/INFINIX;FBBD/Infinix;FBDV/Infinix X6836;FBSV/13;FBCA/arm64-v8a:null;FBDM/{density=3.0,width=1080,height=2352};FB_FW/1;]",
    "[FBAN/FB4A;FBAV/454.1.0.49.104;FBBV/575565987;FBDM/{density=2.0,width=1464,height=720};FBLC/en_US;FBRV/0;FBCR/Ufone;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X690B;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]",
    "[FBAN/FB4A;FBAV/427.0.0.31.63;FBBV/502904154;FBDM/{density=2.0,width=720,height=1440};FBLC/en_US;FBRV/0;FBCR/;FBMF/INFINIX MOBILITY LIMITED;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/Infinix X653C;FBSV/9;FBOP/1;FBCA/armeabi-v7a:armeabi;]",
    "[FBAN/EMA;FBBV/572287848;FBAV/397.0.0.11.117;FBDV/Infinix X653C;FBLC/en_US;FBNG/4G;FBMNT/METERED;FBDM/{density=2.0}]",
    "[FBAN/FB4A;FBAV/426.0.0.26.50;FBBV/500449081;FBDM/{density=2.0,width=720,height=1365};FBLC/ur_PK;FBRV/0;FBCR/ZONG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-M015G;FBSV/11;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
    "[FBAN/FB4A;FBAV/459.1.0.42.84;FBBV/586444216;FBDM/{density=2.625,width=1080,height=1920};FBLC/en_GB;FBRV/0;FBCR/ZONG;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J730F;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]",
    "[FBAN/FB4A;FBAV/444.0.0.31.114;FBBV/546214355;FBDM/{density=2.0,width=720,height=1371};FBLC/en_US;FBRV/0;FBCR/Zong CMPak;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.katana;FBDV/moto g(7) power;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
])
	ua = str(random.choice([ua1,ua2,ua3,ua4,ua6]))  # Add ua6 to the list of choices
	ugen.append(ua1)  # Append the randomly chosen user agent to the ugen list
