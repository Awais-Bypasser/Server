import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A5000','SM-A5009','SM-A500F','SM-A500F1','SM-A500FQ','SM-A500FU','SM-A500G','SM-A500H','SM-A500HQ','SM-A500K','SM-A500L','SM-A500S','SM-A500YZ','SM-A500Y','SM-A500W'])
	realme = random.choice(['SM-P600', 'SM-P601', 'SM-P605'])
	oppo = random.choice(['BAC-AL00','BAC-L03','BAC-L23','BAC-L21','BAC-L22','BAC-TL00'])
	vivo = random.choice(['GT-I8190','GT-I8190N','GT-I8190L','SM-G730A','SM-G730W8'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/181.0.0.13.119;FBBV/285816395;FBDM/{density=3.0,width=1536,height=2048};FBLC/"+fblc+";FBRV/721847193;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/4.4.4;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/151.0.0.17.169;FBBV/471958164;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/461936591;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/7.0;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/177.0.0.24.107;FBBV/370253085;FBDM/{density=3.0,width=1600,height=2560};FBLC/"+fblc+";FBRV/175926496;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/4.3;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/182.0.0.21.173;FBBV/666395;FBDM/{density=1.75,width=480,height=800};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/4.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/196.0.0.12;FBBV/469120846;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/272178288;FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH1707;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua1,ua5,ua7,ua6,ua10]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
