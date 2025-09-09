import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A700F','SM-A700FD','SM-A700K','SM-A700L','SM-A700S','SM-A700X'])
	oppo = random.choice(['MRD-LX1F','MRD-LX1','MRD-LX3','MRD-LX1N'])
	vivo = random.choice(['SM-N920','SM-N9208','SM-N920CD','SM-N920C'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
	fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/122.0.0.45.119;FBBV/268946150;FBDM/{density=3.0,width=1440,height=2560};FBLC/"+fblc+";FBRV/461836582;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+vivo+";FBSV/5.1.1;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/377040;FBDM/{density=2.75,width=720,height=1560};FBLC/"+fblc+";FBRV/371856283;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/9.0;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/33.0.0.32.62;FBBV/666395;FBDM/{density=30,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+samsung+";FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/28.0.0.21.59;FBBV/20748110;FBDM/{density=2.5,width=1080,height=1920};FBLC/en_SX;FBCR/Defense Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900I;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua7,ua6,ua5]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
	
