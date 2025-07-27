import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-G990B','SM-G990B/DS','SM-G990U','SM-G990U1','SM-G990W','SM-G990E','SM-G9900','SM-G990B2','SM-G990U2','SM-G990W2','SM-G990U3'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['ALE-L04', 'ALE-TL00'])
	lg = random.choice(['K220','LS755','US610','K450','LGLS755','F750K','K210','LGUS610'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-G955F','SM-G955FD','SM-G955W','SM-G955A','SM-G955P','SM-G955T','SM-G955V','SM-G955R4','SM-G955U','SM-G955S','SM-G955K','SM-G955L','SM-G955','SM-G955U1','SM-G955N','SM-G9550','SC-03J','G955F'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401182;FBDM/{density=3.0,width=1080,height=2340};FBLC/"+fblc+";FBRV/251947294;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/12;FBOP/14;FBCA/arm64-v8a:;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/481759173;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/4.4.4;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/351.0.0.38.117;FBBV/347007269;FBDM/{density=2.75,width=1080,height=2134};FBLC/ru_RU;FBRV/348304748;FBCR/UA-KYIVSTAR;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/M2004J19C;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/149.0.0.40.71;FBBV/79007703;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/184619462;FBCR/"+fbcr+";FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/6.0.1;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/284619275;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/"+vivo+";FBSV/7.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1440,height=2960};]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/352.0.0.21.117;FBBV/348184967;FBDM/{density=3.0,width=2138,height=1080};FBLC/ru_RU;FBRV/349245423;FBCR/Vodafone UA;FBMF/HUAWEI;FBBD/HONOR;FBPN/com.facebook.katana;FBDV/JSN-L21;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	ua = str(random.choice([ua5,ua7,ua6,ua1,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
