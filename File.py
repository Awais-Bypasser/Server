import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A600F','SM-A600FN','SM-A600A','SM-A600G','SM-A600GN','SM-A600P','SM-A600N','SM-A600T1','SM-A600AZ','SM-A600T','SM-A600U'])
	oppo = random.choice(['GT-I9500','SGH-I337M','SGH-M919','GT-I9507V','SHV-E330L','SPH-L720T','SHV-E300S','SHV-E300L','SHV-E300K','GT-I9507','SGH-M919N'])
	vivo = random.choice(['JMM-AL00','JMM-AL10','JMM-TL00','JMM-TL10','JMM-L22'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three"])
	fblc = random.choice(["ja_JP","ex_MX","en_CU","en_US","fr_FR","fa_IR","es_ES","pt_BR","de_DE","it_IT","ja_JP","ko_KR","ru_RU","zh_CN","ar_AE","en_GB"])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/122.0.0.45.119;FBBV/268946150;FBDM/{density=2.75,width=720,height=1480};FBLC/"+fblc+";FBRV/284917295;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/8.0;FBOP/1;FBCA/arm64-v8a:;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/377040;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/471375514;FBCR/"+fbcr+";FBMF/HONOR;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/"+vivo+";FBSV/7.0;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/33.0.0.32.62;FBBV/666395;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+oppo+";FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/28.0.0.21.59;FBBV/20748110;FBDM/{density=2.5,width=1080,height=1920};FBLC/en_SX;FBCR/Defense Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G900I;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua10,ua6,ua5]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
