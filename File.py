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
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+"[FBAN/Orca-Android;FBAV/332.0.0.23.111;FBBV/75611219;FBDM/{density=1.85,width=480,height=800};FBLC/ar_YE;FBCR/Speedtalk Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-G361H;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/436.0.0.35.101;FBBV/59443893;FBDM/{density=2.85,width=720,height=1280};FBLC/ru_RU;FBCR/Xfinity Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-G550FY;FBSV/7.1.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/452.0.0.50.109;FBBV/94880105;FBDM/{density=2.9,width=1600,height=2560};FBLC/en_BW;FBCR/Speedtalk Mobile;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-P905V;FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/1547287;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/"+vivo+";FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=2.0,width=800,height=1280};]"
	ua = str(random.choice([ua6,ua5]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
