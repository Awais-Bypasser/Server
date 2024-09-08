import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-G988','SM-G988U','SM-G988U1','SM-G9880','SM-G988B/DS','SM-G988N','SM-G988B','SM-G988W','SCG03'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['VNS-L31','VNS-L21','VNS-L22','VNS-L23','VNS-L53','VNS-AL00','VNS-L62','VNS-L52','VNS-DL00','VNS-TL00','DIG-L22'])
	lg = random.choice(['K220','LS755','US610','K450','LGLS755','F750K','K210','LGUS610'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-T116','SM-T116BU','SM-T116NQ','SM-T116NU','SM-T116NY'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=2.625,width=1080,height=2200};FBLC/en_US;FBRV/195717365;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/481759173;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/6.0;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/248.1.0.44.116;FBBV/184540762;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/0;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-S367VL;FBSV/9;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/291.0.0.44.120;FBBV/249604789;FBDM/{density=2.0,width=720,height=1280};FBLC/en_US;FBRV/251279628;FBCR/JIO 4G;FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/HM NOTE 1LTE;FBSV/4.4.4;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/284619275;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/"+vivo+";FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=1.0,width=600,height=1024};]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/85.0.0.15.70;FBBV/33678595;FBDM/{density=1.5,width=480,height=800};FBLC/pt_BR;FBCR/null;FBMF/LGE;FBBD/lge;FBPN/com.facebook.katana;FBDV/LG-D325;FBSV/4.4.2;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua10,ua5,ua7,ua6,ua1,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
