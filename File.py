import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-S916B','SM-S916U','SM-S916U1','SM-S916W','SM-S916N','SM-S9160','SM-S916E'])
	realme = random.choice(['RMX2030', 'RMX2032'])
	oppo = random.choice(['FLA-AL10, FLA-AL00, FLA-LX1, FLA-LX2, FLA-LX3, LDN-AL00, FLA-AL20, FLA-TL10'])
	lg = random.choice(['V2204','V2214'])
	vivo1 = random.choice(['22101316UCP','22101316UG'])
	sony = random.choice(['H9436','H8416','H9493'])
	vivo = random.choice(['SM-A605FN','SM-A605G','SM-A605F','SM-A605GN','SM-A6050','SM-A605K','SM-A605X','SM-A6058'])
	fbcr = random.choice(["Airtel","Jio","BSNL","Mobitel","Nepal Telecom","Globe Telecom","Mobifone","Warid","Banglalink","Grameenphone","Robi"])
	fblc = random.choice(['id_ID','en_BD','en_PK','ja_JP','zh_TW','zh_HK','zh_CN'])
	ft = ['SM-M625F','LM-K525', 'NID-1050','SM-A3051','CPH2069','RMX3286','A101XM','SM-A505GT','WKG-LX9','SM-A4260','Infinix X680C','RMX3265','GLA-LX1','Redmi 4X','V2204','vivo 2018','PCB-T104','2201122G','Infinix X688B','RMP2106','OXF-AN10','Infinix X6835B','CPH2399','SM-F731B','SM-T515','CPH2209','M2101K6R','V2135','SM-M307FN','JLN-LX3','CPH2123','Lenovo TB-X605F','V2110','RMX3572','LM-X420']
	su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
	so = random.choice(su)
	efg = random.choice(ft)
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/113.0.0.43.29;FBBV/3719472;FBDM/{density=3.0,width=1080,height=2412};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3491;FBSV/11;FBOP/12;FBCA/arm64-v8a:;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/83.0.0.16.39;FBBV/1847294;FBDM/{density=3.0,width=1080,height=2160};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/8.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua4 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/317.0.0.64.95;FBBV/5274830;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/12;FBOP/12;FBCA/arm64-v8a:;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/122.0.0.18.63;FBBV/389908;FBDM/{density=3.0,width=1080,height=2160};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/LGE;FBBD/LGE;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/7.1.1;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/64.0.0.51.27;FBBV/3494127;FBDM/{density=2.75,width=1080,height=2220};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/8.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/141.0.0.67.28;FBBV/5714827;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBRV/173571859;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/13;FBOP/14;FBCA/arm64-v8a:;]"
	ua3 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/257.0.0.17.137;FBBV/2184026;FBDM/{density=3.0,width=1080,height=2400};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/"+vivo1+";FBSV/12;FBCA/arm64-v8a:;]"
	ua8 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/172.0.0.37.61;FBBV/5812586;FBDM/{density=3.0,width=1440,height=2880};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/"+sony+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua5,ua7,ua1,ua3,ua8]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
