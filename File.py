import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A205F','SM-A205FN','SM-A205GN','SM-A205YN','SM-A205G','SM-A205W','SM-A205U','SM-A205S','SM-S205DL','SM-A205U1'])
	realme = random.choice(['CPH1723','CPH1727','CHP1723','CHP1727'])
	oppo = random.choice(['TRT-L53','TRT-L21A','TRT-AL00','SLA-TL10','TRT-TL10','SLA-AL00','TRT-AL00A'])
	lg = random.choice(['X6812', 'X6812B'])
	sony = random.choice(['vivo 1907','V1907','vivo 1907_19','V1913A'])
	vivo = random.choice(['SM-G570F','SM-G570F/DD','SM-G570F','SM-G570Y','SM-G570M'])
	fbcr = random.choice(["Zong","Jazz","Zong 4G","Zong CMPak","UFONE-PK","Ufone","Telenor","Telecom","LTE"])
	fblc = random.choice(['en_US','en_GB','en_PK','ur_PK'])
	ft = ['SM-M625F','LM-K525', 'NID-1050','SM-A3051','CPH2069','RMX3286','A101XM','SM-A505GT','WKG-LX9','SM-A4260','Infinix X680C','RMX3265','GLA-LX1','Redmi 4X','V2204','vivo 2018','PCB-T104','2201122G','Infinix X688B','RMP2106','OXF-AN10','Infinix X6835B','CPH2399','SM-F731B','SM-T515','CPH2209','M2101K6R','V2135','SM-M307FN','JLN-LX3','CPH2123','Lenovo TB-X605F','V2110','RMX3572','LM-X420']
	su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
	so = random.choice(su)
	efg = random.choice(ft)
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/173.0.0.54.72;FBBV/3719472;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX1925;FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/83.0.0.16.39;FBBV/1847294;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua4 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/83.0.0.16.39;FBBV/5274830;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/"+sony+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/122.0.0.18.63;FBBV/389908;FBDM/{density=3.0,width=1080,height=2480};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/47.0.0.12.63;FBBV/1848285;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/213.0.0.41.24;FBBV/3712948;FBDM/{density=2.75,width=720,height=1560};FBLC/"+fblc+";FBRV/281639673;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua3 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/257.0.0.17.137;FBBV/2184026;FBDM/{density=2.75,width=720,height=1560};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1923;FBSV/9.0;FBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua6,ua5,ua7,ua2,ua4,ua1,ua3]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
