import random
ugeni = []
for agents in range(10005):
	samsung = random.choice(['SM-A505F','SM-A505FN','SM-A505GN','SM-A505G','SM-A505FM','SM-A505YN','SM-A505W','SM-A505X','SM-A505U','SM-A505GT','SM-A505U1','SM-A505G','SM-A505N','SM-S506DL'])
	oppo = random.choice(['CPH1909','CPH1920','CPH1912'])
	vivo = random.choice(['LM-Q610','LM-Q610.FG','LM-Q610.FGN','LM-Q610(FGN)','LM-Q610.YN','LM-Q725L','LM-Q725K','LM-Q725S'])
	realme = random.choice(['RMX1911','RMX1919','RMX1927'])
	ft = ['SM-M625F','LM-K525', 'NID-1050','SM-A3051','CPH2069','RMX3286','A101XM','SM-A505GT','WKG-LX9','SM-A4260','Infinix X680C','RMX3265','GLA-LX1','Redmi 4X','V2204','vivo 2018','PCB-T104','2201122G','Infinix X688B','RMP2106','OXF-AN10','Infinix X6835B','CPH2399','SM-F731B','SM-T515','CPH2209','M2101K6R','V2135','SM-M307FN','JLN-LX3','CPH2123','Lenovo TB-X605F','V2110','RMX3572','LM-X420']
	an = ['4.0.3','4.4.2']
	aru = ['{density=3.0,width=1080,height=2480}','{density=2.75,width=720,height=1612}','{density=3.0,width=1080,height=2400}','{density=2.75,width=720,height=1520}','{density=3.0,width=1080,height=2408}','{density=3.0,width=1080,height=2340}','{density=3.0,width=1080,height=2376}','{density=3.0,width=1080,height=2404}','{density=3.0,width=1080,height=2404}','{density=2.75,width=720,height=1280}','{density=3.0,width=1080,height=2408}','{density=2.75,width=720,height=1440}','{density=2.75,width=720,height=1280}','{density=3.0,width=1080,height=2448}','{density=3.0,width=1080,height=2448}','{density=3.0,width=1080,height=2448}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2412}','{density=3.0,width=1080,height=2160}','{density=3.0,width=1440,height=3040}','{density=3.0,width=1080,height=2340}','{density=3.0,width=1080,height=2340}','{density=3.0,width=1080,height=2340}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1440,height=3120}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2400}','{density=2.75,width=720,height=1640}','{density=2.75,width=720,height=1440}','{density=2.75,width=720,height=1600}','{density=2.75,width=720,height=1600}','{density=3.0,width=1080,height=2408}','{density=3.0,width=1080,height=2408}','{density=3.0,width=1080,height=2408}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2400}','{density=3.0,width=1080,height=2246}','{density=3.0,width=1080,height=2400}','{density=2.75,width=720,height=1612}']
	su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
	xg = ['armeabi-v7a:armeabi','arm64-v8a','armeabi-v8a:armeabi','arm64-v8a:armeabi']
	fr = ['en_US','en_GB','es_LA','fr_FR','en_PK','id_IN']
	cv = ['Airtel','IND airtel','Jazz','UFONE']
	ap = random.choice(fr)
	af = random.choice(aru)
	fd = random.choice(cv)
	ux = random.choice(an)
	fo = random.choice(xg)
	efg = random.choice(ft)
	so = random.choice(su)
	ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027740;FBDM/{density=2.6,width=800,height=1280};FBLC/+ap+;FBRV/271947196;FBCR/"+fd+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/GT-N8010;FBSV/4.0.3;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua2 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/186.0.0.40.121;FBBV/489186927;FBDM/{density=2.75,width=720,height=1600};FBLC/"+ap+";FBRV/381936593;FBCR/"+fd+";FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua3 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/336.0.0.40.121;FBBV/927195715;FBDM/{density=2.5,width=720,height=1520};FBLC/"+ap+";FBRV/185714729;FBCR/"+fd+";FBMF/oppo;FBBD/oppo;FBPN/com.facebook.katana;FBDV/CPH1955;FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua4 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/316.1.0.28.104;FBBV/421951021;FBDM/{density=3.0,width=1080,height=2160};FBLC/"+ap+";FBRV/431726670;FBCR/"+fd+";FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/"+vivo+";FBSV/8.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/72.0.0.78.20;FBBV/142900020;FBDM/{density=4.8,width=720,height=1280};FBLC/en_PG;FBCR/Snapfon;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-G550T;FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua1,ua6]))  # Add ua6 to the list of choices
	ugeni.append(ua1)  # Append the randomly chosen user agent to the ugen list
