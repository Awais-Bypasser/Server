import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A025F','SM-A025F/DS','SM-A025G','SM-A025G/DS','SM-A025M','SM-A025M/DS','SM-A025U','SM-A025V','SM-A025A','SM-A025U1','SM-A025AZ','SM-S124DL'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['EML-L29C','EML-L09C','EML-AL00 EML-TL00','EML-L29','EML-L09','EML-AL00','EML-TL00'])
	lg = random.choice(['K220','LS755','US610','K450','LGLS755','F750K','K210','LGUS610'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-E7000','SM-E7009','SM-E700F','SM-E700H','SM-E700H/DD','SM-E700H','SM-E700M'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401182;FBDM/{density=1.75,width=720,height=1600};FBLC/"+fblc+";FBRV/251947294;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/10;FBOP/19;FBCA/arm64-v8a:;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=3.0,width=1080,height=2240};FBLC/"+fblc+";FBRV/481759173;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/8.1;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FBIOS;FBAV/168.0.0.57.90;FBBV/96876057;FBDV/iPhone7,2;FBMD/iPhone;FBSN/iOS;FBSV/15.8.1;FBSS/2;FBCR/Beeline;FBID/phone;FBLC/ru_RU;FBOP/5;FBRV/0]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/356.0.0.28.112;FBBV/353870802;FBDM/{density=2.75,width=1080,height=2168};FBLC/ru_RU;FBRV/0;FBCR/HOT mobile;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 9 Pro;FBSV/11;FBOP/1;FBCA/arm64-v8a:;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/284619275;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/"+vivo+";FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=720,height=1280};]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/356.0.0.28.112;FBBV/353870747;FBDM/{density=2.625,width=1080,height=2195};FBLC/ru_RU;FBRV/0;FBCR/MTS RUS;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A315F;FBSV/11;FBOP/19;FBCA/arm64-v8a:;]"
	ua = str(random.choice([ua10,ua5,ua7,ua6,ua1,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
