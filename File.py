import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A600F','SM-A600FN','SM-A600A','SM-A600G','SM-A600GN','SM-A600P','SM-A600N','SM-A600T1','SM-A600AZ','SM-A600T','SM-A600U'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['CRO-L02','CRO-L22','CRO-L03','CRO-L23','CRO-U00'])
	lg = random.choice(['LG-H870','LG-H870DS','LG-H873','LG-H870S','LG-LGM-G600L','LG-H872','LG-H871','LG-LS993','LG-US997','LG-vs988','LG-VS988','LG-LGM-G600K','LG-LGM-G600S','LG-AS993','LG-LGUS997','LG-H870AR','LG-H872PR','LG-H871S','LG-H870I'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-T377W','SM-T377','SM-T375','SM-T377P','SM-T377R','SM-T377A','SM-T378V','SM-T377V'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401182;FBDM/{density=2.25,width=720,height=1480};FBLC/"+fblc+";FBRV/172947184;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/8.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=1.75,width=480,height=854};FBLC/"+fblc+";FBRV/124613835;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/6.0;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/149.0.0.40.71;FBBV/79007703;FBDM/{density=3.0,width=1440,height=2880};FBLC/"+fblc+";FBRV/261846287;FBCR/"+fbcr+";FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/7.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/1547287;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/"+vivo+";FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=800,height=1280};]"
	ua = str(random.choice([ua6,ua5,ua7,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
