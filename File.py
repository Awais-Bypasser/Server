import random
ugeni = []
for agents in range(100000):
	samsung = random.choice(['SM-A8000','SM-A800F','SM-A800Y','SM-A800I','SM-A800IZ','SM-A800S','SM-A800YZ'])
	realme = random.choice(['RMX2027','RMX2020'])
	oppo = random.choice(['CRO-L02','CRO-L22','CRO-L03','CRO-L23','CRO-U00'])
	lg = random.choice(['D335','D331','D335E'])
	vivo1 = random.choice(['21061119AG','21061119DG','21061119AL'])
	sony = random.choice(['CPH2127','CPH2131'])
	vivo = random.choice(['SM-M105F','SM-M105G','SM-M105Y','SM-M105M'])
	fbcr = random.choice(["Zong","Jazz","Zong 4G","UFONE-PK","Telenor"])
	fblc = random.choice(['en_US','en_GB','en_PK'])
	ft = ['SM-M625F','LM-K525', 'NID-1050','SM-A3051','CPH2069','RMX3286','A101XM','SM-A505GT','WKG-LX9','SM-A4260','Infinix X680C','RMX3265','GLA-LX1','Redmi 4X','V2204','vivo 2018','PCB-T104','2201122G','Infinix X688B','RMP2106','OXF-AN10','Infinix X6835B','CPH2399','SM-F731B','SM-T515','CPH2209','M2101K6R','V2135','SM-M307FN','JLN-LX3','CPH2123','Lenovo TB-X605F','V2110','RMX3572','LM-X420']
	su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
	so = random.choice(su)
	efg = random.choice(ft)
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/113.0.0.43.29;FBBV/3719472;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3381;FBSV/10;FBOP/12;FBCA/arm64-v8a:;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/83.0.0.16.39;FBBV/1847294;FBDM/{density=1.75,width=480,height=854};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/6.0;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua4 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/317.0.0.64.95;FBBV/5274830;FBDM/{density=3.01,width=1080,height=2408};FBLC/en_PK;FBCR/Jazz;FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/V2036;FBSV/11;FBOP/11;FBCA/arm64-v8a:;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/122.0.0.18.63;FBBV/389908;FBDM/{density=1.25,width=480,height=854};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/LGE;FBBD/LGE;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/4.4.2;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/34.0.0.57.13;FBBV/2715827;FBDM/{density=2.25,width=720,height=1520};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/9.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/351.0.0.46.163;FBBV/5714827;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_PK;FBRV/315725729;FBCR/Jazz;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/5.1;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua3 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/257.0.0.17.137;FBBV/2184026;FBDM/{density=3.0,width=1080,height=2400};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/"+vivo1+";FBSV/11;FBCA/arm64-v8a:;]"
	ua8 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/172.0.0.37.61;FBBV/5812586;FBDM/{density=2.75,width=720,height=1600};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+sony+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	ua = str(random.choice([ua1,ua6,ua4,ua2,ua7,ua3,ua8]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
