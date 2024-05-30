import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A505F','SM-A505FN','SM-A505GN','SM-A505G','SM-A505FM','SM-A505YN','SM-A505W','SM-A505X','SM-A505U','SM-A505GT','SM-A505U1','SM-A505G','SM-A505N','SM-S506DL'])
	realme = random.choice(['CPH2139', 'CPH2135'])
	oppo = random.choice(['TRT-L53','TRT-L21A','TRT-AL00','SLA-TL10','TRT-TL10','SLA-AL00','TRT-AL00A'])
	vivo = random.choice(['SM-T580','SM-T585','SM-P580','SM-P585','SM-P585Y'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/154.0.0.26.159;FBBV/268946150;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBRV/582916395;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/231.1.0.57.129;FBBV/377040;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/183682738;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/7.0;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/300.1.0.57.129;FBBV/377040;FBDM/{density=3.0,width=1080,height=2400};FBLC/"+fblc+";FBRV/571657194;FBCR/"+fbcr+";FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX2170;FBSV/10;FBCA/arm64-v8a:;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/56.0.0.46.12;FBBV/666395;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/7.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/35.0.0.54.34;FBBV/1263992;FBDM/{density=2.2,width=480,height=800};FBLC/tr_TR;FBCR/Basis Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G318H;FBSV/4.4;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua1,ua7,ua6,ua5,ua10]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
