import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A908B', 'SM-A908N', 'SM-A9080'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['LDN-L21', 'LDN-LX2', 'LDN-TL10'])
	lg = random.choice(['K220','LS755','US610','K450','LGLS755','F750K','K210','LGUS610'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-J415F','SM-J415FN','SM-J415G','SM-J415GN','SM-J415N'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/{density=2.625.0,width=1080,height=2198};FBLC/en_GB;FBRV/0;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/{density=2.0,width=720,height=1360};FBLC/en_GB;FBRV/156625696;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/8.0.0;FBOP/19;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/{density=1.5,width=854,height=480};FBLC/"+fblc+";FBRV/93722336;FBCR/"+fbcr+";FBMF/WIKO;FBBD/WIKO;FBPN/com.facebook.katana;FBDV/FREDDY;FBSV/6.0.1;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBPN/com.facebook.orca;FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/OPPO;FBBD/OPPO;FBDV/CPH1987;FBSV/9;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=2196};FB_FW/1;] FBBK/1"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBPN/com.facebook.orca;FBLC/en_GB;FBBV/187555057;FBCR/"+fbcr+";FBMF/LGE;FBBD/lge;FBDV/LML713DL;FBSV/8.1.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.625,width=1080,height=2034};]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77)) +";FBBV/"+str(random.randint(1111111,7777777))+";FBDM/{density=2.9,width=1440,height=2560};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-N9208;FBSV/7.0;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua10,ua5,ua7,ua6,ua1,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
