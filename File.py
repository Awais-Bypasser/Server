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
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/Orca-Android;FBAV/77.0.0.52.75;FBBV/82308353;FBDM/{density=2.75,width=720,height=1280};FBLC/en_PK;FBCR/Good2GO Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/TRT-L53;FBSV/7.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FBIOS;FBAV/481.1.0.52.106;FBBV/641447568;FBDV/iPad14,11;FBMD/iPad;FBSN/iPadOS;FBSV/17.6.1;FBSS/2;FBID/tablet;FBLC/en_US;FBOP/5;FBRV/0]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/381.0.0.29.105;FBBV/61498731;FBDM/{density=2.75,width=720,height=1600};FBLC/en_GB;FBCR/Jazz;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A215U1;FBSV/11;FBCA/arm64-v8a:;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/402.1.0.24.84;FBBV/12600906;FBDM/{density=3.0,width=1080,height=1920};FBLC/en_US;FBCR/Zong;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-A9000;FBSV/6.0.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua5,ua6,ua2,ua7]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
