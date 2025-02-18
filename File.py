import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A305F','SM-A305FN','SM-A305G','SM-A305GN','SM-A305YN','SM-A3050','SM-A305N','SM-A305GT'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['FIG-LX1','FIG-LA1','FIG-LX2','FIG-LX3','FIG-TL10','FIG-AL10','FIG-AL00'])
	lg = random.choice(['K220','LS755','US610','K450','LGLS755','F750K','K210','LGUS610'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-J415F','SM-J415FN','SM-J415G','SM-J415GN','SM-J415N'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/266.0.0.56.124;FBBV/209027763;FBDM/{density=3.0,width=1080,height=2340};FBLC/en_US;FBRV/195717365;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/61.0.0.15.69;FBBV/20748110;FBDM/{density=3.0,width=1080,height=2160};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/HUAWEI "+oppo+";FBSV/8.0;FBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBPN/com.facebook.katana;FBLC/"+fblc+";FBRV/371294251;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/GT-S7560M;FBSV/4.0.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=800};FB_FW/1;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/411.1.0.29.112;FBBV/466874057;FBDM/{density=2.0,width=720,height=1456};FBLC/es_LA;FBRV/469414336;FBCR/TELCEL;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2185;FBSV/10;FBOP/9;FBCA/arm64-v8a:;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/439.0.0.29.119;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/284619275;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/"+vivo+";FBSV/8.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.75,width=720,height=1480};]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBPN/com.facebook.orca;FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};]"
	ua = str(random.choice([ua10,ua5,ua7,ua6,ua1,ua2]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
