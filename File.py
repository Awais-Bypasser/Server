import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-N930V','SM-N930A','SM-N930P','SM-N930T','SM-N930R4','SM-N930W8','SM-N930F','SM-N930G','SM-N930S'])
	realme = random.choice(['SM-C9000','SM-C900F','SM-C9008','SM-C900Y'])
	oppo = random.choice(['FRL-22','FRL-23','FRL-L22','FRL-L23'])
	lg = random.choice(['LMG820QM7','LM-G820UMB','LMG820UM0','LMG820UM1','LMG820UM2','LM-G820N','LM-G820'])
	sony = random.choice(['F3111 F3113','F3115'])
	vivo = random.choice(['SM-G611F','SM-G611FF','SM-G611M','SM-G611MT','SM-G611K'])
	fbcr = random.choice(["Telenor","UFONE-PAKTel","Zong","Jazz","Jio","Vodafone","Airtel","BSNL","Robi","Banglalink","Zong 4G","LTE","Jio 4G","Ufone","UFONE-PK","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','ur_PK'])
	ft = ['SM-M625F','LM-K525', 'NID-1050','SM-A3051','CPH2069','RMX3286','A101XM','SM-A505GT','WKG-LX9','SM-A4260','Infinix X680C','RMX3265','GLA-LX1','Redmi 4X','V2204','vivo 2018','PCB-T104','2201122G','Infinix X688B','RMP2106','OXF-AN10','Infinix X6835B','CPH2399','SM-F731B','SM-T515','CPH2209','M2101K6R','V2135','SM-M307FN','JLN-LX3','CPH2123','Lenovo TB-X605F','V2110','RMX3572','LM-X420']
	su = ['QP1A.190711.020','QKQ1.190918.001','TP1A.220624.014','SP1A.210812.016','QTG3.200617.002','SQ3A.220705.0040','RP1A.200720.011']
	so = random.choice(su)
	efg = random.choice(ft)
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/173.0.0.54.72;FBBV/3719472;FBDM/{density=3.0,width=1440,height=2560};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/83.0.0.16.39;FBBV/1847294;FBDM/{density=3.0,width=1080,height=2400};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	ua4 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/83.0.0.16.39;FBBV/527644830;FBDM/{density=2.75,width=720,height=1280};FBLC/en_GB;FBRV/261732958;FBCR/Jazz;FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/"+sony+";FBSV/6.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/226.0.0.28.95;FBBV/31389908;FBDM/{density=4.0,width=1440,height=3120};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/LGE;FBBD/LGE;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/10.0.0.47.73;FBBV/5818742;FBDM/{density=3.0,width=1440,height=2560};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+samsung+";FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/38.0.0.0.18;FBBV/5818742;FBDM/{density=2.75,width=720,height=1480};FBLC/en_US;FBCR/MobileNation;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/Samsung Galaxy A54 5G;FBSV/8.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua1 = "Dalvik/2.1.0 (Linux; U; Android "+str(random.randint(4, 13))+"; "+efg+" Build/"+so+") [FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/348.0.0.39.118;FBBV/5816369;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/238159264;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/6.0.1;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua3 = "[FBAN/FB4A;FBAV/257.0.0.17.137;FBBV/20454026;FBDM/{density=3.0,width=1080,height=1776};FBLC/en_US;FBCR/T-Mobile;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D801;FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua6,ua5,ua7,ua1]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
