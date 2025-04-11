import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-T387','SM-T387W','SM-T387V','SM-T387AA','SM-T387T'])
	realme = random.choice(['RMX3310','RMX3312','RMX3311'])
	oppo = random.choice(['GRA-UL00','GRA-L09','GRA-UL10','GRA-TL00','GRA-CL10'])
	lg = random.choice(['CPH1913','CPH1911'])
	sony = random.choice(['vivo 1935', 'V1965A'])
	vivo = random.choice(['SM-G313HU','SM-G316HU','SM-G316M'])
	fbcr = random.choice(["Zong","Jazz","Zong 4G","Zong CMPak","Jio 4G","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','ur_PK'])
	ft = ['SM-M625F','LM-K525', 'NID-1050','SM-A3051','CPH2069','RMX3286','A101XM','SM-A505GT','WKG-LX9','SM-A4260','Infinix X680C','RMX3265','GLA-LX1','Redmi 4X','V2204','vivo 2018','PCB-T104','2201122G','Infinix X688B','RMP2106','OXF-AN10','Infinix X6835B','CPH2399','SM-F731B','SM-T515','CPH2209','M2101K6R','V2135','SM-M307FN','JLN-LX3','CPH2123','Lenovo TB-X605F','V2110','RMX3572','LM-X420']
	su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
	so = random.choice(su)
	efg = random.choice(ft)
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/173.0.0.54.72;FBBV/3719472;FBDM/{density=2.0,width=720,height=1600};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3268;FBSV/11;FBOP/14;FBCA/arm64-v8a:;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/83.0.0.16.39;FBBV/1847294;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua4 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/83.0.0.16.39;FBBV/5274830;FBDM/{density=3.0,width=1080,height=2400};FBLC/"+fblc+";FBRV/261576428;FBCR/"+fbcr+";FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2239A;FBSV/11;FBOP/12;FBCA/arm64-v8a:;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/122.0.0.18.63;FBBV/389908;FBDM/{density=3.0,width=1080,height=2460};FBLC/"+fblc+";FBRV/0;FBCR/"+fbcr+";FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/X6833B;FBSV/13;FBCA/arm64-v8a:;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/10.0.0.47.73;FBBV/5818742;FBDM/{density=1.5,width=480,height=800};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/38.0.0.0.18;FBBV/5818742;FBDM/{density=2.5,width=720,height=1650};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.orca;FBDV/23129RN51X;FBSV/14;FBCA/arm64-v8a:;]"
	ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/111.0.0.55.148;FBBV/5816369;FBDM/{density=2.0,width=800,height=1280};FBLC/"+fblc+";FBRV/471924712;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/8.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua3 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/257.0.0.17.137;FBBV/2184026;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBRV/0;FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2185;FBSV/10;FBCA/arm64-v8a:;]"
	ua = str(random.choice([ua6,ua5,ua7,ua2,ua4,ua1,ua3,ua10]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
