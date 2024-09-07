import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A715F','SM-A715F/DS','SM-A715F/DSN','SM-A715F/DSM','SM-A715W','SM-A715X'])
	realme = random.choice(['SM-T235','SM-T235Y','SM-T239'])
	oppo = random.choice(['ATU-L11','ATU-LX3','ATU-L21','ATU-L22'])
	lg = random.choice(['LG-F520K', 'LG-F520L'])
	sony = random.choice(['X652B', 'X652C'])
	vivo = random.choice(['SM-G9250','SM-G925A','SM-G925F','SM-G925FQ','SM-G925I','SM-G925K','SM-G925L','SM-G925S','SM-G925T','SC-04G','404SC','SM-G925D','SM-G925J'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/48.0.0.41.182;FBBV/2527396;FBDM/{density=3.0,width=1080,height=2400};FBLC/"+fblc+";FBRV/281857295;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/172.0.0.58.20;FBBV/4718395;FBDM/{density=2.75,width=720,height=1440};FBLC/"+fblc+";FBRV/471738572;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/8.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/281.0.0.28.173;FBBV/5829164;FBDM/{density=2.75,width=720,height=1600};FBLC/en_GB;FBRV/162956194;FBCR/"+fbcr+";FBMF/Infinix;FBBD/Infinix;FBPN/com.facebook.katana;FBDV/"+sony+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/281.0.0.31.192;FBBV/3715719;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/LGE;FBBD/LGE;FBPN/com.facebook.katana;FBDV/"+lg+";FBSV/4.4.2;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/24.0.0.11.92;FBBV/11516731;FBDM/{density=2.85,width=800,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+realme+";FBSV/4.4.2;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/233.0.0.101;FBBV/1072372067;FBDM/{density=3.0,width=1080,height=2340};FBLC/fr_FR;FBRV/732392479;FBCR/Verizon;FBMF/Samsung;FBBD/Samsung;FBPN/com.facebook.katana;FBDV/Samsung Galaxy S21;FBSV/14.0;nullFBCA/arm64-v8a:arm64;]"
	ua9 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/122.0.0.40.69;FBBV/61279955;FBDM/{density=3.0,width=1080,height=1920};FBLC/zh_Hant_TW;FBCR/Republic Wireless;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N900L;FBSV/5.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua5,ua7,ua6,ua1,ua9]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
