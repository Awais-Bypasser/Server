import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-J106F','SM-J106B','SM-J106H','SM-J106M'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['MYA-L03','MYA-L23','MYA-L02','MYA-L22','MYA-U29','MYA-L13'])
	lg = random.choice(['LG-H502', 'LG-H500', 'LG-H520'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-J111F','SM-J110G','SM-J110F','SM-J110H','SM-J110M','SM-J110L','SM-J111M'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401182;FBDM/{density=1.75,width=480,height=800};FBLC/"+fblc+";FBRV/172947184;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/5.1;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/345.0.0.34.118;FBBV/332957690;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/173957193;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/6.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FBIOS;FBAV/165.0.0.74.96;FBBV/100174821;FBDV/iPhone9,3;FBMD/iPhone;FBSN/iOS;FBSV/11.2.6;FBSS/2;FBCR/Jazz;FBID/phone;FBLC/en_GB;FBOP/5;FBRV/100948865]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/149.0.0.40.71;FBBV/79007703;FBDM/{density=2.0,width=720,height=1280};FBLC/"+fblc+";FBRV/184619462;FBCR/"+fbcr+";FBMF/lge;FBBD/lge;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/5.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/326591638;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/"+vivo+";FBSV/4.4.4;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=1.75,width=480,height=800};]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/305.1.0.40.120;FBBV/272401182;FBDM/{density=1.75,width=540,height=960};FBLC/"+fblc+";FBRV/172947184;FBCR/"+fbcr+";FBMF/Sony;FBBD/Sony;FBPN/com.facebook.katana;FBDV/"+sony+";FBSV/4.3;FBOP/1;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua5,ua7,ua6,ua1,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
