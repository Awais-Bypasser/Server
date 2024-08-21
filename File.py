import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-J727V','SM-J727P','SM-J727T','SM-J727F','SM-J727U','SM-J727S','SM-J727VPP','SM-J727AZ','SM-S727VL','SM-J727R4','SM-J727A'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['MYA-AL10','MYA-TL10','MYA-L03/L23','MYA-L02/L22','MYA-L11','MYA-L41'])
	lg = random.choice(['K220','LS755','US610','K450','LGLS755','F750K','K210','LGUS610'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-J415F','SM-J415FN','SM-J415G','SM-J415GN','SM-J415N'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=2.75,width=720,height=1280};FBLC/en_GB;FBRV/195717365;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/7.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/7.0;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/{density=3.0,width=1080,height=2147};FBLC/"+fblc+";FBRV/273494982;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/VOG-L09;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/{density=2.75,width=1080,height=2138};FBLC/cs_CZ;FBRV/272618289;FBCR/"+fbcr+";FBMF/Xiaomi;FBBD/Xiaomi;FBPN/com.facebook.katana;FBDV/Mi Note 10;FBSV/10;FBOP/1;FBCA/arm64-v8a:;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/284619275;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/"+samsung+";FBSV/7.0.1;nullFBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=720,height=1280};]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/{density=2.25,width=720,height=1372};FBLC/en_GB;FBRV/271849603;FBCR/null;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A600FN;FBSV/10;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua10,ua5,ua7,ua6,ua1,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
