import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A305F','SM-A305FN','SM-A305G','SM-A305GN','SM-A305YN','SM-A3050','SM-A305N','SM-A305GT'])
	realme = random.choice(['SM-A326B','SM-A326B/DS','SM-A326BR/DS','SM-A326BR','SM-A326U','SM-A326W','SM-A326U1','SM-A326K','SCG08','SM-S326DL'])
	oppo = random.choice(['MLA-L01/L11','MLA-L11','MLA-L02/L12','MLA-L02','MLA-L12','MLA-L03/L13','MLA-L03','MLA-L13','MLA-AL10','MLA-L01'])
	lg = random.choice(['D838','F350S','F350L','F350K'])
	sony = random.choice(['D2203','D2206','D2243','D2202'])
	vivo = random.choice(['SM-G885F','SM-G8850','SM-G885Y','SM-G885S','SM-G8858'])
	fbcr = random.choice(["Telenor","Ufone","Zong","Jazz","Jazz 4G","Mobilink","Zong 4G","Zong CmPak"])
	fblc = random.choice(['en_US','en_GB','en_PK','ur_PK'])
	ft = ['SM-M625F','LM-K525', 'NID-1050','SM-A3051','CPH2069','RMX3286','A101XM','SM-A505GT','WKG-LX9','SM-A4260','Infinix X680C','RMX3265','GLA-LX1','Redmi 4X','V2204','vivo 2018','PCB-T104','2201122G','Infinix X688B','RMP2106','OXF-AN10','Infinix X6835B','CPH2399','SM-F731B','SM-T515','CPH2209','M2101K6R','V2135','SM-M307FN','JLN-LX3','CPH2123','Lenovo TB-X605F','V2110','RMX3572','LM-X420']
	su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
	so = random.choice(su)
	efg = random.choice(ft)
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/173.0.0.54.72;FBBV/3719472;FBDM/{density=2.75,width=800,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/7.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/83.0.0.16.39;FBBV/1847294;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/6.0.1;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua4 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/83.0.0.16.39;FBBV/527644830;FBDM/{density=1.75,width=480,height=854};FBLC/en_GB;FBRV/261732958;FBCR/Zong 4G;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/"+sony+";FBSV/4.4.2;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/226.0.0.28.95;FBBV/31389908;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/LGE;FBBD/LGE;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/10.0.0.47.73;FBBV/5818742;FBDM/{density=3.0,width=1080,height=2220};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/8.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/38.0.0.0.18;FBBV/5818742;FBDM/{density=2.75,width=720,height=1480};FBLC/en_US;FBCR/MobileNation;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/Samsung Galaxy A54 5G;FBSV/8.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/154.0.0.14.27;FBBV/5816369;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBRV/371948591;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua3 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/257.0.0.17.137;FBBV/20454026;FBDM/{density=3.0,width=1080,height=2400};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2059;FBSV/10;FBCA/arm64-v8a:;]"
	ua = str(random.choice([ua2,ua4,ua3,ua5,ua7,ua1]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
