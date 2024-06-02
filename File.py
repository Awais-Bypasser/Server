import random
ugeni = []
for agents in range(10000):
	samsung = random.choice(['SM-A115F','SM-A115M','SM-A115M/DS','SM-A115U','SM-A115A','SM-A115AZ','SM-A115U1','SM-A115W','SM-A115AP','SM-S115DL'])
	realme = random.choice(['V2025', 'V2024'])
	oppo = random.choice(['CUN-U29','CUN-U19','CUN-U09','CUN-L21','CUN-L22','CUN-L01','CUN-L02','CUN-L03','CUN-L33','CUN-L23'])
	vivo = random.choice(['SM-G928A','SM-G928F','SM-G928A','SM-G928T','G928I','SM-G928G','SM-G928C','SM-G928I','SCV31','SM-G9280','SM-G928L','SM-G928S','SM-G928K','SM-G928W8'])
	fbcr = random.choice(["Telenor","fido","MOVO AFRICA","UFONE-PAKTel","Zong","Jazz","SCO","Jio","Vodafone","Airtel","BSNL","MTNL","Grameenphone","Robi","Banglalink","Teletalk","Telkomsel","Indosat Ooredoo","Axiata","Tri","Smartfren","China Mobile","Unicom","Telecom","Satcom","Docomo","Rakuten","IIJmio","Orange","Verizon","AT&T","T-Mobile","Sprint","Vodafone","Telefonica","EE","Orange","Three","null"])
	fblc = random.choice(['en_US','en_GB','en_PK','es_LA','fr_FR','ur_PK','en_LA'])
	ua6 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/181.0.0.13.119;FBBV/285816395;FBDM/{density=2.75,width=720,height=1560};FBLC/"+fblc+";FBRV/183967293;FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/"+samsung+";FBSV/4.3;FBOP/1;FBCA/armeabi-v7a:armeabi;]"
	ua5 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/151.0.0.17.169;FBBV/471958164;FBDM/{density=2.75,width=720,height=1280};FBLC/"+fblc+";FBRV/461936591;FBCR/"+fbcr+";FBMF/HUAWEI;FBBD/HUAWEI;FBPN/com.facebook.katana;FBDV/"+oppo+";FBSV/5.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua1 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/110.0.0.17.269;FBBV/682819375;FBDM/{density=3.0,width=1080,height=2400};FBLC/"+fblc+";FBRV/61838561;FBCR/"+fbcr+";FBMF/vivo;FBBD/vivo;FBPN/com.facebook.katana;FBDV/"+realme+";FBSV/11;FBCA/arm64-v8a:;]"
	ua7 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/Orca-Android;FBAV/182.0.0.21.173;FBBV/666395;FBDM/{density=3.0,width=1440,height=2560};FBLC/"+fblc+";FBCR/"+fbcr+";FBMF/samsung;FBBD/samsung;FBPN/com.facebook.orca;FBDV/"+vivo+";FBSV/5.1.1;nullFBCA/armeabi-v7a:armeabi;]"
	ua10 = "[FBAN/FB4A;FBAV/"+str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,77))+";FBBV/"+str(random.randint(1111111,7777777))+";[FBAN/FB4A;FBAV/196.0.0.40;FBBV/992583544;FBDM/{density=1.5,width=1080,height=1080};FBLC/ca_FR;FBRV/908081925;FBCR/USA Communications;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A2070;FBSV/6.2.4;nullFBCA/armeabi-v7a:armeabi;]"
	ua = str(random.choice([ua7,ua6,ua5,ua1]))  # Add ua6 to the list of choices
	ugeni.append(ua10) # Append the randomly chosen user agent to the ugen list
