import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-G750F','SM-G7508','SM-G7508Q','SM-G750H','SM-G750A'])
	realme = random.choice(['RMX1992','RMX1993','RMX1991'])
	oppo = random.choice(['CAG-L02','CAG-L22','CAG-L23','CAG-L03'])
	lg = random.choice(['CPH2035','CPH2037','CPH2036'])
	sony = random.choice(['Infinix_X625','Infinix_X625B','Infinix_X625','Infinix_X625D'])
	xiaomi = random.choice(['23100RN82L','23106RN0DA','23108RN04Y','2311DRN14I'])
	vivo = random.choice(['SM-T715','SM-T710','SM-T719N','SM-T719','SM-T715Y','SM-T719Y','SM-T713'])
	fbcr = random.choice(["Zong","Jazz","Zong 4G","Zong CMPak","Jio 4G","null","Banglalink","Telenor","UFONE-PK"])
	fblc = random.choice(['en_US','en_GB','en_PK','ur_PK'])
	ft = ['SM-M625F','LM-K525', 'NID-1050','SM-A3051','CPH2069','RMX3286','A101XM','SM-A505GT','WKG-LX9','SM-A4260','Infinix X680C','RMX3265','GLA-LX1','Redmi 4X','V2204','vivo 2018','PCB-T104','2201122G','Infinix X688B','RMP2106','OXF-AN10','Infinix X6835B','CPH2399','SM-F731B','SM-T515','CPH2209','M2101K6R','V2135','SM-M307FN','JLN-LX3','CPH2123','Lenovo TB-X605F','V2110','RMX3572','LM-X420']
	su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
	so = random.choice(su)
	efg = random.choice(ft)
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/112.0.0.75.49;FBBV/5891723;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/17.0.0.37.72;FBBV/184729472;FBDM/{density=1.75,width=480,height=854};FBLC/"+fblc+";FBRV/243196785;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/8.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua4 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/26.0.0.48.61;FBBV/4671823;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+"FBCR/"+fbcr+";FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2029;FBSV/10;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/167.0.0.83.27;FBBV/3104738;FBDM/{density=2.75,width=720,height=1520};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/"+sony+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/10.0.0.47.73;FBBV/1047284;FBDM/{density=3.0,width=1536,height=2048};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/5.0.2;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/38.0.0.0.18;FBBV/3619526;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.orca;FBDV/"+xiaomi+";FBSV/13;FBCA/arm64-v8a:;]"
	ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/169.0.0.57.168;FBBV/5816369;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/341524712;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/4.4.3;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua3 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/257.0.0.17.137;FBBV/2184026;FBDM/{density=3.0,width=1080,height=2400};FBLC/"+fblc+";FBRV/185753291;FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/10;FBCA/arm64-v8a:;]"
	ua = str(random.choice([ua6,ua5,ua7,ua2,ua4,ua1,ua3,ua10]))  # Add ua6 to the list of choice
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
