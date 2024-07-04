import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A217F','SM-A217F/DS','SM-A217F/DSN','SM-A217M','SM-A217M/DS','SM-A217N'])
	realme = random.choice(['RMX2142','RMX2081','RMX2085','RMX2083'])
	oppo = random.choice(['GLK-LX1','GLK-LX2','GLK-LX3','GLK-LX1U','GLK-AL00','GLK-TL00'])
	lg = random.choice(['CPH1937','CPH1939','CPH1941'])
	sony = random.choice(['Infinix_X689B','Infinix_X689','Infinix_X689D'])
	xiaomi = random.choice(['2109119DG','2107119DC','2109119DI'])
	vivo = random.choice(['SM-J737F','SM-J737V','SM-J737T','SM-J737A','SM-J737P','SM-J737T1','SM-J737U','SM-J737S'])
	fbcr = random.choice(["Zong","Jazz","Zong 4G","Zong CMPak","Jio 4G","null","Banglalink","Telenor","UFONE-PK"])
	fblc = random.choice(['en_US','en_GB','en_PK','ur_PK'])
	ft = ['SM-M625F','LM-K525', 'NID-1050','SM-A3051','CPH2069','RMX3286','A101XM','SM-A505GT','WKG-LX9','SM-A4260','Infinix X680C','RMX3265','GLA-LX1','Redmi 4X','V2204','vivo 2018','PCB-T104','2201122G','Infinix X688B','RMP2106','OXF-AN10','Infinix X6835B','CPH2399','SM-F731B','SM-T515','CPH2209','M2101K6R','V2135','SM-M307FN','JLN-LX3','CPH2123','Lenovo TB-X605F','V2110','RMX3572','LM-X420']
	su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
	so = random.choice(su)
	efg = random.choice(ft)
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/112.0.0.75.49;FBBV/3719472;FBDM/{density=3.0,width=1080,height=2400};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/89.0.0.37.72;FBBV/1847294;FBDM/{density=3.0,width=1080,height=2310};FBLC/"+fblc+";FBRV/243196785;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua4 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/26.0.0.48.61;FBBV/5274830;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+"FBCR/"+fbcr+";FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/vivo 1804;FBSV/8.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/167.0.0.83.27;FBBV/389908;FBDM/{density=3.0,width=1080,height=1640};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/"+sony+";FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/10.0.0.47.73;FBBV/5818742;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/8.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/38.0.0.0.18;FBBV/5818742;FBDM/{density=3.0,width=1080,height=2400};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.orca;FBDV/"+xiaomi+";FBSV/11;FBCA/arm64-v8a:;]"
	ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/129.0.0.57.168;FBBV/5816369;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBRV/471924712;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/10;FBOP/12;FBCA/arm64-v8a:;]"
	ua3 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/257.0.0.17.137;FBBV/2184026;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBRV/0;FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/9.0;FBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua6,ua5,ua7,ua2,ua4,ua1,ua3,ua10]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
