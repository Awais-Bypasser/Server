import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A710F','SM-A710S','SM-A710M','SM-A710FD','SM-A710Y','SM-A7100','SM-A710L','SM-A710K','SM-A7108'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['SCC-U21','SCL-U31','SCL-L21','SCL-L01','SCL-L04','SCL-AL00','HW-SCL-L32','SCL-TL00','SCL-L03','SCL-TL00H'])
	lg = random.choice(['LG-H650','LG-F620','LG-F620L','LG-F620K'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-G800H','SM-G800F','SM-G800M','SM-G800Y'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401182;FBDM/{density=3.0,width=1080,height=1920};FBLC/"+fblc+";FBRV/172947184;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/5.1.1;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/173957193;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/5.1;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/149.0.0.40.71;FBBV/79007703;FBDM/{density=2.0,width=720,height=1280};FBLC/pt_PT;FBRV/79424004;FBCR/vodafone P;FBMF/Vodafone;FBBD/Vodafone;FBPN/com.facebook.katana;FBDV/VFD 600;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/149.0.0.40.71;FBBV/79007703;FBDM/{density=2.0,width=720,height=1280};FBLC/"+fblc+";FBRV/184619462;FBCR/"+fbcr+";FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/5.1.1;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/326591638;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/"+vivo+";FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=720,height=1280};]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/264.0.0.44.111;FBBV/206636690;FBDM/{density=2.0,width=2560,height=1504};FBLC/da_DK;FBRV/208541728;FBCR/;FBMF/LENOVO;FBBD/Lenovo;FBPN/com.facebook.katana;FBDV/Lenovo YT-X703F;FBSV/7.1.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua5,ua7,ua6,ua1,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
