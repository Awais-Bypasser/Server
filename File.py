import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-J320H','SM-J3109','SM-J320FN','SM-J320P','SM-J320F','SM-J320M','SM-J320Y','SM-J320A','SM-J320G','SM-J327T1','SM-J320V','SM-J320YZ','SM-J320W8','SM-J320ZN','SM-J320N0','SM-J320R4'])
	realme = random.choice(['LS995','D955','D959','D958','D950','F340','F340L','LGL23'])
	oppo = random.choice(['LYO-L21','LYO-L01','CAM-L21'])
	vivo = random.choice(['SM-T715','SM-T710','SM-T719N','SM-T719','SM-T715Y','SM-T719Y','SM-T713'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/181.0.0.13.119;FBBV/285816395;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/721847193;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/5.1.1;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/151.0.0.17.169;FBBV/471958164;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/461936591;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/367.0.0.24.107;FBBV/370253085;FBDM/{density=3.0,width=1080,height=2401};FBLC/"+fblc+";FBRV/175926496;FBCR/Verizon;FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/4.2.2;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/182.0.0.21.173;FBBV/666395;FBDM/{density=2.7,width=768,height=1024};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-P355;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/196.0.0.12;FBBV/469120846;FBDM/{density=3.0,width=720,height=720};FBLC/fr_HT;FBRV/272178288;FBCR/Credo Mobile;FBMF/realme;FBBD/realme;FBPN/com.facebook.katana;FBDV/RMX3472;FBSV/11.1.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua1,ua5,ua7,ua6]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
