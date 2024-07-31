import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-S901B','SM-S901B/DS','SM-S901U','SM-S901U1','SM-S901W','SM-S901N','SM-S9010','SM-S901E','SM-S901E/DS'])
	realme = random.choice(['CPH2083', 'CPH2077'])
	oppo = random.choice(['PRA-TL10','PRA-TL20','PRA-LA1','PRA-LX1','PRA-LX2','TAG-L21','PRA-AL00X','TAG-L32','PRA-LX3','PRA-AL00'])
	vivo = random.choice(['SM-J100F','SM-J100FN','SM-J100H','SM-J100H/DD','SM-J100H','SM-J100M','SM-J100MU','SM-J100ML','SM-J100VPP','SM-J100Y'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/154.0.0.26.159;FBBV/268946150;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBRV/619461836;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/12;FBOP/14;FBCA/arm64-v8a:;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/231.1.0.57.129;FBBV/377040;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/361926295;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/7.0;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/377040;FBDM/{density=2.75,width=720,height=1520};FBLC/"+fblc+";FBRV/174956283;FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/9.0;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/116.0.0.32.62;FBBV/666395;FBDM/{density=1.5,width=480,height=800};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/55.0.0.90.22;FBBV/20097172;FBDM/{density=2.8,width=800,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-T315;FBSV/4.2.2;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua1,ua7,ua6,ua5]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
