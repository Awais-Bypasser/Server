import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['GM1911','GM1913','GM1917','GM1910','GM1915'])
	realme = random.choice(['SM-G386F', 'SM-G386T1'])
	oppo = random.choice(['CLT-L29C','CLT-L29','CLT-L09C','CLT-L09','CLT-AL00','CLT-AL01','CLT-TL01','CLT-AL00L','CLT-L04','HW-01K','CLT-L0J'])
	lg = random.choice(['K220','LS755','US610','K450','LGLS755','F750K','K210','LGUS610'])
	sony = random.choice(['D2303', 'D2305', 'D2306'])
	vivo = random.choice(['SM-G928A','SM-G928F','SM-G928A','SM-G928T','G928I','SM-G928G','SM-G928C','SM-G928I','SCV31','SM-G9280','SM-G928L','SM-G928S','SM-G928K','SM-G928W8'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/231.0.0.52.19;FBBV/371846295;FBDM/{density=3.25,width=1440,height=3120};FBLC/en_US;FBRV/195717365;FBCR/"+fbcr+";FBMF/OnePlus;FBBD/OnePlus;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/9.0;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/47.0.0.82.13;FBBV/172957294;FBDM/{density=3.0,width=1080,height=2240};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/10;FBCA/arm64-v8a:;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBPN/com.facebook.katana;FBLC/"+fblc+";FBRV/371294251;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/GT-S7560M;FBSV/4.0.4;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.5,width=480,height=800};FB_FW/1;]"
	ua2 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/411.1.0.29.112;FBBV/466874057;FBDM/{density=2.0,width=720,height=1456};FBLC/es_LA;FBRV/469414336;FBCR/TELCEL;FBMF/OPPO;FBBD/OPPO;FBPN/com.facebook.katana;FBDV/CPH2185;FBSV/10;FBOP/9;FBCA/arm64-v8a:;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/38.0.0.62.41;FBPN/com.facebook.orca;FBLC/"+fblc+";FBBV/481937692;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/"+vivo+";FBSV/6.0.1;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.15,width=1440,height=2560};]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";FBPN/com.facebook.orca;FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBDV/SM-A720F;FBSV/8.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=3.0,width=1080,height=1920};]"
	ua = str(random.choice([ua6,ua5,ua7]))  # Add ua6 to the list of choices
	ugeni.append(ua) # Append the randomly chosen user agent to the ugen list
