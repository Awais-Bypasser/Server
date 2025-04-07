import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A505F','SM-A505FN','SM-A505GN','SM-A505G','SM-A505FM','SM-A505YN','SM-A505W','SM-A505X','SM-A505U','SM-A505GT','SM-A505U1','SM-A505G','SM-A505N','SM-S506DL'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['WAS-LX1','WAS-LX2','WAS-LX3','WAS-LX1A','WAS-LX2J','WAS-L03T','WAS-AL00','WAS-TL10'])
	lg = random.choice(['LM-G710','LM-G710N','LM-G710VM','G710','SM-G710','LM-G710V'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-N910C','SM-N910S','SM-N910H','SM-N910F','SM-N910G','SM-N910U','SM-N910K','SM-N916S','SM-N910L','SM-N916L','SM-N916K','SM-N910T3'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401182;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBRV/471846792;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/481759173;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/7.0;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/28.0.0.62.73;FBBV/13358203;FBDM/{density=2.3,width=838,height=1622};FBLC/fr_BJ;FBCR/Total Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/SM-G357FZ;FBSV/None;nullFBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/149.0.0.40.71;FBBV/79007703;FBDM/{density=4.0,width=1440,height=3120};FBLC/"+fblc+";FBRV/184619462;FBCR/"+fbcr+";FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/8.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/326591638;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/"+vivo+";FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=1440,height=2560};]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/25.0.0.43.37;FBBV/77868908;FBDM/{density=3.7,width=807,height=2168};FBLC/es_US;FBCR/H2O Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-J327T1;FBSV/8.4.6;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua5,ua7,ua6,ua1,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
